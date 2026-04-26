Deploy latest code to the finance-etl instance.

**Argument:** `$ARGUMENTS` — optional: `--start` to auto-start the instance if stopped.

## Instructions

1. Check if there are uncommitted local changes:
```bash
git status --porcelain
```
If there are changes, ask the user if they want to commit first.

2. Check if local is ahead of remote:
```bash
git log origin/main..HEAD --oneline 2>/dev/null
```
If ahead, remind user to push first.

3. Check instance status:
```bash
oci compute instance get \
  --instance-id ocid1.instance.oc1.phx.anyhqljthhgov4icemyj2bqyxhlpspcfj3zri725rckwo5wiehbcndcmfa4q \
  --query 'data."lifecycle-state"' --raw-output
```

4. If STOPPED and `--start` was passed, start it (use the start-instance flow). If STOPPED without `--start`, tell the user.

5. If RUNNING, SSH in and pull latest:
```bash
ssh finance-etl "cd ~/oracle-financial-lakehouse && git pull origin main"
```

6. Optionally install any new dependencies:
```bash
ssh finance-etl "cd ~/oracle-financial-lakehouse && pip install -r requirements.txt"
```

7. Report success and what was deployed (show the git log of what changed on the instance).
