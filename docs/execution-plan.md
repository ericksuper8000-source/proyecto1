# EXECUTION PLAN

## Sequential Execution State & Checklists

**Project:** CI/CD Pipeline Labs
**Version:** 1.0 (2026 revision)
**Status:** In Progress

---

## How to Use This File

This is the **single source of truth** for project status. It does not contain theory or
stages — it tells you exactly where the project is and what to do next.

- **Every day starts with the v4 review block** (3–5 concepts, see `AGENTS.md` — Daily Work
  Session v4), then reads the **Current Status** block below.
- **Every session ends** by updating the **Current Status** block, ticking completed
  checkboxes, and syncing the memory folder with `C:\Repo2`.
- A phase or stage is only marked complete when it is **understood, documented, evidenced,
  and synchronized** (see Definition of Done in `AGENTS.md`). Commit/push only on request.
- Any AI agent joining the project reads this file first (see `AGENTS.md`).

---

## 📌 CURRENT STATUS

> **This block is updated at the end of every session.**

- **Route:** **v2.1** (2026-10-29, product-first) — phases renumbered per **ADR-0016**;
  **ADR-0015** defines the product (Deploy Journal). Full index: `docs/adr/README.md`.
  Phases 0–8 are unchanged.
- **Current phase:** Phase 9 — **Deploy Journal** (product + FastAPI + MySQL 8 +
  CI/CD v2). Stage: `docs/stages/stage-09-deploy-journal.md`.
- **Current stage / task:** Stage 09 — product defined (ADR-0015); next: **Session 1 —
  data model** (`environments`, `deployments`) + schema explanation. Zero checkboxes
  marked yet.
- **Last completed item:** 2026-10-29 — route v2.1 documentation (product-first,
  reordering, ADR-0015/0016). Previous work: Session 07 (2026-10-21).
- **Audit 2026-10-29 (technical rival review):** full review of `C:\Repo2` (HEAD
  `ec181df` at audit close) and this memory folder. Verdict: **4.5/10** as a junior
  portfolio today; **8.5/10** when the revised route is completed. Findings C1–C12 are
  embedded in this plan, in ADR-0008…0016 and in the Priority Action List below.
  **Documentation-only sessions:** no code changed.
- **Product (ADR-0015):** Deploy Journal — records every deployment (version,
  environment, status, message, author), public timeline, `/health` with DB check,
  writes protected by `X-API-Key`. Stack: Python + FastAPI + MySQL 8 + HTML page.
- **Pending student decisions (resolve and record in `session-log.md`):**
  1. **VPS provider** — Oracle Cloud Always Free (card required for verification, no
     charge) vs an already-owned Hetzner VPS (no incremental cost). Gate: **Stage 10
     Session 0** (ADR-0009).
  2. **GitLab mirror** — make public with curation (ADR-0014) or stop calling it a
     public mirror (today it is private).
  3. **Secret scopes/rotation** — Docker Hub PAT, GitLab token, journal API key,
     deploy key (ADR-0013/0015).
- **Environment:** memory `requirements.txt` = repo; `.dockerignore` normalized;
  memory folder and `C:\Repo2` docs in sync (2026-10-29).
- **Blockers / open questions:** none. Next session: read ADR-0016, then Stage 09
  Session 1 (data model from the product requirements).
- **Last session:** 2026-10-29 — Route v2.1 (product-first + Deploy Journal,
  documentation only).
- **Repo state (verified by fetch 2026-10-29):** `develop` = `ec181df` = `github/develop`
  = `gitlab/develop`; local `master` = `ee5983e` = `github/master`; `gitlab/master` =
  `d13e8c4` (SHA differs by GitLab merge commit; `git diff` = 0). `git diff develop
  master` = 0. Route v2.1 docs are synced to `C:\Repo2` and **pending commit** —
  commit/push only when the student asks.

---

## General Status

