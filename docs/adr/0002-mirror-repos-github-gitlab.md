# ADR-0002 — Mirror Repositories on GitHub and GitLab

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning / Phase 3 (already completed)

---

## Decision

The project is published as a **mirrored pair**: the same repository is pushed to both
GitHub (`proyecto1`) and GitLab (`repo2`). The canonical working copy lives in `C:\Repo2`;
both platforms receive every push.

## Context & Problem

Companies use different platforms and different CI ecosystems. The project deliberately
practices **multi-platform delivery**: GitHub Actions and GitLab CI run the same pipeline.
Hosting the code on both platforms is the natural home for that comparison, and provides
redundancy — if one platform disappears, the project survives on the other.

## Alternatives Considered

- **GitHub only** — simpler, but loses GitLab CI experience and platform breadth.
- **GitLab only** — same, reversed.
- **Both, mirrored (chosen)** — one working copy, two remotes, minimal extra effort.

## Why This Option

Mirroring costs almost nothing (one extra remote) and doubles the portfolio surface.
Both CI systems are already in use, so both accounts are needed regardless.

## Consequences

- `git remote -v` shows two remotes; every push goes to both.
- Both repositories stay public and in sync.
- Pipelines are developed and compared on both platforms.

## If It Disappeared

The portfolio would lose the multi-platform story and the direct GitHub Actions vs
GitLab CI comparison that interviewers value.
