# Oracle Cloud Financial Data Lakehouse

A production-grade ETL pipeline and data lakehouse for financial market data analysis on Oracle Cloud Infrastructure (OCI). Built with Python and pandas, with planned migration paths to Spark and Oracle Autonomous Database.

**Status**: 🔄 Active Development — Phase 1B (Transform Layer)

## Architecture

```
Hugging Face Dataset
        ↓
[Ingestion] yahoo_finance_huggingface_etl.py
        ↓
OCI Object Storage: finance-raw/raw_data/yahoo_finance_huggingface/
        ↓
[Transform] financial_data_transformer.py
        ↓
OCI Object Storage: finance-raw/curated_data/
        ↓
[Future] Oracle Autonomous Database → Analytics/ML
```

## Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/oracle-financial-lakehouse.git
cd oracle-financial-lakehouse

# Install dependencies
pip install -r requirements.txt

# Configure environment
export OCI_COMPARTMENT_ID="ocid1.compartment.oc1..."
export OCI_BUCKET_NAME="finance-raw"

# Run ingestion
python etl/ingestion/yahoo_finance_huggingface_etl.py \
  --compartment-id "$OCI_COMPARTMENT_ID"

# Run transformation
python etl/transform/stock_analysis_pipeline.py \
  --compartment-id "$OCI_COMPARTMENT_ID" \
  --analysis-type full
```

## Project Structure

```
oracle-financial-lakehouse/
├── README.md                          # This file
├── PROJECT_CONTEXT.md                 # Detailed context for Claude Code
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git ignore rules
│
├── etl/
│   ├── ingestion/
│   │   └── yahoo_finance_huggingface_etl.py
│   └── transform/
│       ├── financial_data_transformer.py
│       └── stock_analysis_pipeline.py
│
├── infrastructure/
│   └── compute/
│       └── oracle_instance_scheduler.sh
│
├── docs/
│   └── initial_setup_history.md       # Terminal history (if added)
│
├── logs/                              # Generated at runtime (gitignored)
├── reports/                           # Generated at runtime (gitignored)
└── tests/
    ├── unit/
    └── integration/
```

## Data Sources

**Primary**: Yahoo Finance via Hugging Face (`bwzheng2010/yahoo-finance-data`)
- 20 parquet files
- ~1-3 GB total
- Updated periodically by source maintainer
- Strategy: Full overwrite on each ETL run

## Infrastructure

| Component | Specification |
|-----------|--------------|
| Compute | OCI VM.Standard.A1.Flex (4 OCPU, 32 GB RAM) |
| OS | Ubuntu 24.04 LTS |
| Storage | Oracle Object Storage (`finance-raw` bucket) |
| Cost | ~$5-10/month with auto-shutdown scheduling |

## Development Phases

- ✅ **Phase 0**: Infrastructure setup
- ✅ **Phase 1A**: Ingestion layer (all 20 files downloaded)
- 🔄 **Phase 1B**: Transform layer (in progress)
- 📋 **Phase 2**: Serving layer (Autonomous DB + API)
- 📋 **Phase 3**: Analytics & ML (vector DB, dashboards)

## Documentation

- [`PROJECT_CONTEXT.md`](./PROJECT_CONTEXT.md) — Full technical context, design decisions, and history
- [`CLAUDE_CODE_STARTER_PROMPT.md`](./CLAUDE_CODE_STARTER_PROMPT.md) — Initialization prompt for Claude Code sessions

## License

MIT

---

**Author**: DMay  
**Last Updated**: April 26, 2026