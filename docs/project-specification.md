# PROJECT SPECIFICATION

> **Project:** CI/CD Pipeline Labs
> **Version:** 1.0 (2026 revision)
> **Status:** Active
> **Type:** Documented practical learning + professional portfolio

---

## 1. Vision

CI/CD Pipeline Labs is a practical learning project that builds the technical competencies
required to work as a **DevOps Junior**. It covers the **complete software delivery
lifecycle**: writing a small application, guaranteeing its quality with automated tools,
containerizing it, publishing images to multiple registries, automating everything with
CI/CD pipelines on two platforms, and finally deploying the application to a real Linux
server with production practices.

The project does not teach isolated commands or tutorial completion. Its purpose is to
develop the ability to understand, operate, and justify an entire software delivery
pipeline — from `git push` to a running application.

Everything is built publicly as professional evidence of learning.

---

## 2. Main Objective

Build, step by step, the **Deploy Journal** product — a small deployment-history service
(Python + FastAPI + MySQL 8) — and around it a real delivery pipeline that tests the
product, builds multi-arch images, publishes them to three registries, and deploys to a
free VPS **provisioned with Terraform and configured with Ansible** — then hardens it
(Nginx, HTTPS, backups) and **observes** it (monitoring, dashboards, alerts) — all
documented end to end with good engineering practices.

### The product (ADR-0015)

**Deploy Journal** records every deployment of this pipeline: version (immutable tag),
environment, status (success/failed/rollback), message and author. It exposes a public
timeline page, stats, and a `/health` endpoint that checks the database. The pipeline
writes to the app after each deploy — the product is the pipeline's own mirror.

The pipeline, tooling and infrastructure are **derived from this product** (ADR-0016),
never the other way around.

The student must understand each component **before** automating it.

---

## 3. Scope

Included:

- **Deploy Journal** (product, ADR-0015): deployment-history API + public timeline,
  built with Python + FastAPI + MySQL 8
- Code quality: Ruff, Flake8, Black, MyPy (harmonized in `pyproject.toml`, ADR-0013)
- Automated testing with Pytest (unit + API tests + coverage)
- Supply-chain checks: Bandit, pip-audit, Trivy, Dependabot, gitleaks, pre-commit
- Git, GitHub, and GitLab (mirrored repositories; public curation per ADR-0014)
- CI/CD with GitHub Actions and GitLab CI (CI/CD v2 rules, ADR-0013)
- Docker, multi-arch images (amd64+arm64, ADR-0010), and Docker Compose
- Container registries: Docker Hub, GHCR, GitLab Container Registry
- Continuous Deployment simulation (Watchtower, local only)
- SSH and remote administration
- **Infrastructure as Code: Terraform + cloud-init (ADR-0009)**
- **Configuration management: Ansible bootstrap playbook (ADR-0009)**
- VPS provisioning (Oracle Always Free or owned Hetzner) and Linux administration
- **Database: MySQL 8 (ADR-0012)**
- Production practices: Nginx, HTTPS (free domain), environment variables, volumes,
  logs, backups + restore drill
- **Observability: Uptime Kuma, cAdvisor, Prometheus, Grafana, Telegram alerts (ADR-0011)**
- Deployment with immutable tags, CD over SSH, and rollback (ADR-0013)
- Public portfolio packaging: README v2, demo, LICENSE, releases (ADR-0014)

Explicitly out of scope:

- Large-enterprise infrastructure, high availability, complex clusters
- Kubernetes (only referenced conceptually, never a goal)
- Paid services of any kind (zero-cost rule, ADR-0005)

---

## 4. Project Story

A young DevOps candidate is handed a simple Python script and asked: *"take this from my
laptop to a real server used by real users."* The candidate must decide, step by step:
how to guarantee the code is good, how to package it, where to store it, how to build and
test it automatically, and finally how to make it run on a remote server — and keep it
running.

Every stage is a task that could exist in a professional environment. No isolated
exercises. Every stage leaves the project in a better state than before.

---

## 5. Philosophy

### Understand before memorizing

No command memorization. Concepts first.

### Understand before automating

No automation may hide how the delivery pipeline actually works.

### Learn by doing

