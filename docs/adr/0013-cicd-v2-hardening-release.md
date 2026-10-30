# ADR-0013 — CI/CD v2: hardening, release strategy, and supply-chain checks

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29 findings C2, C4, C5, C9, C10, C11. Replaces several implicit
defaults of the Phase 4 pipeline with explicit rules. All tools free.

---

## Decision

1. **Publishing gate:** the `docker` job runs only on `push` to `develop` and on `tags`;
   `:latest` is pushed only from tagged releases. PR builds validate but never publish.
2. **Reproducible CI:** dev tools pinned in `requirements-dev.txt` (audited with
   pip-audit); one `pyproject.toml` harmonizes Black (line-length 88), Flake8
   (`max-line-length = 88`, ignore E203/W503), Ruff and MyPy.
3. **Container smoke test:** after build, the pipeline runs the image and curls `GET
   /health` — "build OK" must mean "it runs".
4. **CI hygiene:** explicit `permissions:` (least privilege), pip cache in
   `setup-python`, `concurrency` groups, `timeout-minutes` on every job.
5. **Supply chain:** Trivy image scan (fail on HIGH/CRITICAL), Dependabot
   (actions/pip/docker), `gitleaks` secret scanning, `pre-commit` hooks locally.
6. **Deployment strategy:** the server consumes the **immutable SHA tag**, never
   `:latest`; CD deploys over SSH with a scoped deploy key, runs a post-deploy
   healthcheck, and rollback = redeploy the previous tag (documented runbook + one
   practiced drill).

## Context & Problem

Findings from the audit: the docker job ran on pull requests and overwrote `:latest` with
unmerged code (C2); Flake8 79 vs Black 88 will break as soon as code grows (C4); `pip
install` without versions is a time bomb (C5); images were never executed by CI (C9);
missing permissions/cache/timeouts (C10); no image scanning or secret scanning (C11).

## Alternatives Considered

- **Keep current pipeline** — rejected: real bugs (PR publishing) and latent failures
  (unpinned tools).
- **Blue-green / canary deploy** — rejected for now: single-node free VPS; documented
  rollback-by-tag is the right size for junior scope. Revisit if a second node ever
  exists.
- **Renovate instead of Dependabot** — valid; Dependabot chosen (native to GitHub, zero
  setup).

## Why This Option

- Every rule closes a concrete, observed failure mode — not cargo cult.
- All tools are free and run inside GitHub Actions or locally.
- Immutable tags + healthcheck + rollback drill is exactly the "production delivery"
  story a junior portfolio needs to defend.

## Consequences

- Phase 9 implements items 1–5 alongside the Deploy Journal product; Phase 12 implements 6.
- `:latest` becomes a release-only pointer; local CD simulation (Watchtower, ADR-0004)
  stays local-only.
- Git tags + GitHub Releases become part of the workflow (semantic versions `v0.x.0`).
- Secrets scopes documented (Docker Hub PAT write-only, GitLab `write_registry`, deploy
  key read-only) + rotation note.

## If It Disappeared

PRs would publish unmerged images again, tooling versions would float, and deployment
would have no verified artifact and no way back — the exact failure modes this ADR exists
to prevent.
