# LEARNING ROADMAP

## Competency Map — "You are done when you can…"

**Project:** CI/CD Pipeline Labs
**Version:** 1.0 (2026 revision)

---

## How to Use This Document

This is the **competency map**. For every phase it defines the questions the student must
be able to answer and the skills they must demonstrate **without help**. It complements
[`execution-plan.md`](execution-plan.md) (the *what to do*) by defining *what "done"
means for your brain*.

The mentor uses these questions to validate understanding. The student uses them to
self-assess before marking a phase complete. If you cannot answer a question fluently,
the phase is **not** complete — regardless of how many checkboxes are ticked.

---

## Phase 0 — Planning

- [ ] I can explain the mission of the project in 3 sentences.
- [ ] I know the core documents and what each one is for.
- [ ] I understand the Definition of Done and why every session must update state.

---

## Phase 1 — Application Development

- [ ] I can explain why the project needs an application before it needs DevOps.
- [ ] I can write a small Python program with functions and tests without help.
- [ ] I can explain why tests must exist before the pipeline runs them.

---

## Phase 2 — Code Quality & Automated Testing (incl. exhaustive flow tools)

- [ ] I can explain the responsibility of each tool: Ruff, Flake8, Black, MyPy, Pytest, **Bandit (security)**, **pip-audit (supply chain)**.
- [ ] I can explain what Ruff detects, what it does not, and how it differs from Flake8,
  MyPy, Bandit and Black.
- [ ] I can explain what Flake8 checks, how it differs from Ruff and Black, and why it
  reports but does not rewrite.
- [ ] I can explain what Black changes, why CI runs `--check` instead of rewriting, and why
  it is a formatter rather than a linter.
- [ ] I can explain what MyPy checks, why type hints are not enforced at runtime, and why
  this project's lack of annotations limits MyPy's real coverage.
- [ ] I can explain what Bandit scans, why tests are excluded from it, and why a code
  security scanner does not replace dependency auditing or testing.
- [ ] I can explain what pip-audit checks, why it includes transitive dependencies, and why
  a requirements file is not a lock file or a security guarantee.
- [ ] I can explain what `.gitignore` does to untracked vs already-tracked files and why it
  is not a security barrier for secrets already committed.
- [ ] I can read a CI YAML file and explain its triggers, jobs, steps, `needs`/stages and
  why some jobs run in parallel while others wait.
- [ ] I can distinguish commit from push, explain which remote/branch triggers CI, and
  describe why local validation is only a rehearsal.
- [ ] I can explain the difference between a Dockerfile, an image and a container, and why
  layer order and `.dockerignore` matter.
- [ ] I can distinguish `.gitignore` from `.dockerignore` and explain why filtering the build
  context improves speed and reduces secret exposure.
- [ ] I can explain what a registry stores, why the same image goes to three registries, and
  why the commit tag is safer than `latest` for deployment.
- [ ] I can explain what Compose and Watchtower each do, and why `latest` is only a local CD
  simulation while the VPS pins a commit tag.
- [ ] I can explain what a VPS is, how SSH reaches it on port 22, why the first host-key
  warning appears, and why the private key never travels.
- [ ] I can explain why the quality/security gate has multiple reviewers, what question each
  answers, and how a failure blocks Docker/publish.
- [ ] I can explain why Black runs as `--check` in CI instead of modifying files.
- [ ] I can explain what a unit test is and what makes a good test.
- [ ] I can explain why tests are written by behavior/risk rather than one per file, and the
  difference between unit, integration and end-to-end tests.
- [ ] I can explain why coverage alone is not proof of quality.
- [ ] I can justify why a professional pipeline never ships broken code.
- [ ] I can explain **what Bandit scans** (hardcoded secrets, injection) and why it runs in CI.
- [ ] I can explain **what pip-audit checks** vs Bandit, and how both protect the flow.
- [ ] I can explain what `requirements.txt` is and is not (packages vs Python version),
  runtime vs dev dependencies, pinning/lock files, and how it affects CI, Docker, security
  and reproducibility.
