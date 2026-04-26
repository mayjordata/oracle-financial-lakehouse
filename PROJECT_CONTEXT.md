# Project Context — Oracle Cloud Financial Data Lakehouse

> This document provides comprehensive context for Claude Code (or any AI assistant) to assist with this project. Read this first before making changes.

## Project Summary

A learning-focused, production-grade ETL pipeline for financial market data analysis built on Oracle Cloud Infrastructure. Goals are split between practical infrastructure (a working data lakehouse) and skill development (data engineering, cloud, financial analysis).

**Owner**: DMay  
**Started**: April 2026  
**Current Phase**: 1B — Transform Layer Development

## Three-Environment Architecture

This project lives in three places that must stay in sync via Git:

1. **Local machine** — Development environment (where Claude Code runs)
2. **GitHub** — Version control source of truth
3. **OCI Compute Instance** — Production runtime (has OCI credentials, runs scheduled jobs)

Workflow: edit locally → push to GitHub → pull on OCI instance → run there.

## Infrastructure

### OCI Compute Instance
- **Shape**: VM.Standard.A1.Flex (ARM, always-free tier)
- **Resources**: 4 OCPUs, 32 GB RAM (upgraded from 24 GB)
- **OS**: Ubuntu 24.04 LTS
- **Boot Volume**: 50 GB
- **Cost optimization**: Scheduled start/stop via cron

### OCI Object Storage
- **Bucket**: `finance-raw`
- **Structure**:
```
  finance-raw/
  ├── raw_data/
  │   └── yahoo_finance_huggingface/    ← 20 parquet files
  └── curated_data/                     ← Transform outputs
```

### Authentication
- Config: `~/.oci/config` (DEFAULT profile, API key auth)
- Future: migrate to instance principal authentication

## Data Pipeline

### Source: Yahoo Finance via Hugging Face
- **Dataset**: `bwzheng2010/yahoo-finance-data`
- **URL**: https://huggingface.co/datasets/bwzheng2010/yahoo-finance-data
- **Files**: 20 parquet files (~1-3 GB total)
- **Update behavior**: Source maintainer updates files in place with same names

### Files (20 total)

**Price & Market Data:**
- `stock_prices.parquet` — OHLCV historical
- `treasury_yield.parquet` — Treasury yield curves
- `exchange_rate.parquet` — FX rates

**Company Fundamentals:**
- `stock_income.parquet` — Income statements
- `stock_balance_sheet.parquet` — Balance sheets
- `stock_cash_flow.parquet` — Cash flow statements
- `stock_profile.parquet` — Company profiles
- `stock_officers.parquet` — Executives

**Earnings & Estimates:**
- `stock_earning_calendar.parquet`
- `stock_earning_estimate.parquet`
- `stock_revenue_estimate.parquet`
- `stock_earning_call_transcripts.parquet`

**Market Activity:**
- `stock_dividends.parquet`
- `stock_splits.parquet`
- `stock_news.parquet`
- `stock_shares_outstanding.parquet` ⚠️ *Originally omitted from script, manually added*

**Analytics:**
- `stock_key_stats.parquet`
- `stock_summary.parquet`
- `stock_tailing_eps.parquet`
- `stock_revenue_breakdown.parquet`

## Key Design Decisions

### 1. Pandas First, Spark Later
**Decision**: Use pandas for the transform layer; migrate to Spark only when justified.

**Rationale**:
- Current dataset (~1-3 GB) fits comfortably in 32 GB RAM
- Faster iteration during development
- Richer ecosystem for financial analysis
- Pandas patterns translate well to Spark when migration is needed

**Migration trigger**: Dataset exceeds ~50 GB OR processing time exceeds ~1 hour.

### 2. Overwrite Strategy (No Versioning)
**Decision**: Always overwrite files in Object Storage on each ETL run.

**Rationale**:
- Source updates files in place with the same names
- Simpler architecture, no date-folder hierarchy to manage
- Latest data is always at a predictable path
- Storage cost optimization

