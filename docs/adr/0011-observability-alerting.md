# ADR-0011 — Observability & Alerting Stack (zero-cost, self-hosted)

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29 — observability was 1/10 (a one-line mention of Uptime Kuma in Phase 12). Defines the full stack for the new Phase 14. Everything below is free software running on the existing VPS.

---

## Decision

Phase 14 builds a self-hosted observability stack on the VPS:

- **Uptime Kuma** — availability checks on `GET /health` (public status page).
- **cAdvisor + Prometheus + Alertmanager** — container/host metrics and alert routing.
- **Grafana** — dashboards (node + containers), screenshotted as portfolio evidence.
- **Alerts via Telegram bot API** (free): app down, disk > 80 %, CPU > 90 %, container
  restart loop.
- **Logs:** `json-file` driver with rotation limits + documented where-to-look runbook;
  **Loki is deferred** (stretch goal, avoids over-complexity at junior level).

## Context & Problem

A pipeline that deploys without observing is half a story. Interviewers ask: "how do you
know it works at 3 a.m.?" The project needs evidence of alerting and dashboards, and the
`/health` endpoint from ADR-0008 is the hook. The zero-cost rule forbids paid SaaS
monitoring (Datadog, New Relic, paid Grafana Cloud).

## Alternatives Considered

- **Paid SaaS monitoring** — rejected: violates ADR-0005.
- **Uptime Kuma only** — rejected: uptime is not metrics; no capacity/resource visibility.
- **Grafana Cloud free tier** — acceptable fallback if the VPS lacks resources; not the
  primary choice because self-hosting demonstrates more and stays fully under our control.
- **Loki now** — rejected: adds a stack layer before the basics are solid; deferred.

## Why This Option

- Every component is open source, free, and runs in the same compose stack as the app.
- Telegram is the free alert channel that reaches the student's phone instantly.
- The dashboard + the received alert are concrete, screenshot-able portfolio evidence
  that no tutorial repository has.

## Consequences

- Phase 14 adds 4–5 containers (ARM images verified per ADR-0010); the A1 free shape
  (2–4 OCPU / 12–24 GB) comfortably fits.
- A Telegram bot token becomes a server secret (`.env`, 600 permissions, never in Git).
- One required drill: kill the app → alert arrives on the phone → evidence logged.
- Prometheus scrape config and Grafana dashboards are versioned in the repo
  (`monitoring/`).

## If It Disappeared

The deployment would be blind: no proof of availability, no alert when it breaks — the
portfolio would lose its strongest "production story".
