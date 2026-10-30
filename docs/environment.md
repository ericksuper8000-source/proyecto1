# ENVIRONMENT — Local Development Setup

**Phase:** Phase 0 — Planning (environment reference)
**Objective:** Document the local environment where the project lives, so every stage can
assume a verified baseline instead of unknown state.

**Last verified:** 2026-10-29 (audit + route v2.1, documentation-only) — docs updated to
route v2.1 (ADR-0015/0016) and synced between this folder and `C:\Repo2`. **No commit
made yet** for the v2.1 docs (sync-only rule).
✅ Drift fixed this day: memory `requirements.txt` now matches the repo
(`pytest==9.0.3`); `.dockerignore` normalized to the repo version.
✅ Repo state: route v2 docs committed as `ec181df` on `develop` (pushed to both remotes);
`master` `ee5983e` (github) / `d13e8c4` (gitlab, content-identical). Route v2.1 docs are
in the working tree, **uncommitted**.
⚠️ `nuevo.py` stays until Phase 15, where ADR-0014 removes it from the public repo.
⚠️ The GitLab repo is currently **private** — ADR-0014 pending decision (make public and
curated, or stop calling it a public mirror).

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
| Python 3.11 quality toolchain | flake8, black, ruff, mypy, bandit, pip-audit, pytest 9.0.3 (mirrors the CI jobs) |
| Docker Desktop | Docker Engine + Compose + BuildKit on Windows |
| Git Bash | Git CLI and command convenience |
| Terraform CLI (planned, Phase 10) | Provision the VPS from code — free (ADR-0009) |
| Ansible (planned, Phase 11) | Reproducible server bootstrap — free (ADR-0009) |
| Docker Buildx + QEMU (planned, Phase 9) | Multi-arch images amd64+arm64 — free (ADR-0010) |
| Trivy / gitleaks / pre-commit (planned, Phase 9) | Image CVE scan / secret scan / local gate — free (ADR-0013) |

> Verify with: `git --version`, `python --version`, `docker --version`,
> `docker compose version`.

## Repositories & Folders

| Path | Role |
|---|---|
| `C:\Repo2` | **The real repository** — code + pipelines + all project files. Lives here. |
| `E:\Datos\IA\CICD - Project` | **Memory/planning folder** — documentation, session log, execution plan. Kept in sync with `C:\Repo2`. (Historically `C:\Users\XPC\Desktop\CICD - Project` — moved to `E:\Datos\IA\` on 2026-09-08) |
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
| MySQL 8 (planned) | official image, multi-arch (ADR-0012) | Database |
| DuckDNS / sslip.io / nip.io (planned) | free hostname (ADR-0005) | HTTPS in Phase 13 |
| Telegram Bot API (planned) | free alert channel (ADR-0011) | Alerts in Phase 14 |
| Cloudflare R2 / Google Drive (planned) | free off-site backup target (ADR-0005) | Backups in Phase 13 |

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
