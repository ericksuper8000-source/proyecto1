# ADR-0010 — Multi-Architecture Images (linux/amd64 + linux/arm64)

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29, finding C1 (blocking): GitHub runners build `linux/amd64`, but the Oracle Always Free shape with usable resources (A1.Flex) is **ARM64**. Follows ADR-0009.

---

## Decision

All images are built as **multi-arch** (one manifest covering `linux/amd64` and
`linux/arm64`) using Docker Buildx + QEMU in GitHub Actions. Compose files never pin a
single platform.

## Context & Problem

A `docker build` on GitHub Actions produces an amd64 image. Running it on an Oracle A1.Flex
(ARM) instance fails with `exec format error`. The alternative x86 free shape
(E2.1.Micro) has 1/8 OCPU and 1 GB RAM — too small for app + MySQL + Nginx + monitoring.
Therefore: either we build for ARM, or the free-tier server cannot host the final stack.

## Alternatives Considered

- **x86-only VPS shape (E2.1.Micro)** — rejected: 1 GB RAM cannot hold the Phase 13/14
  stack.
- **Separate images per architecture** — rejected: two names, two compose files, drift;
  manifest lists are the industry standard.
- **Emulate the app on the server** — rejected: slow, fragile, defeats Docker.
- **amd64 VPS elsewhere (paid)** — rejected: violates ADR-0005 (unless Hetzner is already
  owned, see ADR-0009).

## Why This Option

- `docker/setup-buildx-action` + `docker/setup-qemu-action` are free official GitHub
  Actions; the change is ~4 lines in the pipeline.
- One image name, three registries, both architectures: the server pulls the right
  variant automatically.
- Multi-arch is a real-world skill and a visible portfolio differentiator.

## Consequences

- Docker build step moves to Buildx (QEMU emulation for arm64; slower builds, ~2–3 min).
- Registries store manifest lists (both variants under one tag).
- MySQL 8 and monitoring images must also be multi-arch — official images already are;
  verify each new service image in Phase 13/14.
- Dockerfile stays unchanged; the CI workflow gains a `platforms:` argument.

## If It Disappeared

The free ARM server cannot run the app — the project would be forced into the 1 GB x86
shape or a paid server, breaking either the stack or the zero-cost rule.