- [ ] I can explain **`.gitignore` vs `.dockerignore` vs `.gitattributes`** — what each excludes, why `.venv/__pycache__/*.pem/.env` must not go to Git nor to image, and what breaks if they do.
- [ ] I can explain **YAML** as a language (maps, lists, indentation, why a missing space breaks the pipeline) and why the runner reads it.
- [ ] I can explain what **Trivy, Dependabot, gitleaks and pre-commit** each protect, and where each runs (image, dependencies, git history, local commits).
- [ ] I can explain **multi-arch images** (amd64 vs arm64), why buildx + QEMU are needed, and what `exec format error` means.
- [ ] I can explain why CI pins tool versions (`requirements-dev.txt`) and why an unpinned `pip install` is a time bomb.

---

## Phase 3 — Version Control & Repositories

- [ ] I can explain what a commit is and what makes a commit "meaningful".
- [ ] I can explain the difference between the working directory, staging area, and repository.
- [ ] I can explain the branch strategy (`master` vs `develop`) and why a PR/merge is used.
- [ ] I can push to both GitHub and GitLab and explain why the project is mirrored.

---

## Phase 4 — CI/CD Pipelines (incl. YAML & secrets)

- [ ] I can explain why the pipeline is designed around the application's stack (code → stack → dependencies/tests/build → pipeline), not before it.
- [ ] I can explain the difference between CI and CD with a real example.
- [ ] I can explain every element of the GitHub Actions workflow (triggers, jobs, steps, needs).
- [ ] I can explain the equivalent concepts in GitLab CI (stages, jobs, scripts).
- [ ] I can explain how a pipeline builds and pushes a Docker image automatically.
- [ ] I can explain why secrets are stored as CI variables and not in the repository.
- [ ] I can explain **YAML syntax pitfalls** (indentation, `:` vs `-`) that break a pipeline.
- [ ] I can explain **`.env` files vs CI secrets** and why `.env` is in `.gitignore`.

---

## Phase 5 — Containerization (incl. .dockerignore)

- [ ] I can explain the problem Docker solves.
- [ ] I can explain images vs containers and why images are immutable.
- [ ] I can write a Dockerfile and explain what a layer is.
- [ ] I can explain what `WORKDIR`, `COPY`, `RUN`, `CMD` do and why the order matters.
- [ ] I can explain **`.dockerignore`** — why it exists separately from `.gitignore`, what it prevents from entering the build context, and its impact on image size / cache / security.
- [ ] I can explain **build context** vs `.dockerignore` vs `.gitignore`.

---

## Phase 6 — Registries & Image Publishing

- [ ] I can explain why images must live in a registry and not only on the runner.
- [ ] I can explain why the image pushed to the three registries is the *same* image.
- [ ] I can explain the difference between Docker Hub, GHCR, and GitLab Container Registry.
- [ ] I can explain how a server will pull the image later.

---

## Phase 7 — Orchestration & CD Simulation (incl. exhaustive flow)

- [ ] I can explain the difference between Docker Compose and Docker Engine.
- [ ] I can read a `docker-compose.yml` and explain every field we use.
- [ ] I can explain what Watchtower does and how it simulates CD.
- [ ] I can explain why containers are ephemeral and what `restart: always` does.
- [ ] I can explain why persistence will matter in production (Phase 13).
- [ ] I can explain **how each piece intervenes in the flow**: `docker build → image → registry → compose (decides) → engine (executes, pulls, creates) → Watchtower (recreates)` — and what breaks if one link disappears.
- [ ] I can explain **Kubernetes conceptually**: what problem it solves when Compose is not enough (multi-host, scheduler, declarative state), how it compares to `docker compose up`, and why we do not install it (out of scope, reference only).

---

## Phase 8 — SSH & Remote Access

- [ ] I can explain what SSH is and what problem it solves.
- [ ] I can explain what happens, step by step, when I run `ssh usuario@servidor`.
- [ ] I can explain how key-based authentication works (private vs public key).
- [ ] I can explain why a server normally has no graphical interface.
- [ ] I can explain who/what I am controlling when I write commands over SSH.

---

## Phase 9 — VPS Provisioning with Terraform + cloud-init

- [ ] I can explain the difference between a local computer and a cloud VPS.
- [ ] I can explain what Terraform is for, what a provider/state/resource are, and what
  `plan`, `apply` and `destroy` each do.
- [ ] I can explain what cloud-init does at first boot and why the SSH key goes there.
- [ ] I can explain the free-tier limits of the chosen provider and how to avoid costs
  (ADR-0005/0009), including what a budget alert is.
- [ ] I can recreate the server from zero with `terraform apply` and connect over SSH.

---

