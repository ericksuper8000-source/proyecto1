# ADR-0016 — Product-First Engineering & Phase Order v2.1

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Student principle, 2026-10-29: *"the pipeline is not defined by the
technologies I want to use, but by the viability and functionality of the product; the
stack defines dependencies and tools; the pipeline revolves around the product — not the
other way around."* This ADR formalizes that principle and renumbers the phases to obey
it.

---

## Decision

1. **Product-first rule:** the product definition precedes the stack; the stack precedes
   dependencies, tests, tooling, container, pipeline and infrastructure. **No element of
   the pipeline (job, tool, stage, server resource) may exist without a product
   requirement or a named risk that justifies it.**
2. **Phase order v2.1** (supersedes the order in ADR-0008/0009/0012/0013):
   **9 Deploy Journal (product + FastAPI + MySQL + CI/CD v2) → 10 VPS with Terraform →
   11 Linux + Ansible → 12 Deploy + CD + rollback → 13 Hardening + backups →
   14 Observability → 15 Portfolio.**
3. The app is built, tested, containerized and published **before** any server exists.
   The server is sized and configured **from the product's known stack** (app + MySQL +
   Nginx + monitoring).

## Context & Problem

Route v2 provisioned the VPS before the application reached its final shape. That
inverted the dependency: server size, open ports, healthcheck target and backup target
would be decided before the product defined them. It also coupled progress to external
friction (Oracle account verification) that has nothing to do with learning the delivery
flow. The student's principle fixes the direction of derivation.

## The derivation chain (method)

```
Product scope & users
  → user-facing behaviors + data
  → API contract (endpoints, validation)
  → stack & dependencies (FastAPI, MySQL 8)
  → test strategy (unit + API, DB in CI)
  → quality tooling (pyproject: Black/Ruff/Flake8/MyPy)
  → security tooling (API key, Bandit, pip-audit, Trivy, gitleaks, Dependabot)
  → container (port, healthcheck, non-root, multi-arch)
  → pipeline stages (lint → test → security → build → smoke → publish)
  → infrastructure (server size, ports, volumes — Terraform)
  → operations (health, backups, monitoring, alerts)
  → portfolio evidence (README, diagram, demo)
```

## Traceability matrix (product → pipeline)

| Product requirement / risk | Derived element | Phase |
|---|---|---|
| API must respond and be verifiable | FastAPI, `/health`, smoke test | 9 |
| Deployment history must persist | MySQL 8, named volume | 9 |
| History must survive loss | `mysqldump` + off-site + restore drill | 13 |
| Writes must be protected | `X-API-Key`, CI secret, server `.env` | 9/12 |
| Code must be correct | pytest (unit + API), coverage ≥ 80 % | 9 |
| Code must be consistent/typed | Black/Ruff/Flake8/MyPy via `pyproject.toml` | 9 |
| Dependencies may carry CVEs | pip-audit, Dependabot, Trivy | 9 |
| Secrets may leak | gitleaks, `.gitignore`, pre-commit | 9 |
| Image must run on the free ARM server | buildx multi-arch (amd64+arm64) | 9/10 |
| Unverified code must never ship | PR gating, smoke test, immutable tags | 9 |
| Deploys must be reversible | tag-based rollback + runbook | 12 |
| Users need trusted HTTPS | Nginx/Caddy + Let's Encrypt + free hostname | 13 |
| Ops must know when it breaks | `/health` checks + Uptime Kuma + alerts | 14 |
| Pipeline's own deploys must be visible | CD writes to the journal; public timeline | 9/12 |
| Interview needs evidence | README v2, ADRs, demo, releases | 15 |

If a proposed tool has no row in this matrix, it does not enter the project.

## Alternatives Considered

- **Keep v2 order (VPS first)** — rejected: infra sized before the product, progress
  blocked by cloud-account friction, weaker narrative.
- **Build the app after deployment (v1 order)** — rejected already in ADR-0008
  (double hardening work).
- **Choose tools first, then find a use ("resume-driven development")** — rejected: it is
  exactly what this ADR forbids.

## Why This Option

- Every phase consumes the previous phase's output; nothing is built twice.
- The student can always answer "why does this exist?" with a product requirement.
- Progress on the product is independent of cloud-provider friction; the VPS simply
  arrives when the product is ready to be hosted.
- The matrix doubles as an interview artifact: it shows judgment, not tool collecting.

## Consequences

- **Renumbering:** old Phase 9 (VPS) becomes **Phase 10**; old Phase 10 (FastAPI) becomes
  **Phase 9**. Stage files rename accordingly: `stage-09-deploy-journal.md`,
  `stage-10-vps-provisioning.md`. References in ADR-0008/0009/0012/0013 were updated.
- VPS provider decision moves to Phase 10 (Stage 10 Session 0); it no longer blocks the
  start of the project.
- CI gains the MySQL service container (API tests), the smoke test and the journal
  write-back in CD — all derived from product requirements (ADR-0013/0015).
- The zero-cost rule (ADR-0005) is unchanged; the derived stack is entirely free.

## If It Disappeared

We would be back to choosing tools first and inventing reasons later — the exact
anti-pattern that makes junior portfolios look like tutorials.