| Item | State |
|---|---|
| Project | ☒ In progress (route v2.1 — product-first) |
| Plan | ☒ Defined (execution-plan v2.1 + ADR-0001…0016) |
| Product | ☒ Defined — Deploy Journal (ADR-0015), implementation next |
| Zero-cost policy | ☒ Active (ADR-0005; free stack in ADR-0009/0011) |
| Version control | ☒ Active (GitHub + GitLab mirrored; GitLab private until ADR-0014 decision) |
| Application | 🔄 Next — Python toy app exists; Deploy Journal in Phase 9 |
| Code quality | ☒ Active (Ruff, Flake8, Black, MyPy, Pytest; pyproject + pinned dev-tools in Phase 9) |
| CI/CD | ☒ Active (CI/CD v2 rules in ADR-0013; PR gating + smoke test in Phase 9) |
| Docker | ☒ Active (images, compose, 3 registries; multi-arch in Phase 9, ADR-0010) |
| CD simulation | ☒ Active (Watchtower, local only) |
| SSH | ✅ Complete (Phase 8) |
| VPS + IaC | ⬜ Planned (Phase 10 — Terraform + cloud-init) |
| Observability | ⬜ Planned (Phase 14 — ADR-0011) |
| Backups | ⬜ Planned (Phase 13) |

---

## Phase 0 — Planning & Documentation Architecture

**Objective:** Fully define the project before continuing the technical work.

- [x] Define the general objective
- [x] Define the methodology
- [x] Define the project philosophy
- [x] Define the mentor role
- [x] Define the student role
- [x] Create the Project Specification
- [x] Create the Execution Plan
- [x] Create the Learning Roadmap
- [x] Define the documentation strategy
- [x] Define the repository structure
- [x] Decide to version from day one (see ADR-0001)
- [x] Decide to mirror GitHub + GitLab (see ADR-0002)
- [x] Decide multi-registry publishing (see ADR-0003)
- [x] Decide Docker Compose early + Watchtower for CD simulation (see ADR-0004)
- [x] Adopt the zero-cost principle (see ADR-0005)
- [x] Decide public documentation in English (see ADR-0006)
- [x] Define the daily recap & validation ritual

**Status:** ✅ COMPLETE

---

## Phase 1 — Application Development

**Objective:** Have a real application to deliver. Without software, there is no delivery pipeline.

**Estimated duration:** Completed (2–3 months, prior work)

- [x] Python fundamentals: variables, conditionals, loops, functions
- [x] Python: classes, exceptions, regex, files, modules, decorators, type hints
- [x] Create the first application (`Principal.py`)
- [x] Application runs locally without errors
- [x] Structure the code so tests can import it (`test_principal.py`)
- [x] Run the app and verify it behaves as expected

**Status:** ✅ COMPLETE

> ⚠️ The application is intentionally **small**. The project's focus is the delivery
> lifecycle. The app evolves into FastAPI in Phase 13.

---

## Phase 2 — Code Quality & Automated Testing

**Objective:** Guarantee the code is correct and consistent **before** it is published. A professional pipeline never ships broken code. Exhaustive flow coverage includes security and ignore-files.

**Estimated duration:** Completed (1 week, prior work) — exhaustive tooling (Bandit/pip-audit, .gitignore/.dockerignore/YAML) reinforced via spiral recaps from now on.

- [x] Ruff — fast linting
- [x] Flake8 — Python best practices
- [x] Black — automatic formatting
- [x] MyPy — static type checking
- [x] Pytest — unit tests
- [x] Tests written for the core functions (`suma`, `division`, `es_par`)
- [x] All quality tools pass locally before pushing
- [x] `.gitignore` / `.gitattributes` — understood (what never goes to Git)
- [x] **Bandit** (static security) — practiced 2026-09-29: `bandit -r . -x` local + `security` job in both pipelines
- [x] **pip-audit** (dependency vulnerabilities) — practiced 2026-09-29: `pip-audit -r requirements.txt` local + `security` job in both pipelines (found PYSEC-2026-1845 → pytest pinned to 9.0.3)
- [x] **`.dockerignore`** — added (2026-09-08) + explained vs `.gitignore` in Block E recaps

**Status:** ✅ COMPLETE — Bandit + pip-audit integrated into both CI pipelines (audit session 2026-09-29)

> ✅ Note: Both pipelines now run Flake8 + Black + Ruff + MyPy (lint), Pytest (test), and
> Bandit + pip-audit (security) before the `docker` job — the optional improvement recorded
> earlier is done. CI mastery (YAML deep) remains part of Block A/B recaps.

---

## Phase 3 — Version Control & Repositories

**Objective:** Version the project from day one on two platforms (multi-platform practice + redundancy).