Every concept is applied immediately in a real stage.

### Document everything

Nothing is finished until documented with evidence.

### One evolving pipeline

The pipeline evolves across the entire journey. No throwaway projects.

---

## 6. Initial State

The project already completed Phases 1–7 (application, quality, version control, CI/CD,
containerization, registries, orchestration/CD simulation). See
[`execution-plan.md`](execution-plan.md) for the verified state of each phase.

What remains to be built from here (route v2.1, 2026-10-29):

- The product: **Deploy Journal** (FastAPI + MySQL 8 + CI/CD v2) — ADR-0015/0016
- A VPS provisioned **from code** (Terraform + cloud-init), sized from the product
- Linux administration + Ansible bootstrap
- Deployment through the pipeline (immutable tag → CD over SSH → healthcheck → rollback)
- Production hardening: Nginx, HTTPS, persistence, logs, backups + restore drill
- Observability: Uptime Kuma, metrics, dashboards, Telegram alerts
- Public portfolio packaging: README v2, demo, LICENSE, releases

---

## 7. Resources

Current infrastructure:

- Windows 10/11 host
- Visual Studio Code + Git Bash
- Python 3.11
- Docker Desktop (Engine + Compose)
- Repositories on GitHub (`proyecto1`) and GitLab (`repo2`), mirrored
- Three container registries (Docker Hub, GHCR, GitLab Container Registry)

Future infrastructure (all free — ADR-0005):

- Free VPS (Oracle Cloud Always Free, or an owned Hetzner server) provisioned with
  Terraform + cloud-init
- Ansible for server bootstrap
- MySQL 8 as the database service
- Nginx + Let's Encrypt with a free hostname (DuckDNS / sslip.io / nip.io)
- Monitoring stack: Uptime Kuma, cAdvisor, Prometheus, Grafana, Alertmanager
- Telegram bot API for alerts
- Free off-site backup target (Cloudflare R2 free 10 GB / Google Drive 15 GB)

### Zero-cost principle

The student currently has no income, so the project **must stay at $0 cost** (or as close
as technically possible). Every cloud service, tool, and domain choice must be free-tier
or free. If a paid option is ever required, it must be justified, discussed with the
mentor, and explicitly approved **before** any expense. Cloud provider strategy is
recorded in ADR-0005.

---

## 8. Methodology

Every session follows the same structure:

1. Daily recap & validation mini-session (one question at a time, before any progress).
2. Review of the previous session.
3. Conceptual explanation (why first).
4. Professional scenario.
5. Practical stage.
6. Technical discussion.
7. Documentation and evidence.
8. State update and definition of the next stage.

Do not advance while conceptual gaps exist. Understanding gates progress.

---

## 9. Learning Architecture

Knowledge is built in layers, and each layer depends on full understanding of the
previous one:

```
Developer / Code (FastAPI + MySQL)
  ↓
Version Control (Git)
  ↓
Quality & Testing
  ↓
CI/CD Pipeline (GitHub Actions + GitLab CI)
  ↓
Multi-arch Docker Images
  ↓
Registries
  ↓
SSH / Remote Access
  ↓
VPS via Terraform + cloud-init (IaC)
  ↓
Bootstrap via Ansible
  ↓
Deployment (immutable tag, CD, rollback)
  ↓
Production Hardening (Nginx, HTTPS, Volumes, Logs, Backups)
  ↓
Observability (Uptime Kuma, Prometheus, Grafana, Alerts)
```

---

## 10. Roadmap (Phases)

