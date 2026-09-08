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
- [ ] I can explain why Black runs as `--check` in CI instead of modifying files.
- [ ] I can explain what a unit test is and what makes a good test.
- [ ] I can justify why a professional pipeline never ships broken code.
- [ ] I can explain **what Bandit scans** (hardcoded secrets, injection) and why it runs in CI.
- [ ] I can explain **what pip-audit checks** vs Bandit, and how both protect the flow.
- [ ] I can explain **`.gitignore` vs `.dockerignore` vs `.gitattributes`** — what each excludes, why `.venv/__pycache__/*.pem/.env` must not go to Git nor to image, and what breaks if they do.
- [ ] I can explain **YAML** as a language (maps, lists, indentation, why a missing space breaks the pipeline) and why the runner reads it.

---

## Phase 3 — Version Control & Repositories

- [ ] I can explain what a commit is and what makes a commit "meaningful".
- [ ] I can explain the difference between the working directory, staging area, and repository.
- [ ] I can explain the branch strategy (`master` vs `develop`) and why a PR/merge is used.
- [ ] I can push to both GitHub and GitLab and explain why the project is mirrored.

---

## Phase 4 — CI/CD Pipelines (incl. YAML & secrets)

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
- [ ] I can explain why persistence will matter in production (Phase 12).
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

## Phase 9 — VPS Provisioning

- [ ] I can explain the difference between a local computer and a cloud VPS.
- [ ] I can explain what an instance is and why Ubuntu was chosen.
- [ ] I can explain the free-tier limits of the chosen provider and how to avoid costs (ADR-0005).
- [ ] I can connect to the VPS over SSH and verify the basics.

---

## Phase 10 — Linux Server Administration

- [ ] I can update/upgrade the system and explain what `apt` does.
- [ ] I can create users, groups, and permissions and explain why they exist.
- [ ] I can navigate the filesystem and explain the purpose of `/etc`, `/var`, `/home`.
- [ ] I can configure a firewall so only the needed ports are open.
- [ ] I can explain SSH hardening measures and apply them.
- [ ] I can install Docker Engine and the Compose plugin and explain what each installs.

---

## Phase 11 — Deployment to the Server

- [ ] I can explain why we clone the project (compose file) instead of building on the server.
- [ ] I can run `docker compose up -d` and explain what the server does (pull → create → start).
- [ ] I can verify the application responds with `curl`.
- [ ] I can explain how the application comes back after a reboot.
- [ ] I can explain (if implemented) how a CD job deploys on push.

---

## Phase 12 — Production Hardening & Observability

- [ ] I can explain why Nginx sits in front of the application.
- [ ] I can explain why HTTPS is non-negotiable and how certificates are obtained.
- [ ] I can explain volumes vs bind mounts and why the database needs persistence.
- [ ] I can read container and Nginx logs to diagnose a failure.
- [ ] I can explain the backup strategy and demonstrate a restore.
- [ ] I can describe a basic rollback strategy and why it matters.

---

## Phase 13 — FastAPI Full Stack

- [ ] I can explain why the database is a separate service.
- [ ] I can explain what a health check is and why monitoring needs one.
- [ ] I can explain how environment variables make dev/prod configuration possible.
- [ ] I can run the full stack and the full pipeline for the evolved app.

---

## Phase 14 — Final Project & Portfolio

- [ ] I can explain the final architecture end to end (user → Nginx → app → DB).
- [ ] I can walk an interviewer through the repository, phase by phase.
- [ ] I can justify every major decision using the ADRs.
- [ ] I can answer "Why did you do it this way?" for each component.

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
| 9 VPS Provisioning | ⬜ | ⬜ | |
| 10 Linux Administration | ⬜ | ⬜ | |
| 11 Deployment to Server | ⬜ | ⬜ | |
| 12 Production Hardening | ⬜ | ⬜ | |
| 13 FastAPI Full Stack | ⬜ | ⬜ | |
| 14 Portfolio & Interview | ⬜ | ⬜ | |
