# EXECUTION PLAN

## Sequential Execution State & Checklists

**Project:** CI/CD Pipeline Labs
**Version:** 1.0 (2026 revision)
**Status:** In Progress

---

## How to Use This File

This is the **single source of truth** for project status. It does not contain theory or
stages — it tells you exactly where the project is and what to do next.

- **Every day starts with the recap mini-session** (see `AGENTS.md` — Daily Recap &
  Validation), then reads the **Current Status** block below.
- **Every session ends** by updating the **Current Status** block and ticking every
  checkbox completed during that session.
- A phase or stage is only marked complete when it is **understood, documented,
  evidenced, committed, and pushed** (see Definition of Done in `AGENTS.md`).
- Any AI agent joining the project reads this file first (see `AGENTS.md`).

---

## 📌 CURRENT STATUS

> **This block is updated at the end of every session.**

- **Current phase:** Phase 9 — VPS Provisioning (Oracle Cloud Always Free)
- **Current stage / task:** Stage 09 — Create Oracle Cloud account + provision VPS
- **Phase 0 (Planning):** ✅ Complete
- **Phases 1–7 (Code → Quality → VCS → CI/CD → Docker → Registries → Compose):** ✅ Complete
- **Phase 8 (SSH & Remote Connections):** ✅ Complete — mental model, practice, Part C questions answered
- **Last completed item:** Session 05 (2026-10-01, recap-only) — **Block D (Pipelines) evaluated
  and validated ✅**, closing the evaluation debt left open by Session 04. New concepts captured:
  parallelism (GitHub `needs` DAG) vs serialization (GitLab `stages`), image identity by 8-char
  commit SHA vs moving `:latest`, and **silent drift** between the three registries (nothing turns
  red when tags diverge). Rule reaffirmed: **`:latest` only locally; the VPS pins the SHA.**
- **Daily recap status:** Session 05 (2026-10-01) — Block D ✅ (needs-vs-stages semantics,
  8-char tag identity, `--password-stdin` **still untouched**). **Block F (Registries) has never
  been evaluated** — it is the next block in the rotation.
- **Next session target:** **Repo hygiene debt FIRST (15 min, before Stage 09)** — resolve the
  `nuevo.py` regression + add it to `.gitignore` + confirm today's pipeline runs → then recap
  **Block F (Registries)** with varied questions → then Phase 9 — Stage 09 **Session 1: Oracle
  Cloud account, Always Free quotas, Always Free vs trial credits**. Stage 09 still has **zero**
  checkboxes marked.
- **✅ Repo state VERIFIED 2026-10-01** (real `git fetch` to both remotes, no `BatchMode`):

  | Ref | SHA | Status |
  |---|---|---|
  | `develop` | `dc41430` | = `github/develop` = `gitlab/develop` ✅ |
  | `master` | `f51df86` | merge PR #79, contains `develop` ✅, content identical |
  | `github/master` | `f51df86` | ✅ |
  | `gitlab/master` | `2ce2b11` | ✅ contains `develop` — **this was wrongly reported stale earlier today** |

  **All 6 refs are content-identical** (`git diff` = 0 for every pair) and `develop` is an ancestor
  of all of them. Nothing is out of sync. GitLab SSH works: `id_ed25519_gitlab` + `~/.ssh/config`
  Host block → `Welcome to GitLab, @ericksuper80!`.
  > **The 68 extra merge commits in `gitlab/master` are normal mirror divergence** — GitLab creates
  > a merge every time `master` is pushed there. Two mirrors can have **different history with
  > identical content**. The only correct check is `git diff` between refs = 0, never "do the SHAs
  > look the same".
- **⚠️ Repeat false positive (2nd occurrence — read the rule before trusting any remote claim):**
  this file previously reported `gitlab/master = 36aaf77` as **stale/unverified**. That was wrong:
  the remote was at `2ce2b11` all along. Cause: the mentor's own `GIT_SSH_COMMAND='ssh -o
  BatchMode=yes'` blocked the fetch and produced a fake `publickey` error, then the stale
  remote-tracking ref was treated as fact. **Session 04 had the identical mistake (finding F-01).**
  Rule: *a remote is unknown until you `git fetch` it, and a remote-tracking ref is Git's memory of
  the remote, not the remote.* Never write a remote's state into the docs from a tracking ref alone.
- **⚠️ Undocumented work found in the repo (2026-10-01):** 7 commits dated today touch **only
  `nuevo.py`** (`eb0c9ca` add → `99a1434` → `0968c30` → `ffe257c` → `0618ba0` → `c533b6e` →
  `dc41430` format fix). They are **not project progress** and have **no session-log entry**.
  Their messages also break the conventional-commit convention (`feature3 commit 0`,
  `feature4 commit 1`, …) → portfolio defect.
- **✅ `nuevo.py` — resolved by student decision (2026-10-01):** it is a **deliberate local
  practice file** and **stays in the repo** (`develop` + `master`). Impact verified as nil: the
  `Dockerfile` runs `COPY Principal.py .`, so it never enters the image. Trade-off accepted: it
  does pass through the 7 CI gates on every push (hence `dc41430 fix: format nuevo.py to pass
  linting`), but it cannot affect the deployed app. Logged as a decision, not an accident — see
  `AGENTS.md` Repo Hygiene Rules #1.
- **✅ Pipeline state at HEAD `dc41430` (2026-10-01):** the student reports **all jobs green**
  (unit tests + lint + security) after the `dc41430` formatting commit. The 6 earlier commits of
  that `nuevo.py` series may still show red runs in the history — irrelevant operationally (HEAD is
  what ships) but visible to an interviewer reading the run list.