| # | Phase | Description | Status |
|---|---|---|---|
| 0 | Planning | Documentation architecture, methodology, roles | ✅ |
| 1 | Application Development | Python fundamentals + first app | ✅ |
| 2 | Code Quality & Testing | Ruff, Flake8, Black, MyPy, Pytest | ✅ |
| 3 | Version Control | Git, GitHub, GitLab, branches | ✅ |
| 4 | CI/CD Pipelines | GitHub Actions + GitLab CI | ✅ |
| 5 | Containerization | Dockerfile, build, images | ✅ |
| 6 | Registries | Docker Hub, GHCR, GitLab Registry | ✅ |
| 7 | Orchestration & CD Sim | Docker Compose + Watchtower | ✅ |
| 8 | SSH & Remote Access | Understand and use SSH | ✅ |
| 9 | Deploy Journal (product-first) | FastAPI + MySQL 8 + timeline + CI/CD v2 | 🔄 Current |
| 10 | VPS Provisioning (IaC) | Terraform + cloud-init, sized from the product | ⬜ |
| 11 | Linux Admin + Ansible | Users, firewall, Docker, idempotent playbook | ⬜ |
| 12 | Deployment | Immutable tag, CD over SSH, rollback | ⬜ |
| 13 | Production Hardening | Nginx, HTTPS, persistence, backups + restore | ⬜ |
| 14 | Observability & Alerting | Uptime Kuma, metrics, Grafana, Telegram alerts | ⬜ |
| 15 | Portfolio & Interview | Public README v2, demo, LICENSE, curation | ⬜ |

> Detailed checklists and current status: [`execution-plan.md`](execution-plan.md)

---

## 11. Expected Competencies

By the end of the project, the student can:

- Explain the full delivery lifecycle: code → test → build → publish → deploy → observe
- Derive the pipeline and infrastructure from product requirements (ADR-0016)
- Write and justify CI/CD pipelines on GitHub Actions and GitLab CI
- Build, publish, and pull multi-arch Docker images across multiple registries
- Operate Docker Compose stacks (app + database)
- Provision a server from code with Terraform + cloud-init
- Bootstrap a server idempotently with Ansible
- Connect to and administer a Linux VPS over SSH
- Deploy an application with an immutable tag, healthcheck, and rollback
- Harden a server: reverse proxy, HTTPS, firewall, backups with tested restore
- Monitor the system and receive real alerts
- Diagnose pipeline and server failures
- Present and defend the project with a public demo and the ADRs

---

## 12. Documentation

Professional documentation is produced for the whole project. Each stage includes, when
applicable: objective, context, procedure, technical explanation, commands used,
screenshots, problems encountered, solutions, and conclusions.

Reasoning behind decisions is captured as **Architecture Decision Records (ADRs)** in
`docs/adr/`, making the "why" interview-ready.

---

## 13. Repositories

The project is published on **GitHub** and **GitLab** (mirrored). The real repository
lives in `C:\Repo2`; this folder (`CICD - Project`) is the memory and
planning folder and stays in sync with it.

Every commit represents meaningful progress. Documentation carries the same weight as
technical implementation.

---

## 14. Restrictions

- No tool is introduced before the problem it solves is understood.
- No tutorial is copied without understanding.
- No command memorization.
- No skipped documentation.
- No rushing that sacrifices understanding.
- No creating the VPS before SSH is understood.

---

## 15. Success Criteria

The project is successful when there is evidence that the student can:

- Operate a software delivery pipeline with judgment
- Justify every pipeline and infrastructure decision (ADRs)
- Show that every pipeline element traces to a product requirement or a named risk
  (ADR-0016)
- Provision infrastructure from code (Terraform) and configure it reproducibly (Ansible)
- Diagnose problems in CI/CD and on a live server
- Document professionally
- Deploy a containerized application to a free VPS through CI/CD, with rollback
- Restore a database from backup (practiced drill)
- Receive a real alert when the system fails
- Present a curated public repository with a live demo

The result must constitute a portfolio that shows the full evolution of learning and lets
an interviewer understand the technical level reached.

---

## 16. Related Documents

This project is supported by the following coherent document set:

- **`AGENTS.md`** — operating manual for any AI mentor on this repo
- **`docs/mentor-constitution.md`** — pedagogical and technical principles of the mentor
- **`docs/execution-plan.md`** — sequential execution state and checklists
- **`docs/learning-roadmap.md`** — competency map and progress
- **`docs/session-log.md`** — daily session diary
- **`docs/environment.md`** — local environment documentation

All are part of a single documentation architecture and must stay coherent with each other.

---

## Guiding Principle

> The goal of this project is not to learn how to copy a pipeline.
> The goal is to develop the technical judgment to think, act, and solve problems like a
> DevOps Engineer — using a real delivery pipeline as public evidence of that learning.
