# ADR-0003 — Multi-Registry Image Publishing

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 6 — Registries & Image Publishing (already completed)

---

## Decision

The **same** Docker image is published to **three** container registries from a single
pipeline: Docker Hub (`erickdev8/mi-app`), GitHub Container Registry
(`ghcr.io/ericksuper8000-source/mi-app`), and GitLab Container Registry
(`registry.gitlab.com/ericksuper80-group/repo2`).

## Context & Problem

Images built in a pipeline disappear when the runner finishes. They need a permanent
home a server can pull from. We also wanted to practice multi-platform delivery and avoid
dependence on a single provider.

## Alternatives Considered

- **Single registry (e.g., only Docker Hub)** — simplest, but no redundancy and less
  platform experience.
- **Multiple registries (chosen)** — one build, three `docker push` commands. Same image,
  three storage locations.

## Why This Option

The image is built once and tagged three times. This demonstrates: how registries work,
how to authenticate against each (tokens, `--password-stdin`), and how to make a server
independent of any single vendor. It is a realistic pattern for teams that mirror images
across cloud providers.

## Consequences

- The pipeline builds once and pushes three tags.
- Registry credentials live as CI secrets, never in the repository.
- A future server can pull from any of the three.

## If It Disappeared

The project would depend on one provider for image distribution — losing redundancy and
the multi-platform experience.