**Rejected alternative**: Smart change detection (Hugging Face doesn't expose reliable metadata; full hash comparison defeats the purpose by requiring full download anyway).

### 3. Source-Specific Folder Structure
**Decision**: `raw_data/yahoo_finance_huggingface/` rather than flat `raw_data/`.

**Rationale**:
- Scalable for adding future sources (Bloomberg, Alpha Vantage, etc.)
- Clear data lineage in folder paths
- Different sources can have different update cadences

### 4. Cost-Optimized Instance Scheduling
**Decision**: Stop instance when not in use; auto-start before scheduled jobs.

**Implementation**: `infrastructure/compute/oracle_instance_scheduler.sh`

**Savings**: ~$25-30/month vs. always-on.

## Implementation Status

### ✅ Phase 0: Foundation (Complete)
- OCI account, compartment, and IAM setup
- Compute instance provisioned and configured
- Object Storage bucket created
- OCI CLI installed and configured
- Python 3.11+ environment

### ✅ Phase 1A: Ingestion (Complete)
**Script**: `etl/ingestion/yahoo_finance_huggingface_etl.py`

**Capabilities**:
- Downloads all 20 parquet files from Hugging Face
- Validates files (parquet integrity, row counts, sizes)
- Uploads to `oci://finance-raw/raw_data/yahoo_finance_huggingface/`
- Always overwrites (no skip logic)
- Retry with exponential backoff
- Comprehensive logging and reporting

**History**:
- Started with multiple iterations (`finish_etl.py`, `robust_restart.py`, `fixed_restart.py`)
- Hit memory bottleneck → upgraded instance to 32 GB
- Discovered `stock_shares_outstanding.parquet` was missing from file list, added manually
- Consolidated into single production script
- Did "clean slate" reorganization: deleted old date-based folders, repopulated with new structure

### 🔄 Phase 1B: Transform (In Progress)
**Scripts**:
- `etl/transform/financial_data_transformer.py` — Core framework
- `etl/transform/stock_analysis_pipeline.py` — Analysis workflows

**Implemented (untested)**:
- OCI client integration with caching
- Data loading from Object Storage
- Cleaning utilities (deduplication, outlier removal, type coercion)
- Technical indicators: SMA (5/20/50/200), daily returns, volatility, RSI, momentum
- Financial ratios: profitability (ROA/ROE/margin), leverage, liquidity
- Custom features: 52-week bands, volatility percentiles, gap detection
- Composite "health score" calculation

**TODO**:
- Test on real data
- Generate first curated datasets
- Data quality validation
- Performance benchmarking
- Unit tests

### 📋 Phase 2: Serving Layer (Planned)
- Oracle Autonomous Database setup
- Star/snowflake schema design
- Data loading procedures from curated zone
- REST API layer
- Query optimization

### 📋 Phase 3: Advanced Analytics (Future)
- Vector DB (MySQL HeatWave Vector) for earnings transcripts and news
- Sentiment analysis on transcripts/news
- Forecasting models
- Real-time streaming integration
- Dashboards (Oracle Analytics Cloud or custom)

## Transformations Catalog

### Technical Indicators (applied to `stock_prices`)
- Simple Moving Averages: 5, 20, 50, 200-day
- Daily returns (per-symbol pct_change)
- 30-day rolling volatility
- RSI-14 (Relative Strength Index)
- Price momentum: 1, 5, 20-day
- Volume SMA-20 and volume ratio
- 52-week high/low and price-vs-band ratios
- Volatility percentiles
- Gap detection (>2% open vs prior close)

### Financial Ratios (joins `stock_income` × `stock_balance_sheet`)
- **Profitability**: net profit margin, ROA, ROE, asset turnover
- **Leverage**: debt-to-assets, debt-to-equity
- **Liquidity**: current ratio
- **Composite**: 0-100 health score with categorical rating (Poor/Fair/Good/Excellent)

## Operations

### Manual ETL Run
```bash
python etl/ingestion/yahoo_finance_huggingface_etl.py \
  --compartment-id "$OCI_COMPARTMENT_ID" \
  --bucket-name finance-raw \
  --log-file "logs/etl_$(date +%Y%m%d).log" \
  --report-file "reports/etl_$(date +%Y%m%d).txt"
```

### Manual Transform Run
```bash
python etl/transform/stock_analysis_pipeline.py \
  --compartment-id "$OCI_COMPARTMENT_ID" \
  --analysis-type full
```

### Scheduled Operations (crontab on instance)
```bash
# Daily ETL at 2 AM, then auto-shutdown
0 2 * * * /home/opc/oracle-financial-lakehouse/infrastructure/compute/oracle_instance_scheduler.sh etl-and-stop
```

### Instance Management (from local machine)
```bash
# Start
oci compute instance action --action START --instance-id "$INSTANCE_OCID"

# Stop
oci compute instance action --action STOP --instance-id "$INSTANCE_OCID"

# Status
oci compute instance get --instance-id "$INSTANCE_OCID" --query 'data."lifecycle-state"'
```

⚠️ **Note**: Stopping the instance immediately terminates SSH connections. The instance must be restarted before SSH access is restored.

## Cost Profile

| Component | Monthly Cost |
|-----------|-------------|
| Compute (running) | $0 (always-free tier) |
| Boot volume storage | ~$5 |
| Object Storage | $0-5 (first 20 GB free) |
| Networking | Minimal |
| **Total** | **~$5-10/month** |

## Known Issues & Quirks

1. **`stock_shares_outstanding.parquet` was missing** from the original ETL file list — has been added manually but watch for similar omissions if Hugging Face dataset changes.
2. **Memory pressure on smaller instances** — original 24 GB instance hit memory bottlenecks; 32 GB resolved this for current dataset size.
3. **Public IP may change** when instance is stopped/started unless reserved.
4. **No automated tests yet** — high priority for Phase 1B completion.

## Common Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| SSH connection refused | Instance stopped | `oci compute instance action --action START` |
| OOM during ETL | Memory bottleneck | Verify 32 GB RAM, process files individually |
| OCI auth errors | Bad config | Check `~/.oci/config` and API key |
| Download fails | HF rate limiting / network | Retry logic should handle; check logs |

## References

- [OCI Object Storage docs](https://docs.oracle.com/en-us/iaas/Content/Object/home.htm)
- [OCI CLI reference](https://docs.oracle.com/en-us/iaas/tools/oci-cli/latest/oci_cli_docs/)
- [Hugging Face dataset](https://huggingface.co/datasets/bwzheng2010/yahoo-finance-data)
- [pandas docs](https://pandas.pydata.org/docs/)

---

**Last Updated**: April 26, 2026