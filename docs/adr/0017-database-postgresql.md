# ADR-0017 — Database: PostgreSQL

**Status:** Accepted (supersedes ADR-0012)
**Date:** 2026-11-04
**Context:** Student direction (2026-11-04) — the current study path around FastAPI + Python now centers on PostgreSQL; the project moves the Deploy Journal database from MySQL 8 (ADR-0012) to PostgreSQL.

---

## Decision

The application database is **PostgreSQL** (official Docker image, major version 16 at planning time).

## Context & Problem

ADR-0012 (2026-10-29) declared **MySQL 8** as the database for the Deploy Journal, resolving a prior documentation contradiction (execution-plan referenced PostgreSQL while the learning path was MySQL). The student has since shifted the current study focus to **PostgreSQL**, and the product decision must follow the student's validated direction.

## Alternatives Considered

- **Keep MySQL 8** — rejected per student direction (2026-11-04).
- **PostgreSQL** — chosen as the new database for the Deploy Journal.

## Why This Option

- Aligns with the student's current learning path (FastAPI + Python + PostgreSQL + DevOps).
- Keeps the product-first derivation (ADR-0016): the stack is chosen because the product requires it, not the other way around.

## Consequences

- Phase 9 (Deploy Journal) product stack: **Python + FastAPI + PostgreSQL**.
- Data model uses PostgreSQL types (`BIGSERIAL`, `CHECK` constraints, `TIMESTAMPTZ`, ...).
- Local compose gains a `postgres` service (official image, named volume, internal port 5432, `POSTGRES_*` env vars).
- Backups: `pg_dump` / restore instead of `mysqldump`.
- CI: PostgreSQL service container for API tests (Phase 9, Session 3).
- ADR-0012 is **superseded** by this ADR.

## If It Disappeared

The project would need to re-justify the database choice; the migration path back to MySQL would be a new decision.
