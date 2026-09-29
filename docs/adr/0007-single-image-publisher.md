# ADR-0007 — Single Image Publisher (GitHub Actions), Validation-Only GitLab CI

**Status:** Accepted
**Date:** 2026-09-29
**Context:** Audit session (Session 04) — follow-up to ADR-0002 (mirror repos) and ADR-0003 (multi-registry publishing)

---

## Decision

1. **GitHub Actions is the only pipeline that builds and publishes the image.**
   One `docker build`, then push to the three registries (ADR-0003 stays true — the image
   still lives in all three).
2. **GitLab CI is validation-only** (`lint` + `test` + `security`). The `docker` publish
   job was removed from `.gitlab-ci.yml`. GitLab keeps its role as code mirror/storage
   (and still *receives* the registry copy of the image, published there by GitHub).
3. **Docker Hub is the single consumption registry** — `docker-compose.yml` (and the
   future VPS pull) use `erickdev8/mi-app:latest`. GHCR and the GitLab Registry are
   archives/redundancy, not deploy sources.

## Context & Problem

The audit (finding F-02) aligned both pipelines so each pushed to all three registries.
That symmetry required GitLab to push to GHCR, which needs a **GitHub PAT** stored as
GitLab CI variables — credentials only the student's GitHub account can mint (platform
boundary: `GITHUB_TOKEN` exists only inside GitHub Actions).

The student then defined the desired architecture explicitly: build once, publish from
GitHub to the three registries, consume from one registry, and keep GitLab purely as a
storage mirror. The cross-platform PAT became unnecessary.

## Alternatives Considered

- **Symmetric publishers (both pipelines push to 3 registries)** — maximum parity between
  platforms, but requires a cross-platform PAT + 2 GitLab variables, extra secret to
  rotate, and two places that can publish (who owns the image?).
- **Single publisher on GitHub (chosen)** — one build, three pushes, zero extra
  credentials; GitLab stays useful for validation practice (`stages`/`jobs` per the
  learning roadmap).
- **Disable GitLab CI entirely** — simplest, but loses the GitLab CI learning objectives.

## Why This Option

- **Single source of truth for publishing:** the image exists because one job built it,
  once, and copied it everywhere.
- **Zero cross-platform secrets:** no PAT, no `GHCR_USERNAME`/`GHCR_TOKEN` variables.
- **Clear ownership:** GitHub publishes, GitLab validates and stores, Docker Hub serves.
- Keeps GitLab pipeline alive for learning without giving it publishing power.

## Consequences

- Publishing availability depends on GitHub Actions (acceptable: the registry *copies*
  remain pullable even if GitHub CI is down).
- GitLab no longer practices Docker-in-Docker builds — that experience lives in GitHub.
- If any of the three pushes in the GitHub `docker` job fails, the job fails (pipeline
  red) — intentional, so the three registries never silently diverge.
- A future server pulls only from Docker Hub; switching registries = one compose line.

## If It Disappeared

Reverting means restoring the GitLab `docker` job (symmetric publishing) — which
reintroduces the PAT requirement, or documenting the platforms' asymmetry elsewhere.