- **Housekeeping:** decide whether the `GHCR_USERNAME`/`GHCR_TOKEN` GitLab CI variables are
  dropped — ADR-0007 removed the need for a cross-platform PAT (an older block of this file
  still mentions them as a next step).
- **Blockers / open questions:** none technical. Pipelines green at `dc41430` (confirmed by the
  student: tests + lint + security). **Pending:** memory docs are synced into `C:\Repo2\docs/` but
  **still uncommitted**, and `docs/delivery-story.md` is a new untracked file in the repo.
- **Last session:** 2026-10-01 — Session 05 recap-only (Block D): closed the pending pipelines
  evaluation with new angles (platform parallelism semantics, tag identity + registry drift);
  2 misunderstandings corrected (GitLab stages are sequential; GitLab does not receive the image)
  + 1 mentor lapse (tag identity was assumed instead of explained, then taught in depth). New
  Sticky Frames added to AGENTS.md. No stage work — student closed the day
- **Last commit / push:** Session 05 memory changes committed as `0b15177` — `docs(session-05):
  close Block D recap, repo audit + student decision on nuevo.py, sync delivery-story v1.0`
  (5 files: +343/−35, including `docs/delivery-story.md` as a new file). Pushed to **GitHub
  develop** and **GitLab develop** (`0b15177..0b15177`). **All remotes verified with a real
  `git fetch`:** `develop`/`github/develop`/`gitlab/develop` = `0b15177`; `master`/`github/master`
  = `1dc240a` (FF from `f51df86` after the student's merge of develop→master on GitHub/GitLab);
  `gitlab/master` = `74102e8`. **Content parity:** `git diff develop <any master/*>` = 0 (all
  content-identical) and `develop` is an ancestor of every `master/*` (all in sync). Local
  `master` was FF-updated to `github/master` (no history rewrite), and the working tree was left
  clean on `develop`. The 68 merge commits on `gitlab/master` are the normal mirror divergence
  (different history, identical content).

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

## Timeline (2 sessions/week, 1.5–2 h each)

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
| 9 VPS Provisioning | Weeks 2–3 | 2–3 |
| 10 Linux Administration | Weeks 3–5 | 6–8 |
| 11 Deployment to Server | Weeks 5–6 | 2–3 |
| 12 Production Hardening | Weeks 6–9 | 6–8 |
| 13 FastAPI Full Stack | Weeks 9–12 | 4–6 |
| 14 Portfolio & Interview | Weeks 12–13 | 2–3 |

> Total remaining ≈ 25–35 sessions ≈ 3 months. Cadence may be adjusted — understanding
> is the only fixed requirement.

---

## Session Workflow — v2 (Spiral Repetition + Feedback Loop)

**Daily recap mini-session v2 (before anything else, every day, ~15 min cap):**

1. The mentor gives the **general journey summary** (2–3 min, always).
2. For **each of the 1–2 blocks of the day** (rotating, cyclical A→H then loop), execute the
   per-topic micro-cycle (`AGENTS.md`):
   - **Specific summary + analogy** for that topic (what it is, why it exists, how it
     intervenes in `CICD.txt` flow, failure mode)
   - **Comprehension check:** *"¿Lo entendiste o necesitas otra explicación?"* → if needed,
     re-explain differently; if asimilado, proceed
   - **Varied evaluation:** exactly **one question at a time**, topic repeats but exact
     question never repeats unless `refuerzo útil ⏰`
   - **Student Q&A slot:** *"¿Tienes preguntas tú sobre este tema?"* → log Q&A
   - **Topic gate:** ✅ next topic / ⚠️ reinforce with different question next session
3. The recap is **general and cyclical** — covers **complete delivery flow + every tool/file
   in CICD.txt** (Blocks A–H), always with intentional topic repetition for retention after
   a full A→H cycle loops to A with varied Qs.
4. **When the day's practice is judged complete** (1–2 topics validated), **immediately
   transition to the work session** — no gap.
5. Result recorded **per-topic** in `session-log.md` (table: summary/analogy, check,
   Qs+answers+verdict, your Qs, verdict) + `Recap meta` (timing, bank update). This log is
   permanent memory and feeds future recaps.

**Start of the progress session (10 min):**

1. Read **Current Status** above.
2. Read the last entry of `session-log.md` (per-topic table + work log).
3. Read the current stage document.
4. Tell the mentor what you remember from the previous session.

**During the session:**

5. Work the stage checklist. The mentor guides with questions (why-first, 1 at a time).
   New concepts are taught with the same micro-cycle (summary+analogy → check → evaluation).

**End of session (20 min):**

6. Fill the stage report section in the stage document.
7. Save screenshots/evidence in `screenshots/stage-NN/`.
8. Append an entry to `session-log.md` with **per-topic recap table + work session log**
   (what was built, decisions, commands with why, errors/hypotheses/resolutions — this
   becomes future recap material).
9. Tick completed checkboxes in this file and update **Current Status** + confirm question
   bank updated (no exact duplicate unless refuerzo útil).
10. Write an ADR if a meaningful decision was made.
11. Sync this folder with `C:\Repo2`, commit with a conventional message, push to
     **both** GitHub and GitLab.
12. Confirm the next session's target (next blocks in rotation + next work checkbox).

---

## Related Documents

- [`AGENTS.md`](../AGENTS.md) — AI operating manual & Definition of Done
- [`project-specification.md`](project-specification.md) — vision and scope
- [`mentor-constitution.md`](mentor-constitution.md) — mentoring principles
- [`learning-roadmap.md`](learning-roadmap.md) — competency map
- [`session-log.md`](session-log.md) — daily diary
- [`environment.md`](environment.md) — local environment preparation
