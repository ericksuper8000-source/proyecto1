# ADR-0004 — Docker Compose Early + Watchtower for CD Simulation

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 7 — Orchestration & CD Simulation (already completed)

---

## Decision

Docker Compose was introduced **early** (even with a single-service application) and
**Watchtower** was added to simulate continuous deployment. The stack runs locally and
auto-recreates the container when a new image is published.

## Context & Problem

The project had one container and could have been run with a single `docker run`. But the
goal was to learn how production environments are described and operated. Docker Compose
was introduced not because the app needed it, but because the *learning* needed it: the
mental model of "describe the desired state, then let the tools execute it" is the
foundation of Phases 11–12.

## Alternatives Considered

- **`docker run` only** — fastest, but teaches nothing about orchestration and gives no
  base for the future stack (app + database + Nginx).
- **Docker Compose early (chosen)** — one `docker-compose.yml` file that will grow with
  the project.
- **No CD simulation** — manual redeploys only; rejected because CD is part of the
  delivery lifecycle we are learning.

## Why This Option

- Compose documents the running state in a versioned file instead of a fragile manual
  command (infrastructure as code, even if small).
- Watchtower demonstrates the CD concept concretely: publish a new image → the running
  container is recreated automatically. This is exactly what the pipeline + server will
  do in Phase 11/12.
- It gave a safe, local way to understand container lifecycle, restart policies, and the
  difference between Compose (decides) and Engine (executes).

## Consequences

- The stack is described in `docker-compose.yml` (app + watchtower) with `restart: always`.
- Watchtower needs access to the Docker socket to detect and recreate containers.
- Production persistence (volumes) is intentionally *not* solved yet — it is addressed in
  Phase 12, when the need is real.

## If It Disappeared

The project would lose its local rehearsal ground for the deployment phases and the
compose file that later becomes the production stack.
