# ADR-0014 — Public Repository Curation (portfolio presentation)

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29 findings C6, C8, C12 and the structural finding: ~287 KB of
internal documentation vs ~45 lines of application code, publicly exposed.

---

## Decision

The **public** GitHub repository presents only portfolio-grade material. Internal
AI-process artifacts move out of the public mirror:

1. **Public (stays):** README v2 (one-liner, mermaid architecture diagram, stack,
   quickstart, operations runbook, demo link, CI badges), `LICENSE` (MIT), `CHANGELOG.md`,
   git tags + GitHub Releases, ADRs, stage reports, `infra/`, `ansible/`, `monitoring/`.
2. **Moves to a private repo (or `docs-internal/` excluded from the public mirror):**
   `AGENTS.md`, `docs/session-log.md`, `docs/mentor-constitution.md`,
   `INSTRUCCIONES SESION DIARIA - IA.txt`, delivery-story internal notes. The memory
   folder on `E:` keeps being the working copy (already outside Git).
3. **Cleanup:** remove `nuevo.py` (practice noise); rename the GitHub repo to
   `ci-cd-pipeline-labs` (GitHub renames are free and preserve redirects); make the
   GitLab mirror **public with the same curation** (or stop calling it a public mirror —
   today it is private and invisible, contradicting ADR-0002's story).
4. **Evidence:** real screenshots/GIF/video (pipeline green, registries, `terraform
   plan`, HTTPS, dashboards, alert received, restore drill) replace `.txt` notes.

## Context & Problem

An interviewer landing on the repo today sees an operating manual for an AI mentor, a
93 KB session diary, a README that mentions `C:\Repo2`, and a GitLab mirror that is
actually private. The documentation-to-code ratio signals "process theater" regardless of
the real learning behind it. The README is a story, not a project README (no quickstart,
no architecture, no demo).

## Alternatives Considered

- **Leave everything public** — rejected: internal scaffolding dilutes the portfolio and
  exposes the AI-driven process.
- **Delete internal docs** — rejected: they are the project's memory; they move, not die.
- **Rewrite git history (filter-repo)** — optional stretch; not required because the
  damage is noise, not secrets (verified: no credentials in history).

## Why This Option

- Curated public repos are what hiring managers actually read; ADRs + stage reports alone
  tell the whole story without the scaffolding.
- Zero cost: private repo on GitHub is free; rename is free; MIT license is free.
- The internal protocol keeps working unchanged — it simply lives out of the public eye.

## Consequences

- Phase 15 has a dedicated checklist for the curation; the public repo is re-packaged
  **once**, at the end.
- `README v2` is written for a stranger who wants to run and understand the project in
  5 minutes.
- The GitLab mirror decision (public curated vs private) is recorded in the session log
  when resolved.

## If It Disappeared

The public repo stays a confusing mix of diary and code — the strongest learning
project on the profile would keep reading like an internal notebook.
