# Oracle Financial Data Lakehouse

A learning-focused, production-grade ETL pipeline for financial market data analysis built on Oracle Cloud Infrastructure. Goals: practical data lakehouse + skill development in data engineering, cloud, and financial analysis.

## Current Phase: 1B — Transform Layer (Not Started)

- Phase 0 (Foundation) and Phase 1A (Ingestion) are complete
- Transform scripts are planned but not yet written
- No automated tests yet

### Roadmap
- **Phase 2**: Serving layer — Oracle Autonomous Database, star/snowflake schema, REST API
- **Phase 3**: Advanced analytics — vector DB for transcripts, sentiment analysis, forecasting, dashboards

## Three-Environment Workflow

1. **Local** (this machine) — development, editing, testing
2. **GitHub** (`mayjordata/oracle-financial-lakehouse`) — source of truth
3. **OCI Compute Instance** (`finance-etl`) — production runtime, has OCI credentials, runs scheduled jobs

**Flow:** edit locally -> push to GitHub -> pull on instance -> run there

## OCI Infrastructure

- **Instance:** `finance-etl` (VM.Standard.E4.Flex, 2 OCPUs, 32 GB RAM, Oracle Linux 9 x86_64)
  - OCID: `ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q`
  - SSH: `ssh finance-etl` (key: `~/.ssh/oci_vm_key`, user: `opc`)
  - Public IP: 129.146.243.189 (may change on start/stop)
  - Python 3.9 (system), Git 2.47
  - **`~/oracle-financial-lakehouse/`** — git-tracked repo clone (use this)
  - **`~/finance-etl/`** — legacy pre-git directory (reference only)
- **Object Storage Bucket:** `finance-raw`
  - `raw_data/yahoo_finance_huggingface/` — 15 parquet files (current), 18 previously
  - `curated_data/` — transform outputs (empty, not yet populated)
- **Region:** us-phoenix-1 (PHX)
- **Finance Compartment:** `ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq`
- **Tenancy (root):** `ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta`
- **Auth:** `~/.oci/config` (DEFAULT profile, API key). Future: instance principal.

## Data Source

**Yahoo Finance via Hugging Face** — mirror: `bwzheng2010/yahoo-finance-data`, original: `defeatbeta/yahoo-finance-data` (~3.22 GB total, 15 parquet files, last updated 2026-04-17)

| Category | Files |
|----------|-------|
| Price & Market | `stock_prices`, `daily_treasury_yield`, `exchange_rate` |
| Fundamentals | `stock_statement`, `stock_profile`, `stock_officers` |
| Earnings | `stock_earning_calendar`, `stock_earning_call_transcripts`, `stock_tailing_eps` |
| Market Activity | `stock_dividend_events`, `stock_split_events`, `stock_news`, `stock_shares_outstanding` |
| Filings & Analysis | `stock_sec_filing`, `stock_revenue_breakdown` |

All filenames are `.parquet`. Source updates files in place with same names. **Note:** maintainer makes silent breaking changes with no changelog — audit periodically against live dataset. Removed 2026-04-27: `stock_summary`, `stock_historical_eps`, `stock_earning_estimates`, `stock_revenue_estimates`. Added: `stock_sec_filing`.

## Key Design Decisions

1. **Pandas first, Spark later** — dataset fits in 32 GB RAM. Migrate when >50 GB or processing >1 hour.
2. **Overwrite strategy** — always overwrite in Object Storage (no versioning). Source updates in place; smart change detection rejected (HF lacks reliable metadata).
3. **Source-specific folders** — `raw_data/yahoo_finance_huggingface/` to support future sources (Bloomberg, Alpha Vantage, etc.).

## Project Structure

```
etl/
  ingestion/     — download from Hugging Face, upload to OCI
  transform/     — pandas-based cleaning, indicators, ratios (not yet built)
  config/        — shared configuration
infrastructure/
  compute/       — instance scheduler, deployment scripts
  terraform/     — IaC (future)
tests/
  unit/          — unit tests
  integration/   — integration tests (needs OCI access)
notebooks/       — exploratory analysis
logs/            — ETL run logs (gitignored)
reports/         — ETL execution reports (gitignored)
docs/            — project documentation
```

## Conventions

- Python with pandas, pyarrow, oci SDK
- OCI CLI for infrastructure management (`oci compute`, `oci os`)
- Compartment-scoped queries: use finance-project compartment for this project's resources
- Logs go to `logs/`, reports to `reports/` — both gitignored
- Credentials live in `~/.oci/config` (DEFAULT profile) — never committed
- Edit locally, run ETL on instance. Unit tests can run locally.

## Cost Profile

| Component | Monthly Cost |
|-----------|-------------|
| Compute | ~$0 (E4.Flex is paid but stopped most of the time) |
| Boot volume | ~$5 |
| Object Storage | $0-5 (first 20 GB free) |
| **Total** | **~$5-10/month** |

## Known Issues

1. `stock_shares_outstanding.parquet` was originally omitted from the ETL file list — manually added, watch for similar omissions if HF dataset changes.
2. Instance hit OOM at 24 GB RAM — upgraded to 32 GB. Process files individually if issues recur.
3. Public IP may change on instance stop/start unless reserved.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| SSH refused | Instance is stopped — start it |
| OOM during ETL | Verify 32 GB RAM, process files individually |
| OCI auth errors | Check `~/.oci/config` and API key |
| Download fails | Retry logic handles HF rate limiting; check logs |

## Do NOT modify without explicit request

- `~/.oci/config` (credentials)
- `.gitignore` (only with care)
