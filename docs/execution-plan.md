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

- **Current phase:** Phase 9 — VPS Provisioning (Oracle Cloud Always Free)
- **Current stage / task:** Stage 09 — Create Oracle Cloud account + provision VPS
- **Phase 0 (Planning):** ✅ Complete
- **Phases 1–7 (Code → Quality → VCS → CI/CD → Docker → Registries → Compose):** ✅ Complete
- **Phase 8 (SSH & Remote Connections):** ✅ Complete — mental model, practice, Part C questions answered
- **Last completed item:** Session 07 (2026-10-21, documentation only) — the **v4 daily
  session model** was defined and written into `AGENTS.md`, the session instructions and
  this plan: 2 h standard / 2.5 h max / 45–60 min minimum, 5 days/week, review 3–5 concepts
  (cap 40 min) + one practical objective + documentation, weekly consolidation. It supersedes
  the daily 18/18 review; that full pass remains the one-time baseline from Session 06.
  Concepts 1–18 validated/accepted ✅: **Código fuente**, **Dependencias
  (`requirements.txt`)**, **Tests (`test_principal.py` + pytest)**, the **Calidad y
  seguridad gate (7 reviewers)**, **Ruff**, **Flake8**, **Black**, **MyPy**, **Bandit**,
  **pip-audit**, **Git/`.gitignore`**, **YAML/pipelines**, **push flow**,
  **Docker/Dockerfile**, **`.dockerignore`**, **registries**, **Compose/Watchtower** and
  **SSH/VPS**. Student's permanent insight: **the pipeline is born from the application**
  (code → stack → dependencies/tests/build → pipeline), documented in `AGENTS.md` +
  `delivery-story.md` v2.8. The canonical explanations for Concepts 2–18 are recorded in
  `AGENTS.md` and `docs/session-log.md`; reuse them in future reviews.
- **Daily session model:** **v4**. Concepts validated/accepted: **18 of 18** (Código
  fuente, Dependencias, Tests, Calidad y seguridad, Ruff, Flake8, Black, MyPy, Bandit,
  pip-audit, Git/`.gitignore`, YAML/pipelines, push flow, Docker/Dockerfile, `.dockerignore`,
  registries, Compose/Watchtower, SSH/VPS). **The review list is complete.** Next: **Block F
  formal evaluation** (registries), then Stage 09.
- **Next session target:** Block F formal evaluation → Stage 09 Session 1 (Oracle Cloud
  account, Always Free quotas, third key `id_ed25519_vps`, `~/.ssh/config` alias `mi-vps`).
  Stage 09 still has **zero** checkboxes marked.
- **✅ Repo state VERIFIED 2026-10-21** (real `git fetch` to both remotes):

  | Ref | SHA | Status |
  |---|---|---|
  | `develop` | `fe37aa7` | = `github/develop` = `gitlab/develop` ✅ |
  | `github/master` | `2fd2de9` | contains `fe37aa7` ✅, content identical |
  | `gitlab/master` | `8cce10c` | contains `fe37aa7` ✅, content identical |
  | `master` (local) | `1dc240a` | behind remotes; content identical ✅ |

  **All refs are content-identical** (`git diff` = 0 for every pair); `develop` is an ancestor
  of both remote `master` refs. The feature6/feature7 commits are merged into `develop` and
  pushed to both remotes; the local `feature6` branch is gone. At verification time the
  working tree was clean; since then the docs were synced and remain uncommitted.
  > **Remote rule (permanent):** a remote is unknown until you `git fetch` it; a remote-tracking
  > ref is Git's memory of the remote, not the remote. Never write a remote's state into the docs
  > from a tracking ref alone. GitLab's extra merge commits are normal mirror divergence: the only
  > valid parity check is `git diff` = 0, never "do the SHAs match".
- **✅ `nuevo.py` — resolved by student decision (2026-10-01):** deliberate local practice file,
  stays in the repo; `Dockerfile` uses `COPY Principal.py .`, so it never enters the image. See
  `AGENTS.md` Repo Hygiene Rules #1.
- **Housekeeping:** decide whether the `GHCR_USERNAME`/`GHCR_TOKEN` GitLab CI variables are
  dropped — ADR-0007 removed the need for a cross-platform PAT. Also: memory-folder
  `requirements.txt` still says `pytest==8.2.2` while the real repo uses `9.0.3`.
- **Blockers / open questions:** none technical. **Pending:** these memory updates are
  **synced to the `C:\Repo2` working tree but not committed/pushed** (student chose sync-only;
  commit/push requires explicit instruction). Pending decision: Block F evaluation first, or
  begin Stage 09 directly.
- **Last session:** 2026-10-21 — Session 07 documentation-only: v4 daily session model defined.
  No concepts reviewed, no stage work.
- **Last commit / push:** none from this session (sync-only). Last documented push: Session 05 memory
  commit `0b15177` (+ later docs commit `7b6643e`), then the student's feature6/feature7
  commits on `develop` (`fe37aa7`), merged and pushed to both remotes.

---

## General Status

| Item | State |
|---|---|
| Project | ☒ In progress |
| Plan | ☒ Defined |
| Zero-cost policy | ☒ Active (ADR-0005) |
| Version control | ☒ Active (GitHub + GitLab mirrored) |
| Application | ☒ Basic Python app + tests |
| Code quality | ☒ Active (Ruff, Flake8, Black, MyPy, Pytest) |
| CI/CD | ☒ Active (GitHub Actions + GitLab CI) |
| Docker | ☒ Active (images, compose, 3 registries) |
| CD simulation | ☒ Active (Watchtower) |
| SSH | ✅ Complete (Phase 8) |
| VPS | 🔄 Next (Phase 9) |

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
- [x] Understand why persistence will matter in Phase 12
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

