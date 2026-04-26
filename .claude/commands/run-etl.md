Run the ETL pipeline on the finance-etl instance.

**Argument:** `$ARGUMENTS` — optional: `ingestion`, `transform`, or `full` (default: `full`).

## Instructions

1. Check instance status:
```bash
oci compute instance get \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q \
  --query 'data."lifecycle-state"' --raw-output
```
If STOPPED, offer to start it first.

2. Based on the argument:

### Ingestion (or full)
```bash
ssh finance-etl "cd ~/oracle-financial-lakehouse && python etl/ingestion/yahoo_finance_huggingface_etl.py \
  --compartment-id \$OCI_COMPARTMENT_ID \
  --bucket-name finance-raw \
  --log-file logs/etl_\$(date +%Y%m%d).log \
  --report-file reports/etl_\$(date +%Y%m%d).txt"
```

### Transform (or full, after ingestion)
```bash
ssh finance-etl "cd ~/oracle-financial-lakehouse && python etl/transform/stock_analysis_pipeline.py \
  --compartment-id \$OCI_COMPARTMENT_ID \
  --analysis-type full"
```

3. Monitor output and report results. If errors occur, check the log files:
```bash
ssh finance-etl "tail -50 ~/oracle-financial-lakehouse/logs/etl_\$(date +%Y%m%d).log"
```
