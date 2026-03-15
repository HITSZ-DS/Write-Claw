# Write-Claw

This folder is a sanitized, GitHub-ready export of the runtime code only.

It intentionally includes:
- Core agent/runtime source: `agents/`, `rag/`, `utils/`, `workflow/`
- Web app source: `local_web_portal/app/`
- Runtime entry files: `main.py`, `config.py`, `capability_registry.py`
- Dependency and startup files: `requirements.txt`, `local_web_portal/requirements.txt`, `local_web_portal/start_local.ps1`, `local_web_portal/.env.example`
- Optional deployment helpers: `local_web_portal/Dockerfile`, `local_web_portal/docker-compose.yml`

It intentionally excludes:
- Any previous `.git` history
- Local database files
- Runtime logs and generated runs
- Vector store data
- Session secrets and encryption keys
- Local virtual environments and caches

## Quick Start

```powershell
cd Write-Claw
.\local_web_portal\start_local.ps1
```

Then open:

```text
http://127.0.0.1:8010
```

## Before First Run

Copy the environment template and fill in your own values:

```powershell
Copy-Item local_web_portal\.env.example local_web_portal\.env
```

Do not commit `local_web_portal\.env`.

## Safe Upload Flow

Inside this folder:

```powershell
git init
git branch -M main
git add .
git commit -m "Initial clean export"
git remote add origin https://github.com/HITSZ-DS/Write-Claw.git
git push -u origin main
```

## Notes

- The `.gitignore` in this folder is stricter than the source workspace on purpose.
- Runtime data will be created locally under ignored paths such as `runs/`, `vector_db/`, and `local_web_portal/data/`.
- If you want, you can upload this folder directly, not the original workspace root.