## Phase 9 — VPS Provisioning (Oracle Cloud Always Free)

**Objective:** Create the first real server, deliberately — understanding each choice.

**Estimated duration:** 2–3 sessions

**Stage document:** [`docs/stages/stage-09-vps-provisioning.md`](docs/stages/stage-09-vps-provisioning.md)

**SSH key strategy (decided in Stage 08):** Create a **third separate key pair** (`id_ed25519_vps`) following the existing pattern of separate keys for GitHub and GitLab. See [`docs/stages/stage-08-ssh-remote-connection.md`](docs/stages/stage-08-ssh-remote-connection.md#ssh-key-strategy-for-phase-9-students-decision) for details.

- [ ] Create the Oracle Cloud account (free tier only — see ADR-0005)
- [ ] Understand quotas and how to avoid costs
- [ ] Create the VPS (instance)
  - [ ] Choose Ubuntu
  - [ ] Understand what an instance really is
  - [ ] Understand the shape/resources (ARM vs x86) and their limits
- [ ] Generate VPS key pair: `ssh-keygen -t ed25519 -C "vps-oracle@project"` → save to `~/.ssh/id_ed25519_vps`
- [ ] Add public key to Oracle Cloud console
- [ ] Add VPS entry to `~/.ssh/config`
- [ ] Connect for the first time with `ssh mi-vps`
- [ ] Basic first-contact: whoami, OS version, resources
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 10 — Linux Server Administration

**Objective:** Administer the VPS like a professional. Nothing is copy-paste.

**Estimated duration:** ~6–8 sessions

- [ ] First contact with the Linux CLI on the server
- [ ] Update/upgrade the system (understand what `apt` does)
- [ ] Users, groups, permissions (why they exist)
- [ ] Filesystem layout and navigation (FHS)
- [ ] Package management (apt) — install and justify tools
- [ ] Firewall (UFW) — only the needed ports open
- [ ] SSH hardening (keys only, no root login, no password login)
- [ ] Install Docker Engine (understand what is installed)
- [ ] Install Docker Compose plugin (understand the difference)
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 11 — Deployment to the Server

**Objective:** The pipeline delivers. First real deployment.

**Estimated duration:** 2–3 sessions

- [ ] `git clone` the project on the server
- [ ] Understand why we clone the compose file and not build on the server
- [ ] Configure environment variables on the server (`.env`)
- [ ] `docker compose up -d` — first run
- [ ] Watch the server pull the image from the registry and create containers
- [ ] Verify the application responds (curl)
- [ ] Restart behavior: reboot the server, app comes back (restart policies)
- [ ] Optional: CD job in the pipeline that SSHes and redeploys on push
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 12 — Production Hardening & Observability

**Objective:** Move from "it runs" to "it runs like production".

**Estimated duration:** ~6–8 sessions

- [ ] Nginx reverse proxy (understand why the app is not exposed directly)
- [ ] HTTPS with Let's Encrypt (why HTTPS is non-negotiable)
- [ ] Environment variables and secrets management
- [ ] Persistence: named volumes, bind mounts (understand ephemerality)
- [ ] Logs: container logs, Nginx logs, log rotation
- [ ] Backups: strategy + **test a restore**
- [ ] Monitoring: health checks, simple monitoring (e.g., Uptime Kuma or equivalent)
- [ ] Split pipeline into CI + CD (deploy on push with rollback basics)
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 13 — FastAPI Full Stack & Evolving the App

**Objective:** Turn the toy app into a real service with a database — the kind of app a DevOps engineer actually deploys.

**Estimated duration:** ~4–6 sessions

- [ ] Integrate FastAPI into the repository
- [ ] Add a health endpoint (for monitoring)
- [ ] PostgreSQL service (why the DB is separate, why it persists)
- [ ] Compose grows: app + database (+ optional Redis)
- [ ] Migrations and initialization
- [ ] Environment-based configuration (dev vs prod)
- [ ] Full pipeline: build → test → push → deploy the evolved app
- [ ] Document + evidence + update state

**Status:** ⬜ Pending

---

## Phase 14 — Final Portfolio & Interview Defense

**Objective:** Turn the work into a story you can defend in an interview.

**Estimated duration:** 2–3 sessions

- [ ] Final architecture diagram (user → Nginx → app → DB)
- [ ] Final README polish
- [ ] Walk through the repository as an interviewer would
- [ ] Rehearse "why" for every major decision (use the ADRs)
- [ ] Prepare answers for the most common DevOps Junior questions
- [ ] Record the final portfolio review

**Status:** ⬜ Pending

---

## Timeline (5 sessions/week, ~2 h each + weekly consolidation)

| Phase | When | Sessions |
|---|---|---|
| 0 Planning | 2026-08 (week 0) | 1 |
| 1 Application Dev | ✅ prior work | — |
| 2 Code Quality | ✅ prior work | — |
| 3 Version Control | ✅ prior work | — |
| 4 CI/CD Pipelines | ✅ prior work | — |
| 5 Containerization | ✅ prior work | — |
| 6 Registries | ✅ prior work | — |
| 7 Orchestration & CD Sim | ✅ prior work | — |
| 8 SSH & Remote Access | Weeks 1–2 | 1–2 |
| 9 VPS Provisioning | Week 1 | 2–3 |
| 10 Linux Administration | Weeks 1–2 | 6–8 |
| 11 Deployment to Server | Week 2 | 2–3 |
| 12 Production Hardening | Weeks 2–4 | 6–8 |
| 13 FastAPI Full Stack | Weeks 4–6 | 4–6 |
| 14 Portfolio & Interview | Weeks 6–7 | 2–3 |

> Total remaining ~ 25–35 sessions ~ 5–7 weeks at 5 sessions/week. Cadence may be adjusted;
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