**Estimated duration:** Completed (2 weeks, prior work)

- [x] Git basics: commits, branches, merge, push
- [x] GitHub repository created (`proyecto1`)
- [x] GitLab repository created (`repo2`)
- [x] Branch strategy: `master` (stable) + `develop` (integration)
- [x] Remotes configured on both platforms
- [x] Feature-branch practice exercised (multiple `feature*` branches merged)
- [x] Push to both remotes verified

**Status:** ✅ COMPLETE

---

## Phase 4 — CI/CD Pipelines

**Objective:** Automate validation and build. Stop doing manually what the pipeline should do.

**Estimated duration:** Completed (1–2 weeks, prior work)

- [x] Understand the difference between CI and CD
- [x] GitHub Actions workflow: `.github/workflows/ci.yml`
  - [x] Triggers: push on `develop`, pull request on `master`
  - [x] Job `lint`: Flake8 + Black + Ruff + MyPy (added 2026-09-29)
  - [x] Job `test`: Pytest
  - [x] Job `security`: Bandit + pip-audit (added 2026-09-29)
  - [x] Job `docker`: needs `lint` + `test` + `security`, builds and pushes the image with 8 char commit tag + `latest` to the 3 registries
- [x] GitLab CI pipeline: `.gitlab-ci.yml` — **validation-only since 2026-09-29 (ADR-0007)**
  - [x] Stages: `lint`, `test`, `security` (ruff/mypy + security job added 2026-09-29)
  - [x] No publish job: GitLab is the storage mirror; the single publisher is GitHub Actions
- [x] Secrets management (DOCKER_USERNAME, DOCKER_TOKEN, GITLAB_TOKEN, GITHUB_TOKEN — no cross-platform PAT needed after ADR-0007)
- [x] Pipelines run green on both platforms

**Status:** ✅ COMPLETE

> 💡 Future improvement (Phase 12): split into CI + CD stages so a green pipeline also
> deploys to the server.

---

## Phase 5 — Containerization

**Objective:** Guarantee the application runs identically anywhere. Enter Docker.

**Estimated duration:** Completed (1–2 weeks, prior work)

- [x] Understand why Docker exists (portability problem)
- [x] Write the `Dockerfile` (python:3.11-slim)
- [x] `docker build` produces an image
- [x] Understand images: layers, immutability, build context
- [x] Run the image locally and verify behavior
- [x] Understand images vs containers

**Status:** ✅ COMPLETE

---

## Phase 6 — Registries & Image Publishing

**Objective:** Give images a permanent home so any server can download them.

**Estimated duration:** Completed (1 week, prior work)

- [x] Understand why local images are not enough
- [x] Publish to **Docker Hub** (`erickdev8/mi-app:latest`)
- [x] Publish to **GHCR** (`ghcr.io/ericksuper8000-source/mi-app:latest`)
- [x] Publish to **GitLab Container Registry** (`registry.gitlab.com/ericksuper80-group/repo2:latest`)
- [x] Publish the **same image** to the three registries from a single pipeline
- [x] Registry authentication (tokens vs passwords; `--password-stdin`)
- [x] `docker pull` the image back from a registry

**Status:** ✅ COMPLETE

---

## Phase 7 — Orchestration & CD Simulation

**Objective:** Describe the desired running state with Docker Compose and simulate continuous deployment with Watchtower. Deepen exhaustive understanding of how each piece intervenes.

**Estimated duration:** Completed (1 week, prior work)

- [x] Understand Compose vs Engine (Compose decides, Engine executes)
- [x] Write `docker-compose.yml`
  - [x] Service `app` with `restart: always`
  - [x] Service `watchtower` with Docker socket access
  - [x] Watchtower poll interval configured (30 s)
- [x] Run the stack with `docker compose up`
- [x] Watchtower detects a new image and recreates the container (CD simulation)
- [x] Understand container lifecycle and restart policies
- [x] Understand why persistence will matter in Phase 13 (volumes for the DB)
- [x] Understand exhaustive flow `build → image → registry → compose → engine → watchtower` and failure modes
- [ ] **Kubernetes (conceptual)** — understand what it solves when Compose is not enough (multi-host, scheduler) — reference only, no install (see AGENTS.md Technology Introduction Rule)

