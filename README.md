# CI/CD Pipeline Labs

> Turning a small Python application into a fully automated, containerized, multi-registry, production-deployed software delivery pipeline — stage by stage, publicly documented from day one.

**Type:** Practical learning project + professional portfolio
**Duration:** ~6–8 weeks remain (route v2, 5 sessions/week, ~2 h each)
**Language:** English (public documentation)

---

## The Story

This is the repository of a **DevOps Junior candidate** learning the *complete software
delivery lifecycle* by building it with his own hands. It does not start with a finished
product — it starts with a simple Python script and a question: *"how does code actually
reach a user in a modern company?"*

Then, stage by stage, the story unfolds:

1. First, a **simple Python application** with tests is written (Phase 1).
2. **Code quality tools** are added — not because they are trendy, but because a
   professional pipeline never ships broken code (Phase 2).
3. **Git** versions everything from day one, mirrored on **GitHub and GitLab** (Phase 3).
4. **CI/CD pipelines** automate linting, testing, and building on *both* platforms
   (Phase 4).
5. **Docker** turns the code into a portable image (Phase 5).
6. The same image is published to **three registries** — Docker Hub, GHCR, and GitLab
   Container Registry (Phase 6).
7. **Docker Compose + Watchtower** simulate continuous deployment locally (Phase 7).
8. Next: the application evolves into a **FastAPI service with MySQL 8 and a
   `/health` endpoint** — *before* deployment, so the server phases are built once
   (Phase 10, ADR-0008).
9. The first real server is provisioned **from code** with **Terraform + cloud-init**
   and configured with **Ansible** (Phases 9 & 11, ADR-0009), on a **zero-cost** VPS.
10. The pipeline deploys with an **immutable tag over SSH**, with healthcheck and a
    practiced **rollback** (Phase 12).
11. The server is **hardened**: Nginx, HTTPS with a free hostname, persistence,
    backups with a tested restore (Phase 13).
12. The system is **observed**: Uptime Kuma, Prometheus, Grafana, and a real
    Telegram alert that reaches the phone (Phase 14, ADR-0011).
13. The repository ends as a curated, demo-able, interview-ready portfolio
    (Phase 15, ADR-0014).

Every step is documented with evidence, screenshots, and the reasoning behind each
decision. This is not a tutorial; it is a complete engineering journey.

Every session begins with a **concept-by-concept review**: one concept at a time, with an
example, an analogy, its connection to previous concepts, and a space for questions before
advancing, so understanding is real — not memorized.

---

## Why This Project Exists

This project is not about memorizing YAML. It is about building **technical judgment** —
the ability to explain why each pipeline stage exists, how the components communicate
(Git → Pipeline → Build → Registry → Server), and how to diagnose a problem when
something breaks.

The goal is that after finishing, when asked *"Why do you run Black in CI?"*, *"What is
the difference between CI and CD?"*, *"Why three registries?"*, or *"How does the image
get from the registry to the server?"*, the answer comes from real understanding, not
from a copied tutorial.

---

## Cost Policy

The project is built to cost **$0**. All tools, cloud services, and domains are free-tier
or free. The student has no income during the project, so any expense must be justified,
discussed with the mentor, and explicitly approved before it happens. Cloud provider
strategy is documented in [`docs/adr/0005-zero-cost-cloud-strategy.md`](docs/adr/0005-zero-cost-cloud-strategy.md).

---

## Repository Layout

```
.
├── AGENTS.md                     # Operating manual for any AI mentor working on this repo
├── docs/
│   ├── project-specification.md  # Vision, scope, success criteria
│   ├── mentor-constitution.md    # Pedagogical & technical principles of the mentor
│   ├── learning-roadmap.md       # Competency map — "you are done when you can..."
│   ├── execution-plan.md         # ⭐ THE status file — phases, checklists, current state
│   ├── session-log.md            # Daily diary (reverse-chronological)
│   ├── environment.md            # Local environment (Windows host, Docker Desktop, C:\Repo2)
│   ├── adr/                      # Architecture Decision Records
│   └── stages/                   # One document per stage
├── screenshots/                  # Evidence, one folder per stage
├── scripts/                      # Scripts created during stages
└── .gitignore
```

> The **code itself lives in `C:\Repo2`** (the real repository, mirrored to GitHub and
> GitLab). This folder is the **memory/planning** folder and stays in sync with it.

---

## Phase Map

> **Route v2 (2026-10-29 audit):** phases 9–15 reordered and extended per
> ADR-0008…0014 — see `docs/execution-plan.md` and the Priority Action List.

| Phase | Topic | Status |
|---|---|---|
| 0 | Planning & Documentation Architecture | ✅ Complete |
| 1 | Application Development (Python) | ✅ Complete |
| 2 | Code Quality & Automated Testing | ✅ Complete |
| 3 | Version Control & Repositories | ✅ Complete |
| 4 | CI/CD Pipelines | ✅ Complete |
| 5 | Containerization | ✅ Complete |
| 6 | Registries & Image Publishing | ✅ Complete |
| 7 | Orchestration & CD Simulation | ✅ Complete |
| 8 | SSH & Remote Connections | ✅ Complete |
| 9 | VPS Provisioning with Terraform + cloud-init | 🔄 Current |
| 10 | FastAPI + MySQL Evolution + CI/CD v2 | ⬜ Pending |
| 11 | Linux Administration + Ansible | ⬜ Pending |
| 12 | Deployment: immutable tag, CD, rollback | ⬜ Pending |
| 13 | Hardening: Nginx, HTTPS, backups | ⬜ Pending |
| 14 | Observability & Alerting | ⬜ Pending |
| 15 | Portfolio & Interview Packaging | ⬜ Pending |

> **Live status:** see [`docs/execution-plan.md`](docs/execution-plan.md) — the single
> source of truth for what is done and what is next.

---

## How This Repository Is Maintained

- **Single source of truth:** [`docs/execution-plan.md`](docs/execution-plan.md) stores
  the current phase, the current stage, and every checkbox. It is updated at the end of
  every session.
- **Daily session v4:** review 3–5 concepts (one at a time, with canonical explanation,
  analogy, connection, questions, and verification), then one practical objective, then
  documentation. Standard day: 2 h; hard maximum: 2.5 h; 5 days/week plus a short weekly
  consolidation (see [`AGENTS.md`](AGENTS.md)).
- **AI-friendly:** Any AI agent that joins the project follows the bootstrap protocol in
  [`AGENTS.md`](AGENTS.md), which guarantees instant recall of what exists, what is done,
  and what is next.
- **Definition of Done:** a session is finished only when it is understood, documented,
  evidenced, and the memory folder is synchronized with `C:\Repo2`.
- **Mirrored repositories:** the project lives in `C:\Repo2` and is mirrored to GitHub and
  GitLab. Commit/push only when the student explicitly asks; the current preference is
  sync-only.
- **Zero cost:** the whole project runs on free-tier services (see Cost Policy).

---

## First Steps

1. Read [`docs/execution-plan.md`](docs/execution-plan.md) → **Current Status** (Phase 9 — VPS Provisioning with Terraform, route v2).
2. Read [`docs/adr/0009-iac-terraform-ansible.md`](docs/adr/0009-iac-terraform-ansible.md) → provider decision gate.
3. Start **Stage 09 — Session 0** ([`docs/stages/stage-09-vps-provisioning.md`](docs/stages/stage-09-vps-provisioning.md)).

---

## Author

**Erick Perez** — Aspiring DevOps Engineer building hands-on experience with CI/CD,
containers, Linux, automation, cloud infrastructure, and software delivery pipelines.
