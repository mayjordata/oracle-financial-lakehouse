Start the finance-etl compute instance.

## Instructions

1. Start the instance:
```bash
oci compute instance action --action START \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q
```

2. Wait briefly, then check status:
```bash
oci compute instance get \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q \
  --query 'data."lifecycle-state"' --raw-output
```

3. Once running, get the current public IP:
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

4. Report the state and public IP. If IP changed from 129.146.243.189, note that `~/.ssh/config` and CLAUDE.md may need updating.
