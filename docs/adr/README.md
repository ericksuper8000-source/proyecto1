# Architecture Decision Records (ADR)

## Why ADRs exist

Every meaningful technical decision in this project is recorded as an ADR. An ADR
answers five questions (Law of Traceability in `docs/mentor-constitution.md`):

- Why does it exist?
- What problem does it solve?
- What alternatives existed?
- Why was this solution chosen?
- What would happen if it disappeared?

Interviewers love ADRs: they prove you did not copy a tutorial — you made **decisions**.

## When to write one

Write an ADR when you (or the mentor) make a decision that:

- changes how the project works (e.g., moving Git earlier),
- introduces or removes a tool (e.g., Docker, Watchtower, Oracle Cloud Free Tier),
- chooses between valid alternatives (e.g., GitHub Actions vs GitLab CI),
- has lasting consequences for the repository or the server.

Do **not** write an ADR for routine tasks ("installed a text editor").

## Index

| # | Status | Title |
|---|---|---|
| 0001 | Accepted | [Version control from day one](0001-version-control-from-day-one.md) |
| 0002 | Accepted | [Mirror repositories on GitHub and GitLab](0002-mirror-repos-github-gitlab.md) |
| 0003 | Accepted | [Multi-registry image publishing](0003-multi-registry-publishing.md) |
| 0004 | Accepted | [Docker Compose early + Watchtower for CD simulation](0004-docker-compose-early-and-watchtower.md) |
| 0005 | Accepted | [Zero-cost cloud strategy](0005-zero-cost-cloud-strategy.md) |
| 0006 | Accepted | [English public documentation](0006-english-documentation.md) |
| 0007 | Accepted | [Single image publisher (GitHub Actions), validation-only GitLab CI](0007-single-image-publisher.md) |

## Naming & workflow

1. Copy `_template.md` → `NNNN-short-description.md` (zero-padded number).
2. Fill in the sections.
3. Update the index table above.
4. Reference the ADR from the stage document where the decision happens.
5. It becomes part of the session commit.

> Decisions can be **Proposed → Accepted → Superseded**. Superseding an ADR requires a
> new ADR that references the old one.
