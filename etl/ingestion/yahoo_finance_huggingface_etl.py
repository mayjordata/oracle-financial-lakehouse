#!/usr/bin/env python3
"""
Consolidated Yahoo Finance ETL Pipeline
Final production-ready script for scheduled execution
"""

import os
import logging
from datetime import datetime, timezone
from typing import List, Dict, Optional, Tuple
import requests
import pandas as pd
import oci
from pathlib import Path
import time
import argparse
import json
from dataclasses import dataclass

# Configure logging
def setup_logging(log_level: str = "INFO", log_file: Optional[str] = None):
    """Setup logging configuration"""
    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=handlers
    )
    return logging.getLogger(__name__)

@dataclass
class ProcessingResult:
    """Data class for file processing results"""
    filename: str
    success: bool
    rows: Optional[int] = None
    file_size_mb: Optional[float] = None
    processing_time: Optional[float] = None
    error_message: Optional[str] = None
    uploaded_path: Optional[str] = None

class YahooFinanceHuggingFaceETL:
    """
    Production-ready ETL pipeline for Yahoo Finance data from Hugging Face
    """
    
    def __init__(self, 
                 config_file_path: str = "~/.oci/config",
                 profile_name: str = "DEFAULT",
                 compartment_id: str = None,
                 bucket_name: str = "finance-raw",
                 temp_dir: str = "temp_data"):
        """Initialize the ETL pipeline"""
        self.config_file_path = os.path.expanduser(config_file_path)
        self.profile_name = profile_name
        self.compartment_id = compartment_id
        self.bucket_name = bucket_name
        self.temp_dir = Path(temp_dir)
        self.temp_dir.mkdir(exist_ok=True)
        
        self.logger = logging.getLogger(__name__)
        
        # Dataset source configuration
        self.source_name = "yahoo_finance_huggingface"
        self.base_url = "https://huggingface.co/datasets/bwzheng2010/yahoo-finance-data/resolve/main/data"
        
        self.parquet_files = [
            "stock_profile.parquet",
            "stock_officers.parquet",
            "stock_statement.parquet",
            "stock_tailing_eps.parquet",
            "stock_earning_calendar.parquet",
            "stock_dividend_events.parquet",
            "stock_split_events.parquet",
            "stock_earning_call_transcripts.parquet",
            "stock_news.parquet",
            "stock_prices.parquet",
            "stock_revenue_breakdown.parquet",
            "daily_treasury_yield.parquet",
            "exchange_rate.parquet",
            "stock_shares_outstanding.parquet",
            "stock_sec_filing.parquet",
        ]
        
        # Initialize OCI client
        self._init_oci_client()
    
    def _init_oci_client(self):
        """Initialize OCI Object Storage client"""
        try:
            config = oci.config.from_file(self.config_file_path, self.profile_name)
            self.object_storage_client = oci.object_storage.ObjectStorageClient(config)
            self.namespace = self.object_storage_client.get_namespace().data
            self.logger.info(f"✅ Connected to OCI namespace: {self.namespace}")
        except Exception as e:
            self.logger.error(f"❌ Failed to initialize OCI client: {e}")
            raise
    
    def create_bucket_if_not_exists(self) -> bool:
        """Create bucket if it doesn't exist"""
        try:
            self.object_storage_client.get_bucket(self.namespace, self.bucket_name)
            self.logger.info(f"✅ Bucket '{self.bucket_name}' already exists")
            return True
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                try:
                    bucket_details = oci.object_storage.models.CreateBucketDetails(
                        name=self.bucket_name,
                        compartment_id=self.compartment_id
                    )
                    self.object_storage_client.create_bucket(self.namespace, bucket_details)
                    self.logger.info(f"✅ Created bucket: {self.bucket_name}")
                    return True
                except Exception as create_error:
                    self.logger.error(f"❌ Failed to create bucket: {create_error}")
                    return False
            else:
                self.logger.error(f"❌ Error accessing bucket: {e}")
                return False
    
    def download_file(self, filename: str, max_retries: int = 3) -> Tuple[bool, Optional[str]]:
        """Download a single parquet file with retry logic"""
        url = f"{self.base_url}/{filename}"
        local_path = self.temp_dir / filename
        
        for attempt in range(max_retries):
            try:
                self.logger.info(f"📥 Downloading {filename} (attempt {attempt + 1}/{max_retries})")
                
                response = requests.get(url, stream=True, timeout=300)
                response.raise_for_status()
                
                with open(local_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                # Verify file was downloaded
                if local_path.exists() and local_path.stat().st_size > 0:
                    self.logger.info(f"✅ Downloaded {filename} ({local_path.stat().st_size / 1024 / 1024:.2f} MB)")
                    return True, str(local_path)
                
            except Exception as e:
                self.logger.warning(f"⚠️  Download attempt {attempt + 1} failed for {filename}: {e}")
                if local_path.exists():
                    local_path.unlink()
                
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff
        
        self.logger.error(f"❌ Failed to download {filename} after {max_retries} attempts")
        return False, None
    
    def validate_and_get_info(self, file_path: str) -> Tuple[bool, Dict]:
        """Validate parquet file and get metadata"""
        try:
            df = pd.read_parquet(file_path)
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            
            info = {
                'rows': len(df),
                'columns': len(df.columns),
                'file_size_mb': round(file_size_mb, 2),
                'column_names': list(df.columns),
                'memory_usage_mb': round(df.memory_usage(deep=True).sum() / (1024 * 1024), 2)
            }
            
            self.logger.info(f"✅ Validated {Path(file_path).name}: {info['rows']:,} rows, {info['columns']} cols, {info['file_size_mb']} MB")
            return True, info
            
        except Exception as e:
            self.logger.error(f"❌ Validation failed for {Path(file_path).name}: {e}")
            return False, {'error': str(e)}
    
    def upload_to_object_storage(self, local_path: str, filename: str) -> Tuple[bool, Optional[str]]:
        """Upload file to Oracle Object Storage - Simple overwrite approach"""
        try:
            # Source-specific path structure - no date folders, always overwrite
            object_name = f"raw_data/{self.source_name}/{filename}"
            
            with open(local_path, 'rb') as f:
                self.object_storage_client.put_object(
                    namespace_name=self.namespace,
                    bucket_name=self.bucket_name,
                    object_name=object_name,
                    put_object_body=f
                )
            
            self.logger.info(f"✅ Uploaded/Updated: oci://{self.bucket_name}/{object_name}")
            return True, object_name
            
        except Exception as e:
            self.logger.error(f"❌ Upload failed for {filename}: {e}")
            return False, None
    
    def cleanup_temp_file(self, file_path: str):
        """Remove temporary file"""
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
                self.logger.debug(f"🧹 Cleaned up temp file: {file_path}")
        except Exception as e:
            self.logger.warning(f"⚠️  Failed to cleanup {file_path}: {e}")
    
    def process_file(self, filename: str) -> ProcessingResult:
        """Process a single file through the full pipeline"""
        start_time = time.time()
        
        try:
            # Download
            download_success, local_path = self.download_file(filename)
            if not download_success:
                return ProcessingResult(filename, False, error_message="Download failed")
            
            # Validate and get metadata
            valid, info = self.validate_and_get_info(local_path)
            if not valid:
                self.cleanup_temp_file(local_path)
                return ProcessingResult(filename, False, error_message=info.get('error', 'Validation failed'))
            
            # Upload
            upload_success, object_path = self.upload_to_object_storage(local_path, filename)
            if not upload_success:
                self.cleanup_temp_file(local_path)
                return ProcessingResult(filename, False, error_message="Upload failed")
            
            # Cleanup
            self.cleanup_temp_file(local_path)
            
            processing_time = time.time() - start_time
            
            return ProcessingResult(
                filename=filename,
                success=True,
                rows=info['rows'],
                file_size_mb=info['file_size_mb'],
                processing_time=round(processing_time, 2),
                uploaded_path=object_path
            )
            
        except Exception as e:
            self.logger.error(f"❌ Unexpected error processing {filename}: {e}")
            return ProcessingResult(filename, False, error_message=str(e))
    
    def run_pipeline(self, 
                    selected_files: Optional[List[str]] = None) -> Dict:
        """Run the complete ETL pipeline - Always downloads and overwrites"""
        
        start_time = time.time()
        self.logger.info("🚀 Starting Yahoo Finance Hugging Face ETL Pipeline")
        
        # Create bucket if needed
        if not self.create_bucket_if_not_exists():
            raise Exception("Failed to create/access bucket")
        
        # Determine files to process
        files_to_process = selected_files or self.parquet_files
        
        # Process each file
        results = []
        successful = 0
        failed = 0
        
        for filename in files_to_process:
            self.logger.info(f"📊 Processing {filename} ({files_to_process.index(filename) + 1}/{len(files_to_process)})")
            
            result = self.process_file(filename)
            results.append(result)
            
            if result.success:
                successful += 1
                self.logger.info(f"✅ Success: {filename}")
            else:
                failed += 1
                self.logger.error(f"❌ Failed: {filename} - {result.error_message}")
        
        # Generate summary
        total_time = time.time() - start_time
        summary = {
            'total_files': len(files_to_process),
            'successful': successful,
            'failed': failed,
            'total_processing_time': round(total_time, 2),
            'results': results,
            'execution_timestamp': datetime.now(timezone.utc).isoformat()
        }
        
        self.logger.info(f"🎯 Pipeline Complete: {successful}/{len(files_to_process)} successful in {total_time:.2f}s")
        return summary
    
    def generate_report(self, results: Dict, output_file: str = None) -> str:
        """Generate detailed execution report"""
        
        report_lines = [
            "=" * 80,
            "YAHOO FINANCE HUGGING FACE ETL PIPELINE EXECUTION REPORT",
            "=" * 80,
            f"Execution Time: {results['execution_timestamp']}",
            f"Total Processing Time: {results['total_processing_time']} seconds",
            f"Success Rate: {results['successful']}/{results['total_files']} ({results['successful']/results['total_files']*100:.1f}%)",
            "",
            "FILE PROCESSING DETAILS:",
            "-" * 40
        ]
        
        for result in results['results']:
            status = "✅ SUCCESS" if result.success else "❌ FAILED"
            report_lines.append(f"{status}: {result.filename}")
            
            if result.success:
                report_lines.append(f"    Rows: {result.rows:,}")
                report_lines.append(f"    File Size: {result.file_size_mb} MB") 
                report_lines.append(f"    Processing Time: {result.processing_time}s")
                report_lines.append(f"    Uploaded To: {result.uploaded_path}")
            else:
                report_lines.append(f"    Error: {result.error_message}")
            report_lines.append("")
        
        report = "\n".join(report_lines)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report)
            self.logger.info(f"📝 Report saved to: {output_file}")
        
        return report

def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description="Yahoo Finance Hugging Face ETL Pipeline")
    parser.add_argument("--compartment-id", required=True, help="OCI Compartment ID")
    parser.add_argument("--bucket-name", default="finance-raw", help="Object storage bucket name")
    parser.add_argument("--files", nargs="+", help="Specific files to process (optional)")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    parser.add_argument("--log-file", help="Log file path (optional)")
    parser.add_argument("--report-file", help="Report output file (optional)")
    
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logging(args.log_level, args.log_file)
    
    try:
        # Initialize and run pipeline
        etl = YahooFinanceHuggingFaceETL(
            compartment_id=args.compartment_id,
            bucket_name=args.bucket_name
        )
        
        results = etl.run_pipeline(selected_files=args.files)
        
        # Generate report
        report = etl.generate_report(results, args.report_file)
        print(report)
        
        # Exit with error code if any files failed
        exit_code = 0 if results['failed'] == 0 else 1
        return exit_code
        
    except Exception as e:
        logger.error(f"💥 Pipeline failed: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