**Status:** ✅ COMPLETE (core) — Kubernetes conceptual added to Block G/H spiral recaps

---

## Phase 8 — SSH & Remote Connections ✅

**Objective:** Understand what it means to connect to a remote machine. **No VPS is created yet.** Every later command must make sense, not be copy-paste.

**Estimated duration:** 1–2 sessions (completed in Session 02)

**Stage document:** [`docs/stages/stage-08-ssh-remote-connection.md`](docs/stages/stage-08-ssh-remote-connection.md)

- [x] Understand what SSH is and what problem it solves
- [x] Understand what really happens when you run `ssh usuario@servidor`
- [x] Understand how authentication works (keys: private/public)
- [x] Understand why a server normally has no graphical interface
- [x] Understand who you control and what you are controlling over SSH
- [x] (Practice only, no VPS) Generate a local key pair and inspect it
- [x] Answer the Stage 08 mentor questions in your own words
- [x] Document the stage + evidence + update state

**Status:** ✅ COMPLETE

---

## Phase 9 — Deploy Journal: Product + FastAPI + MySQL + CI/CD v2 (product-first)

**Objective:** Build the **product** first (ADR-0015) and let it define the stack,
dependencies, tooling and pipeline (ADR-0016): a small deployment-history service
(FastAPI + MySQL 8) with `/health`, tests, container and the upgraded CI/CD v2 gates.
**Nothing touches a server in this phase.**

**Estimated duration:** 6–8 sessions

**Stage document:** [`docs/stages/stage-09-deploy-journal.md`](docs/stages/stage-09-deploy-journal.md)

**Product (ADR-0015):** Deploy Journal — records every deployment (version,
environment, status, message, author) and exposes a public timeline + stats. The
pipeline writes to it; that closes the loop.

- [ ] **Session 1 — data model:** MySQL schema (`environments`, `deployments`) derived
      from the product requirements; init script; explain every column and index
- [ ] **Session 2 — API contract:** FastAPI with `GET /health` (checks DB),
      `GET/POST /api/deployments`, `GET /api/deployments/{id}`, `GET /api/stats`;
      Pydantic validation; `X-API-Key` on writes; `GET /` timeline page
- [ ] **Session 3 — tests:** unit tests (stats/logic) + API tests with `TestClient`;
      **MySQL service container in CI**; coverage ≥ 80 % on app code
- [ ] **Session 4 — stack & tooling derivation:** `requirements.txt` (runtime) vs
      `requirements-dev.txt` (pinned); `pyproject.toml` harmonizing Black 88 /
      Flake8 88 + E203,W503 / Ruff / MyPy; type hints
- [ ] **Session 5 — container & local stack:** Dockerfile v2 (non-root, HEALTHCHECK,
      EXPOSE 8000, pinned digest); compose with app + MySQL 8 (named volume,
      `.env.example`); `docker compose up` healthy locally
- [ ] **Session 6 — CI/CD v2 (ADR-0013):** docker job gated to push/tags; smoke-test
      job (run image + curl `/health`); pip cache, `permissions:`, `concurrency`,
      `timeout-minutes`; Trivy, Dependabot, gitleaks, pre-commit
- [ ] **Session 7 — multi-arch & publish:** buildx `linux/amd64,linux/arm64`;
      `docker manifest inspect`; push to the 3 registries from a tag
- [ ] **Session 8 — product demo evidence:** timeline page renders recorded
      deployments; screenshots/video of API + page
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 10 — VPS Provisioning with Terraform + cloud-init (sized from the product)

**Objective:** Create the first real server **from code** — now that the final stack
(Deploy Journal + MySQL + Nginx + monitoring, ADR-0015/0011) is known, size it correctly.
Manual console clicks are replaced by `terraform plan/apply` (ADR-0009).

**Estimated duration:** 3–4 sessions

**Stage document:** [`docs/stages/stage-10-vps-provisioning.md`](docs/stages/stage-10-vps-provisioning.md)

**Provider decision gate (Session 0, ADR-0009 + ADR-0005):**
- **Default:** Oracle Cloud Always Free (A1.Flex ARM, free forever). ⚠️ Oracle asks for a
  credit card for identity verification — **no charge**, but a card is required.
- **If a Hetzner VPS is already owned:** prefer it (no incremental cost, simpler
  Terraform provider). Record the decision in the session log.

