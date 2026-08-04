# Stages

## Index & Evidence Rules

**Project:** CI/CD Pipeline Labs

---

## Index

| Stage | Title | Phase | Status |
|---|---|---|---|
| 08 | [SSH & Remote Connections](stage-08-ssh-remote-connection.md) | 8 | 🔄 In progress |
| 09 | [VPS Provisioning](stage-09-vps-provisioning.md) | 9 | ⬜ Pending |

> More stages are created progressively — each one is written in detail only when we reach
> its phase (see `docs/execution-plan.md` for the full roadmap).

---

## Evidence Rules

Every stage produces **evidence** — proof that the work happened and can be reproduced.

### Screenshots

- One folder per stage: `screenshots/stage-08/`, `screenshots/stage-09/`, …
- Name files descriptively: `01-ssh-connect.png`, `02-keygen-output.png`, …
- Capture what matters (commands + output), not the whole screen.

### Command logs

- Save meaningful command output as text files under `screenshots/stage-NN/` when a
  screenshot is not practical.

### Reproducibility

- Another person must be able to follow the stage document and get the same result.
- Include every command with a one-line "why".

---

## Definition of Done (applies to every stage)

A stage is complete when **all** are true:

- [ ] All checklist items in the stage document are ticked.
- [ ] The **Report** section at the bottom of the stage is filled by the student.
- [ ] Evidence exists in `screenshots/stage-NN/`.
- [ ] ADR written if a meaningful decision was made.
- [ ] `session-log.md` has a new entry.
- [ ] `execution-plan.md` checkboxes + Current Status updated.
- [ ] Memory folder synced to `C:\Repo2`, committed and pushed to **both** GitHub and GitLab.
- [ ] The student can explain the stage back to the mentor (mentor validation passed).

---

## Stage Template

Every stage file follows `_template.md`. The template guarantees consistency, which makes
the repository easy to read for an interviewer and easy to resume for an AI.
