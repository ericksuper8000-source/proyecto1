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

Build, step by step, a real software delivery pipeline that starts as a small Python
application and evolves into a containerized application that is automatically tested,
built, published to three registries, and deployed to a free VPS — documented end to end
with good engineering practices.

The student must understand each component **before** automating it.

---

## 3. Scope

Included:

- Python application development (and later FastAPI)
- Code quality: Ruff, Flake8, Black, MyPy
- Automated testing with Pytest
- Git, GitHub, and GitLab (mirrored repositories)
- CI/CD with GitHub Actions and GitLab CI
- Docker, Docker images, and Docker Compose
- Container registries: Docker Hub, GHCR, GitLab Container Registry
- Continuous Deployment simulation (Watchtower)
- SSH and remote administration
- VPS provisioning (Oracle Cloud Always Free) and Linux administration
- Production practices: Nginx, HTTPS, environment variables, volumes, logs, backups, monitoring

Explicitly out of scope:

- Large-enterprise infrastructure, high availability, complex clusters
- Kubernetes (only referenced, never a goal)

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

What remains to be built from here:

- SSH understanding and real remote connections
- A free VPS (Oracle Cloud Always Free)
- Linux administration on the server
- Docker Engine + Compose on the server
- Deployment through the pipeline (`git clone` → `docker compose up`)
- Production hardening, Nginx, HTTPS, persistence, logs, backups, monitoring
- FastAPI full-stack evolution

---

## 7. Resources

Current infrastructure:

- Windows 10/11 host
- Visual Studio Code + Git Bash
- Python 3.11
- Docker Desktop (Engine + Compose)
- Repositories on GitHub (`proyecto1`) and GitLab (`repo2`), mirrored
- Three container registries (Docker Hub, GHCR, GitLab Container Registry)

Future infrastructure:

- Free VPS (e.g., Oracle Cloud Always Free or an equivalent available at that time)
- Nginx, Let's Encrypt, and optional database/monitoring services

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
Developer / Code
  ↓
Version Control (Git)
  ↓
Quality & Testing
  ↓
CI/CD Pipeline (GitHub Actions + GitLab CI)
  ↓
Docker Images
  ↓
Registries
  ↓
SSH / Remote Access
  ↓
VPS (Linux)
  ↓
Deployment (Docker Engine + Compose)
  ↓
Production Hardening (Nginx, HTTPS, Volumes, Logs, Backups)
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
| 8 | SSH & Remote Access | Understand and use SSH | ✅ Complete (2026-08-25) |
| 9 | VPS Provisioning | Oracle Cloud Always Free, Ubuntu | 🔄 Current |
| 10 | Linux Administration | Users, permissions, filesystem, packages, firewall | ⬜ |
| 11 | Deployment to Server | Docker Engine, Compose, git clone, compose up | ⬜ |
| 12 | Production Hardening | Nginx, HTTPS, env, volumes, logs, backups, monitoring | ⬜ |
| 13 | FastAPI Full Stack | FastAPI, PostgreSQL, health checks | ⬜ |
| 14 | Portfolio & Interview | Architecture docs, interview defense | ⬜ |

> Detailed checklists and current status: [`execution-plan.md`](execution-plan.md)

---

## 11. Expected Competencies

By the end of the project, the student can:

- Explain the full delivery lifecycle: code → test → build → publish → deploy
- Write and justify CI/CD pipelines on GitHub Actions and GitLab CI
- Build, publish, and pull Docker images across multiple registries
- Operate Docker Compose stacks
- Connect to and administer a Linux VPS over SSH
- Deploy an application to a server and keep it running
- Diagnose pipeline and server failures
- Explain every technical decision made

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
- Justify every pipeline and infrastructure decision
- Diagnose problems in CI/CD and on a live server
- Document professionally
- Deploy a containerized application to a free VPS through CI/CD
- Defend the whole project in a technical interview

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