**SSH key strategy (decided in Stage 08):** third separate key pair `id_ed25519_vps`.

- [ ] **Session 0 — decision gate:** read ADR-0009/0005; choose provider; install
      Terraform CLI; understand provider / state / resources / plan / apply / destroy
- [ ] **Session 1 — account & quotas:** create the cloud account (Always Free); verify
      what is free vs trial credits; configure a **budget alert** (free to set); record
      the live free-tier limits
- [ ] Generate VPS key pair `id_ed25519_vps`; add to `~/.ssh/config` as `mi-vps`
- [ ] **Session 2 — `infra/` module:** provider config, network (VCN/subnet, ingress
      22/80/443), instance (Ubuntu LTS, ARM A1 or x86 per provider), **cloud-init**
      (user, SSH key, disable password auth, unattended-upgrades), output public IP
- [ ] `terraform plan` → `terraform apply` → server Running
- [ ] **Session 3 — first contact (read-only):** `ssh mi-vps` → whoami, os-release,
      `free -h`, `nproc`, `df -h`, `ip a`; host-key prompt understood (Stage 08)
- [ ] Reproducibility drill: `terraform destroy` + `terraform apply` again (or a second
      workspace) to prove the server is code
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 11 — Linux Server Administration + Ansible (route v2)

**Objective:** Administer the VPS like a professional — with a **reproducible
bootstrap**: everything done manually first, then encoded once in an idempotent Ansible
playbook (ADR-0009).

**Estimated duration:** 5–7 sessions

**Stage document:** [`docs/stages/stage-11-linux-admin-ansible.md`](docs/stages/stage-11-linux-admin-ansible.md)

- [ ] First contact with the Linux CLI on the server (done in Phase 9, read-only)
- [ ] Update/upgrade the system; understand what `apt` does
- [ ] Users, groups, permissions (why they exist); filesystem tour (FHS: /etc, /var, /home)
- [ ] Firewall (UFW): only 22/80/443 open; fail2ban basics
- [ ] SSH hardening: keys only, no root login, no password login
- [ ] Install Docker Engine (official apt repo, not snap) + Compose plugin
- [ ] `ansible/` playbook (`site.yml`) that reproduces **all** the above from a fresh
      server; run it twice to prove idempotency
- [ ] Evidence: playbook run output + before/after server state
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 12 — Deployment: immutable tag, CD over SSH, rollback

**Objective:** The pipeline delivers to the server — with a verified artifact, a
post-deploy healthcheck, and a proven way back (ADR-0013).

**Estimated duration:** 2–3 sessions

**Stage document:** [`docs/stages/stage-12-deployment-cd-rollback.md`](docs/stages/stage-12-deployment-cd-rollback.md)

- [ ] Server clones the repo for the **compose file only** (never builds on the server)
- [ ] `.env` on the server (chmod 600); secrets never in Git
- [ ] Deploy with the **immutable SHA tag** (never `:latest` in prod); compose pins the tag
- [ ] CD job: SSH deploy with a **scoped deploy key** (read-only, limited to repo),
      `docker compose pull && up -d`, then curl `/health`; only from `develop`/tags
- [ ] **Rollback runbook + one practiced drill:** redeploy the previous tag, verify
      `/health`, record time to recover
- [ ] Reboot drill: server restarts → app + db come back (`restart: always`)
- [ ] curl the public IP → `/health` responds (HTTPS arrives in Phase 13)
- [ ] Evidence: deploy log, healthcheck output, rollback timings
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 13 — Production Hardening: Nginx, HTTPS, persistence, backups

**Objective:** Move from "it runs" to "it runs like production" — on the **final** app
(ADR-0008).

**Estimated duration:** 5–7 sessions

**Stage document:** [`docs/stages/stage-13-hardening-https-backups.md`](docs/stages/stage-13-hardening-https-backups.md)

- [ ] Nginx (or Caddy) reverse proxy: app bound to 127.0.0.1:8000; only 80/443 exposed
- [ ] Domain: **free** hostname via DuckDNS / sslip.io / nip.io (zero-cost rule) +
      Let's Encrypt certificate with auto-renewal; verify rating
- [ ] Persistence: named volumes for MySQL; container log rotation limits
      (`json-file` max-size/max-file)