## Phase 10 — FastAPI + MySQL Evolution

- [ ] I can explain why the app evolves to FastAPI **before** deployment (ADR-0008).
- [ ] I can write `GET /health` and explain why monitoring, Nginx and CD all need it.
- [ ] I can explain why the database is a separate service with its own volume.
- [ ] I can explain `requirements.txt` vs `requirements-dev.txt` and why CI pins versions.
- [ ] I can explain what `pyproject.toml` configures and why Black (88) and Flake8 (79)
  must be harmonized.
- [ ] I can explain multi-arch builds and verify a manifest covers both platforms.
- [ ] I can explain what a container smoke test proves that `docker build` does not.

---

## Phase 11 — Linux Server Administration + Ansible

- [ ] I can update/upgrade the system and explain what `apt` does.
- [ ] I can create users, groups, and permissions and explain why they exist.
- [ ] I can navigate the filesystem and explain the purpose of `/etc`, `/var`, `/home`.
- [ ] I can configure a firewall so only the needed ports are open, plus fail2ban basics.
- [ ] I can explain SSH hardening measures and apply them.
- [ ] I can install Docker Engine and the Compose plugin and explain what each installs.
- [ ] I can explain idempotency and prove it: two consecutive Ansible runs change nothing.

---

## Phase 12 — Deployment, CD & Rollback

- [ ] I can explain why the server clones the compose file instead of building images.
- [ ] I can explain why production uses the immutable SHA tag and never `:latest`.
- [ ] I can explain how the CD job deploys over SSH (scoped deploy key) and why it
  checks `/health` after deploying.
- [ ] I can explain the rollback strategy and demonstrate it (previous tag).
- [ ] I can explain how the app + database come back after a server reboot.

---

## Phase 13 — Production Hardening

- [ ] I can explain why Nginx (or Caddy) sits in front of the application.
- [ ] I can explain why HTTPS is non-negotiable, how certificates are obtained with a
  free hostname (DuckDNS/sslip.io/nip.io), and how auto-renewal works.
- [ ] I can explain volumes vs bind mounts and why the database needs persistence.
- [ ] I can read container and Nginx logs to diagnose a failure, and why log rotation
  limits exist.
- [ ] I can explain the backup strategy (mysqldump + off-site free target) and
  **demonstrate a restore**.

---

## Phase 14 — Observability & Alerting

- [ ] I can explain what Uptime Kuma, cAdvisor, Prometheus, Alertmanager and Grafana
  each do, and how they differ (uptime vs metrics vs dashboards vs alerts).
- [ ] I can explain how an alert flows from a failing `/health` to my Telegram.
- [ ] I can demonstrate the alert drill: stop the app → alert arrives.
- [ ] I can read a Grafana dashboard and say what each panel tells me.

---

## Phase 15 — Portfolio & Interview

- [ ] I can explain the final architecture end to end (user → Nginx → app → DB).
- [ ] I can walk an interviewer through the repository, phase by phase, in 5 minutes.
- [ ] I can justify every major decision using the ADRs (0001–0014).
- [ ] I can answer "Why did you do it this way?" for each component.
- [ ] I can show a live demo: deploy, rollback, alert, restore.

---

## Progress Tracker

| Phase | Self-assessment | Mentor validation | Date |
|---|---|---|---|
| 0 Planning | ✅ | ✅ | 2026-08-04 |
| 1 Application Dev | ✅ | ✅ | prior work |
| 2 Code Quality | ✅ | ✅ | prior work |
| 3 Version Control | ✅ | ✅ | prior work |
| 4 CI/CD Pipelines | ✅ | ✅ | prior work |
| 5 Containerization | ✅ | ✅ | prior work |
| 6 Registries | ✅ | ✅ | prior work |
| 7 Orchestration & CD Sim | ✅ | ✅ | prior work |
| 8 SSH & Remote Access | ✅ | ✅ | 2026-08-25 |
| 9 VPS + Terraform | ⬜ | ⬜ | |
| 10 FastAPI + MySQL | ⬜ | ⬜ | |
| 11 Linux + Ansible | ⬜ | ⬜ | |
| 12 Deployment & CD | ⬜ | ⬜ | |
| 13 Hardening & Backups | ⬜ | ⬜ | |
| 14 Observability | ⬜ | ⬜ | |
| 15 Portfolio & Interview | ⬜ | ⬜ | |
