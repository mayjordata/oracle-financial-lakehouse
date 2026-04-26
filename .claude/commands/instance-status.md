Check the status of the finance-etl compute instance.

## Instructions

1. Get live instance status:
```bash
oci compute instance get \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q \
  --query 'data.{"name":"display-name", "state":"lifecycle-state", "shape":"shape", "time-created":"time-created"}' \
  --output table
```

2. If RUNNING, get the current public IP:
```bash
oci compute vnic-attachment list \
  --compartment-id ocid1.compartment.oc1..aaaaaaaaud24osjofbgmzfkupno2rj5xsrsdn7kl5gdvz6kssrzmnaoraefq \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q \
  --query 'data[0]."vnic-id"' --raw-output
```
Then:
```bash
oci network vnic get --vnic-id <VNIC_ID> --query 'data."public-ip"' --raw-output
```

3. Report: instance name, state, shape (2 OCPUs / 32 GB), and public IP if running.
4. If the public IP differs from 129.146.243.189 (documented in CLAUDE.md), flag it.