- [ ] Secrets: `.env` chmod 600; document token scopes + rotation (ADR-0013)
- [ ] Backups: daily `mysqldump` (container/cron) + off-site copy to a **free** target
      (Cloudflare R2 free 10 GB / Google Drive 15 GB via rclone); **restore drill with
      evidence**
- [ ] Watchtower stays a local CD simulation only; production redeploys are
      pipeline-driven (ADR-0013)
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 14 — Observability & Alerting (ADR-0011)

**Objective:** Prove the system is watched: metrics, dashboards, and a real alert that
reaches the student's phone.

**Estimated duration:** 4–5 sessions

**Stage document:** [`docs/stages/stage-14-observability-alerting.md`](docs/stages/stage-14-observability-alerting.md)

- [ ] Uptime Kuma: checks on `/health` every 60 s; public status page
- [ ] cAdvisor + Prometheus + Alertmanager (containers, ARM images verified per ADR-0010)
- [ ] Grafana dashboards (node + containers) — versioned in `monitoring/`
- [ ] Alerts → **Telegram bot** (free API): app down, disk > 80 %, CPU > 90 %,
      container restart loop
- [ ] **Alert drill:** stop the app → alert arrives on the phone → evidence logged
- [ ] Log strategy documented (where to look for what); Loki deferred (ADR-0011)
- [ ] Dashboard + alert screenshots as portfolio evidence
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 15 — Portfolio & Interview (ADR-0014)

**Objective:** Turn the work into a public, curated, demo-able story a stranger can
understand in 5 minutes — and that the student can defend.

**Estimated duration:** 2–3 sessions

**Stage document:** [`docs/stages/stage-15-portfolio-packaging.md`](docs/stages/stage-15-portfolio-packaging.md)

- [ ] **Public README v2:** one-liner, mermaid architecture diagram, stack, quickstart,
      operations (deploy/rollback/backup/monitoring), demo link, CI badges
- [ ] `LICENSE` (MIT), `CHANGELOG.md`, git tags + GitHub Releases (semantic versions)
- [ ] **Curation (ADR-0014):** move internal AI docs out of the public repo; remove
      `nuevo.py`; rename repo to `ci-cd-pipeline-labs`; resolve the GitLab public/private
      decision
- [ ] Real evidence: screenshots/GIF/video (pipeline green, registries, `terraform
      plan`, HTTPS, dashboards, alert received, restore drill)
- [ ] Final architecture diagram + 5-minute walkthrough video
- [ ] Interview rehearsal: every ADR question + learning-roadmap competencies
- [ ] Optional stretch: k3s mini-lab (conceptual only per spec)
- [ ] Final portfolio review with the mentor (rival pass)

**Status:** ⬜ Pending

---

## Priority Action List (audit 2026-10-29)

The audit's 15 actions, mapped to their phase. Each closes one documented finding
(C1–C12) and has an acceptance criterion.

| # | Action | Phase (v2.1) | Acceptance criterion |
|---|---|---|---|
| 1 | Multi-arch builds (buildx amd64+arm64) | 9 | `docker manifest inspect` shows both platforms (C1) |
| 2 | Gate docker job to push/tags; `:latest` only from releases | 9 | A PR publishes nothing (C2) |
| 3 | `pyproject.toml` with Black/Flake8/Ruff/MyPy coherent (88) | 9 | All four green with the same config (C4) |
| 4 | `requirements-dev.txt` pinned + pip-audit | 9 | Reproducible CI; fails on new CVE (C5) |
| 5 | Deploy Journal API + `/health` + API tests + smoke test | 9 | CI runs the image and curls 200 (C3, C9) |
| 6 | Terraform + cloud-init for the VPS | 10 | `terraform apply` creates the server from zero |
| 7 | Ansible playbook (idempotent bootstrap) | 11 | Two consecutive runs change nothing |
| 8 | CD over SSH: immutable tag + healthcheck + rollback | 12 | Rollback to previous tag in < 1 min, drilled |
| 9 | Nginx + free domain + HTTPS (auto-renew) | 13 | `curl https://…` valid certificate |
| 10 | Backups + restore drill | 13 | DB restored on a clean environment, evidenced |
| 11 | Observability + Telegram alert drill | 14 | Killing the app triggers a phone alert |
| 12 | Trivy + Dependabot + gitleaks + pre-commit | 9 | PR with CVE/secret fails (C11) |
| 13 | Public README v2 + diagram + demo + LICENSE + tags | 15 | A stranger runs the project in 5 min (C6) |
| 14 | Curation: internal docs out of public repo; remove `nuevo.py`; rename repo | 15 | Public repo reads like a product (C8, C12) |
| 15 | Secrets scopes/rotation documented; memory↔repo drift closed | 9/12 | Repo is the single source of truth (C7, C11) |

