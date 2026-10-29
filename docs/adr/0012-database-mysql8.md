# ADR-0012 — Database: MySQL 8

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29, finding C8 (docs contradict each other): execution-plan said PostgreSQL while the student's learning path is MySQL. Fixes the contradiction permanently.

---

## Decision

The application database is **MySQL 8** (official Docker image). Backups use `mysqldump`
via a scheduled container/cron, with a documented restore drill (Phase 13).

## Context & Problem

The previous docs named PostgreSQL in Phase 13 while the student studies and practices
MySQL (fastapi + python + mysql stack). Both engines would satisfy this project's needs,
but the documentation must state one truth. Leaving it ambiguous means compose files,
env vars, backups and interview answers would keep drifting.

## Alternatives Considered

- **PostgreSQL** — valid; rejected because it adds learning friction with no benefit for
  this scope, and contradicts the student's established stack.
- **SQLite** — rejected: not production-shaped (no separate service, no real backup
  story).
- **MariaDB** — near-identical, valid fallback; rejected to keep 1:1 with the student's
  MySQL study path (migration later is trivial).

## Why This Option

- Matches the student's existing knowledge (MySQL + SQL + FastAPI with MySQL connectors).
- Official `mysql:8` image is multi-arch (arm64 included) — compatible with ADR-0010.
- `mysqldump` + cron is the simplest free backup that still demonstrates a real restore.

## Consequences

- Compose gains a `db` service (mysql:8) with a named volume in Phase 10 (dev) and
  Phase 12 (server).
- Env-based config: `MYSQL_DATABASE`, `MYSQL_USER`, `MYSQL_PASSWORD`, port 3306 internal
  only.
- Phase 13 backup job: daily `mysqldump` + off-site copy (free tier) + restore drill.
- All docs (spec, roadmap, stages) now say **MySQL 8** — PostgreSQL references removed.

## If It Disappeared

Switching to PostgreSQL later is possible (compose service + driver change), but the
project would lose the zero-friction alignment with the student's study path and force a
re-write of the backup/restore stage.
