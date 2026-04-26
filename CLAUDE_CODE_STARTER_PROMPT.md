# Claude Code Starter Prompt

Use the prompt below when starting a new Claude Code session in this project directory. It gives Claude Code immediate context so you don't have to re-explain the project each time.

---

## Recommended Starter Prompt

```
I'm working on the Oracle Cloud Financial Data Lakehouse project.

Before doing anything else, please read these files for full context:
1. README.md - Project overview
2. PROJECT_CONTEXT.md - Detailed technical context, design decisions, and current status
3. docs/initial_setup_history.md - Terminal history from initial setup (if present)

Quick summary:
- ETL pipeline pulling 20 Yahoo Finance parquet files from Hugging Face into OCI Object Storage
- Currently in Phase 1B: pandas-based transform layer development
- Three environments to keep in sync: local (here), GitHub, OCI compute instance
- All ingestion code is complete; transform code is written but untested

After reading the context files, please confirm you understand:
- The three-environment workflow (local → GitHub → OCI instance)
- The current phase and what's done vs. in progress
- The design decision to use pandas before Spark
- The overwrite strategy for raw data

Then I'll tell you what I want to work on today.
```

---

## Tips for Working with Claude Code on This Project

### Before making changes
- Always have Claude Code read `PROJECT_CONTEXT.md` first
- Be explicit about which environment you're working in (local vs. instance)
- Mention if changes need to be deployed to the instance afterward

### When committing code
- Have Claude Code suggest commit messages based on the changes
- Keep commits focused (one logical change per commit)
- Push to GitHub immediately so the instance can pull the latest

### When troubleshooting
- Share the exact error message
- Indicate whether the error happened locally or on the instance
- Include relevant log file contents from `logs/`

### When adding new features
- Update `PROJECT_CONTEXT.md` to reflect new decisions
- Add tests under `tests/` (this is a Phase 1B priority)
- Document new transformations in the "Transformations Catalog" section

### Files Claude Code should NOT modify without explicit request
- `~/.oci/config` (credentials)
- `.gitignore` (only with care)
- This file (`CLAUDE_CODE_STARTER_PROMPT.md`)

## Common Tasks Cheat Sheet

| Task | Where to do it |
|------|---------------|
| Edit Python code | Local |
| Run unit tests | Local |
| Run full ETL | OCI instance (has credentials + Object Storage access) |
| Manage cron jobs | OCI instance |
| Update infrastructure scripts | Local → push → pull on instance |
| Check ETL logs | OCI instance (`logs/` directory) |