---

## Timeline (route v2.1 — 5 sessions/week, ~2 h each + weekly consolidation)

| Phase | Topic (route v2.1) | Sessions |
|---|---|---|
| 0–8 | Planning → SSH (completed) | ✅ prior work |
| 9 | Deploy Journal: product + FastAPI + MySQL + CI/CD v2 | 6–8 |
| 10 | VPS Provisioning with Terraform + cloud-init | 3–4 |
| 11 | Linux administration + Ansible | 5–7 |
| 12 | Deployment: immutable tag, CD, rollback | 2–3 |
| 13 | Hardening: Nginx, HTTPS, backups | 5–7 |
| 14 | Observability & alerting | 4–5 |
| 15 | Portfolio & interview | 2–3 |

> Total remaining ~ 27–38 sessions ~ 6–8 weeks at 5 sessions/week. Cadence may be adjusted;
> understanding is the only fixed requirement. Do not compress by skipping review or
> documentation.

---

## Session Workflow — v4 (Review + Practice + Documentation)

**Standard day: 2 hours. Heavy infrastructure day: 2.5 hours maximum. Five days/week,
plus one 45–60 minute weekly consolidation.**

| Block | Standard | Heavy |
|---|---|---|
| Open + objective | 5 min | 5 min |
| Interactive review | 30 min (3–5 concepts, cap 40) | 35 min |
| Practical work | 70 min | 90 min |
| Documentation + close | 15 min | 20 min |

**Block 1 — interactive review (3–5 concepts):**

1. **No general journey summary.** Start with the first concept in the queue.
2. Queue priority: fragile yesterday → new yesterday → today's dependencies → one older
   concept from the rotation map.
3. For **each concept**, use the v3 cycle (`AGENTS.md`):
   - canonical explanation + concrete example + analogy
   - explicit connection to previous concepts
   - *"¿Todo claro o necesitas otra explicación? ¿Preguntas?"* → wait
   - one verification question (purpose + connection + failure mode); evaluate as
     **solid / partial / fragile**
   - partial → reinforce the gap and rephrase; fragile → re-teach with another analogy,
     add to tomorrow's queue
4. **Hard cap 40 minutes.** If a concept remains fragile, reduce today's practical scope;
   do not let review consume the whole session.
5. Log each concept in `session-log.md` (explanation, connection, question, answer, verdict).

**Block 2 — practical work (one objective):**

6. Choose **one** unchecked item from the active stage and state the objective, why, expected
   evidence and safe stopping point (5 min).
7. The student executes; the mentor guides with questions/hints. No full solutions.
8. If blocked >10–15 min: hint; if still blocked: document and close at a safe point.
9. Evidence: command + output, screenshot, or diff. No evidence = not done.

**Block 3 — documentation & close:**

10. Fill the stage report and save evidence in `screenshots/stage-NN/`.
11. Append a session-log entry with: concepts reviewed + verdicts, what was done, what was
    learned, what was confusing, commands/decisions, and tomorrow's review queue (3–5).
12. Tick checkboxes, update **Current Status**, write an ADR if a real decision was made.
13. Sync memory folder ↔ `C:\Repo2`. **Commit/push only if the student explicitly asks.**
14. Close with one thing the student can explain and one doubt; unresolved items go first
    tomorrow. Define the exact next objective.

---

## Related Documents

- [`AGENTS.md`](../AGENTS.md) — AI operating manual & Definition of Done
- [`project-specification.md`](project-specification.md) — vision and scope
- [`mentor-constitution.md`](mentor-constitution.md) — mentoring principles
- [`learning-roadmap.md`](learning-roadmap.md) — competency map
- [`session-log.md`](session-log.md) — daily diary
- [`environment.md`](environment.md) — local environment preparation
