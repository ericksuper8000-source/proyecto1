# ADR-0008 — FastAPI + Database BEFORE Deployment (phase reordering)

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29 (technical rival review) — supersedes the original phase order in `execution-plan.md` v1 (FastAPI was Phase 13, after deployment and hardening).

---

## Decision

The application evolves into a **FastAPI service with a database and a health endpoint
(Phase 9)** *before* any server provisioning, deployment, or production hardening work.
The original order (deploy a print-loop script first, evolve the app later) is discarded.

## Context & Problem

The current application (`Principal.py`) is a loop that prints every 5 seconds. It has no
port, no endpoint, no healthcheck. The old plan deployed and hardened this toy first
(Nginx, HTTPS, monitoring, backups) and then replaced the entire application with FastAPI +
database — which would force redoing the reverse proxy, the compose stack, the healthchecks
and the monitoring targets. Double work, double documentation, double risk.

A deployment is only real when it serves something verifiable: an HTTP endpoint.

## Alternatives Considered

- **Keep the original order** — rejected: hardening a print loop teaches nothing and is
  discarded afterwards.
- **Skip FastAPI entirely** — rejected: the portfolio needs a real service with `/health`
  for monitoring, tests and reverse proxy work.
- **FastAPI after deployment but before hardening** — considered; rejected because the
  deployment itself (compose, ports, persistence) would still be built twice.

## Why This Option

- The pipeline is born from the application (permanent principle): the app defines the
  stack, and the stack defines the deployment. The app must reach its final shape first.
- `GET /health` exists **before** monitoring and Nginx need it.
- API tests (TestClient) strengthen the CI gate before the first real deploy.
- Production hardening is done **once**, on the final architecture.

## Consequences

- New phase order (v2.1, ADR-0016): 9 Deploy Journal (FastAPI+MySQL) → 10 Terraform VPS →
  11 Linux+Ansible → 12 Deploy+CD → 13 Hardening+HTTPS+Backups → 14 Observability →
  15 Portfolio.
- The VPS is provisioned in Phase 10 but nothing is deployed to it until Phase 12.
- Compose grows (app + db) before the first server deployment.
- `requirements.txt` (runtime) and `requirements-dev.txt` (pinned tools) split.

## If It Disappeared

We would go back to deploying and hardening a script that prints numbers — twice the work
and a portfolio artifact that proves almost nothing.
