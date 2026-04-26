Stop the finance-etl compute instance.

## Instructions

1. Confirm with the user before stopping (unless they explicitly said to stop it).

2. Stop the instance:
```bash
oci compute instance action --action SOFTSTOP \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q
```

3. Check status:
```bash
oci compute instance get \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q \
  --query 'data."lifecycle-state"' --raw-output
```

4. Report the result. Remind that SSH connections will be terminated and the public IP may change on next start.
