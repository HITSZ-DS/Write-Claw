# Minimal GitHub Whitelist

This repository is exported with a whitelist-first rule.

Keep on GitHub:

- `agents/`
- `integrations/`
- `local_web_portal/`
- `png/`
- `rag/`
- `release/`
- `utils/`
- `workflow/`
- `README.md`
- `.gitignore`
- `capability_registry.py`
- `config.py`
- `main.py`
- `requirements.txt`

Do not keep on GitHub:

- `runs/`
- `vector_db/`
- `local_web_portal/data/`
- `local_web_portal/runs/`
- `.env`
- `local_web_portal/.env`
- `__pycache__/`
- `*.db`
- `*.sqlite*`
- generated logs, temp files, and local secrets

Notes:

- `local_web_portal/data/` is recreated automatically at runtime.
- `runs/`, `vector_db/`, and `local_web_portal/runs/` are runtime output only.
- The export should stay source-only and not include local state.
