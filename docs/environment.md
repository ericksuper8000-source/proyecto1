# ENVIRONMENT — Local Development Setup

**Phase:** Phase 0 — Planning (environment reference)
**Objective:** Document the local environment where the project lives, so every stage can
assume a verified baseline instead of unknown state.

**Last verified:** 2026-08-04

---

## Host Machine

- **OS:** Windows (10/11) — `C:\Users\XPC`
- **Shell (Git):** Git Bash (also used for Git operations)
- **Terminal:** VS Code integrated terminal / PowerShell / Git Bash

## Tools Installed

| Tool | Purpose in this project |
|---|---|
| Visual Studio Code | Main editor |
| Git | Version control |
| Python 3.11 | The application runtime |
| Docker Desktop | Docker Engine + Compose + BuildKit on Windows |
| Git Bash | Git CLI and command convenience |

> Verify with: `git --version`, `python --version`, `docker --version`,
> `docker compose version`.

## Repositories & Folders

| Path | Role |
|---|---|
| `C:\Repo2` | **The real repository** — code + pipelines + all project files. Lives here. |
| `C:\Users\XPC\Desktop\CICD - Project` | **Memory/planning folder** — documentation, session log, execution plan. Kept in sync with `C:\Repo2`. |
| `C:\Users\XPC\Desktop\Linux VPS -BORRADOR` | Reference project (Linux DevOps Labs) — structure inspiration only. |
| `C:\Users\XPC\Desktop\Portafolio` | Personal portfolio materials. |

## The Real Repository (C:\Repo2)

Current key files:

```
C:\Repo2\
├── .github/workflows/ci.yml   # GitHub Actions pipeline
├── .gitattributes             # Line-ending policy (LF normalization)
├── .gitlab-ci.yml             # GitLab CI pipeline
├── Dockerfile                 # Image definition
├── docker-compose.yml         # Stack: app + watchtower
├── Principal.py               # The application
├── nuevo.py                   # Scratch/learning file
├── test_principal.py          # Unit tests
├── requirements.txt           # Python dependencies
├── README.md                  # Existing public README
└── .git/
```

Branches: `master` (stable) and `develop` (integration).
Remotes: `github` (https://github.com/ericksuper8000-source/proyecto1.git) and
`gitlab` (git@gitlab.com:ericksuper80-group/repo2.git).

## External Services (free tier)

| Service | Account / resource | Purpose |
|---|---|---|
| GitHub | `ericksuper8000-source` / repo `proyecto1` | Hosting + Actions |
| GitLab | `ericksuper80-group` / repo `repo2` | Hosting + CI |
| Docker Hub | `erickdev8` / image `mi-app` | Registry 1 |
| GHCR | `ghcr.io/ericksuper8000-source/mi-app` | Registry 2 |
| GitLab Container Registry | `registry.gitlab.com/ericksuper80-group/repo2` | Registry 3 |
| Oracle Cloud (planned) | Free Tier (Phase 9) | VPS |

## Sync Rule

- **Real work and commits** happen in `C:\Repo2`.
- **Planning and AI memory** live in the Desktop folder `CICD - Project`.
- At the end of every session, the memory folder and `C:\Repo2` must show the **same**
  documentation state (the docs are copied into `C:\Repo2\docs/` and committed).

---

## Assumptions Being Eliminated

By the end of this setup, the following are **not assumed** — they are verified facts:

- The user can run Python, Git, and Docker locally.
- GitHub and GitLab pipelines run green.
- Images are published to the three registries.
- The memory folder structure matches the real repository structure.

## Definition of Done (Phase 0 environment)

- [x] Tools verified (Git, Python, Docker Desktop).
- [x] Both remotes configured and working.
- [x] Both pipelines green on `develop`.
- [x] Images visible in the three registries.
- [x] Memory folder created and synced with `C:\Repo2`.
