# Oracle Financial Data Lakehouse

ETL pipeline pulling Yahoo Finance parquet data from Hugging Face into OCI Object Storage, with pandas-based transforms and eventual serving via Oracle Autonomous Database.

## Current Phase: 1B — Transform Layer Development

- Phase 0 (Foundation) and Phase 1A (Ingestion) are complete
- Transform code is written but untested
- No automated tests yet — high priority

## Three-Environment Workflow

1. **Local** (this machine) — development, editing, testing
2. **GitHub** — version control source of truth
3. **OCI Compute Instance** (`finance-etl`) — production runtime, has OCI credentials, runs scheduled jobs

**Flow:** edit locally -> push to GitHub -> pull on instance -> run there

## OCI Infrastructure

- **Instance:** `finance-etl` (VM.Standard.E4.Flex, 2 OCPUs, 32 GB RAM, Oracle Linux)
  - OCID: `ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q`
  - SSH: `ssh finance-etl` (key: `~/.ssh/oci_vm_key`, user: `opc`)
  - Public IP: 129.146.243.189 (may change on start/stop)
- **Object Storage Bucket:** `finance-raw`
  - `raw_data/yahoo_finance_huggingface/` — 20 parquet files
  - `curated_data/` — transform outputs
- **Region:** us-phoenix-1 (PHX)
- **Finance Compartment:** `ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq`
- **Tenancy (root):** `ocid1.tenancy.oc1..aaaaaaaaf5nxubxxw76fcootogezoobou3t5zwmrgoca4ou74lglhwuya7ta`

## Key Design Decisions

1. **Pandas first, Spark later** — dataset (~1-3 GB) fits in 32 GB RAM. Migrate when >50 GB or processing >1 hour.
2. **Overwrite strategy** — always overwrite files in Object Storage (no versioning). Source updates in place.
3. **Source-specific folders** — `raw_data/yahoo_finance_huggingface/` to support future data sources.

## Project Structure

```
etl/
  ingestion/     — download from Hugging Face, upload to OCI
  transform/     — pandas-based cleaning, indicators, ratios
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

- Python 3.11+ with pandas, pyarrow, oci SDK
- OCI CLI for infrastructure management (`oci compute`, `oci os`)
- Compartment-scoped queries: use finance-project compartment for this project's resources
- Logs go to `logs/`, reports to `reports/` — both gitignored
- Credentials live in `~/.oci/config` (DEFAULT profile) — never committed

## Common Operations

```bash
# Instance management
oci compute instance action --action START --instance-id $INSTANCE_OCID
oci compute instance action --action SOFTSTOP --instance-id $INSTANCE_OCID
oci compute instance get --instance-id $INSTANCE_OCID --query 'data."lifecycle-state"'

# Object Storage
oci os object list --bucket-name finance-raw --prefix raw_data/ --query 'data[].name'
oci os object get --bucket-name finance-raw --name <path> --file <local-path>

# ETL (run on instance)
python etl/ingestion/yahoo_finance_huggingface_etl.py \
  --compartment-id "$OCI_COMPARTMENT_ID" \
  --bucket-name finance-raw
```

## Do NOT modify without explicit request

- `~/.oci/config` (credentials)
- `.gitignore` (only with care)
- `CLAUDE_CODE_STARTER_PROMPT.md` (legacy starter prompt)
