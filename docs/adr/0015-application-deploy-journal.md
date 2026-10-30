# ADR-0015 — Application Definition: Deploy Journal

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Route v2.1 — the product is defined before any implementation. Satisfies
ADR-0016 (product-first): the pipeline is assembled around this product, not the other
way around. Supersedes the undefined "evolve the app later" placeholder.

---

## Decision

The application is **Deploy Journal** — a small internal deployment-history service.
Every deployment of this project's pipeline records itself in the app; a public page
shows the timeline. Stack: **Python + FastAPI + MySQL 8**.

## Context & Problem

The project needs a real product to justify a real pipeline. The product must be small
(pipeline is the star), non-generic (portfolio), and must exercise MySQL, FastAPI and
Python meaningfully — with a `/health` endpoint that later phases (Nginx, CD, monitoring,
backups) genuinely need.

## Product scope (MVP)

**Users:** the pipeline (writer, via API key) and the developer/visitor (reader).

Functional requirements:

- **FR1** — Record a deployment: version (immutable tag), environment, status
  (`success` / `failed` / `rollback`), message, author.
- **FR2** — List deployments (newest first, limit, filter by environment).
- **FR3** — Get one deployment by id.
- **FR4** — Stats: total deployments, last deployment, success rate, per environment.
- **FR5** — Health: application + **database connectivity**.
- **FR6** — Public timeline page (server-rendered HTML; no frontend framework).
- **FR7** — Writes are protected by an `X-API-Key` header.

Non-functional requirements:

- **NFR1** — Small: ~200–300 lines of Python + one HTML template.
- **NFR2** — Stateless app + stateful MySQL 8 with a named volume.
- **NFR3** — Contract-first: OpenAPI docs (`/docs`) are the source of truth.
- **NFR4** — Testable: unit + API tests; `/health` covers the DB path.
- **NFR5** — Container-ready: port 8000, non-root user, `HEALTHCHECK`.
- **NFR6** — Backup-worthy data: the deployment history is what gets dumped/restored.

Out of scope (deliberately): user accounts/auth UI, multi-tenant, notifications,
frameworks, editing/deleting history, analytics dashboards, Kubernetes.

## Data model

```
environments(id PK, name UNIQUE)            -- seeded: dev, prod
deployments(
  id PK,
  version VARCHAR(64) NOT NULL,             -- immutable tag
  environment_id FK → environments(id),
  status ENUM('success','failed','rollback') NOT NULL,
  message TEXT NULL,
  deployed_by VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX(environment_id), INDEX(created_at)
)
```

## API contract (v1)

| Method | Path | Purpose | Auth |
|---|---|---|---|
| GET | `/health` | app + DB status | public |
| GET | `/` | deployment timeline (HTML) | public |
| GET | `/api/deployments` | list (limit/filter) | public |
| GET | `/api/deployments/{id}` | detail | public |
| GET | `/api/stats` | totals / last / success rate | public |
| POST | `/api/deployments` | record a deployment | `X-API-Key` |

## How the pipeline uses it (the loop)

1. CD deploys the new image (immutable tag) and verifies `GET /health`.
2. CD calls `POST /api/deployments` with the tag, environment and status.
3. The public timeline shows the deployment — **the pipeline's output becomes the
   product's input**.
4. A rollback is recorded with `status = rollback`, so the journal tells the operation's
   history.

## Alternatives Considered

- **Mini incident tracker** — valid DevOps theme; rejected: duplicates Uptime Kuma's
  status page, adds an incident lifecycle state machine, weaker direct integration with
  the deploy flow.
- **Job application tracker** — useful personally; rejected: generic CRUD disconnected
  from the delivery flow — it would teach FastAPI/MySQL but nothing about deployments.
- **Keep the print-loop script** — rejected: nothing to deploy, nothing to monitor,
  nothing to back up.

## Why This Option

- Small, unique, and it makes the pipeline legible: every later phase has a concrete
  reason to exist (healthcheck, DB volume, backups, monitoring, CD write-back).
- Exercises MySQL for real (schema, joins/aggregations, persistence, restore) and FastAPI
  for real (validation, OpenAPI, API key, DB dependency).
- Produces the best portfolio demo: `git push` → URL timeline updates live.

## Consequences

- Phase 9 implements the product (data model → API → tests → container → CI/CD v2).
- The MySQL service enters compose in Phase 9 (dev) and Phase 12 (server).
- The API key becomes a real secret (CI + server `.env`), covered by ADR-0013.
- `/health` with a DB check becomes the monitoring target (ADR-0011) and the CD
  post-deploy gate.

## If It Disappeared

The project would go back to deploying a script with no user-facing behavior — the
pipeline would be a demo of YAML instead of a delivery system for a product.
