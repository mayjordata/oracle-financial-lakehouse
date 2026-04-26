Check the contents of the finance-raw Object Storage bucket.

**Argument:** `$ARGUMENTS` — optional prefix to filter (e.g., `raw_data/`, `curated_data/`). Defaults to listing everything.

## Instructions

1. List objects in the bucket:
```bash
oci os object list \
  --bucket-name finance-raw \
  --prefix "$ARGUMENTS" \
  --query 'data[].{"name":name, "size":"size", "modified":"time-modified"}' \
  --output table
```

If no argument provided, list the top-level structure:
```bash
oci os object list \
  --bucket-name finance-raw \
  --delimiter "/" \
  --query '{prefixes: prefixes, "object-count": length(data)}'
```

2. Present a clean summary: file count, total size, and last modified date.
3. For `raw_data/yahoo_finance_huggingface/`, verify all 20 expected parquet files are present.
