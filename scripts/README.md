# Scripts

## Purpose

This folder holds every script created during the stages: pipeline YAML examples, Docker
files, deployment scripts, server setup scripts, and any automation produced while
learning the delivery lifecycle.

## Conventions

- One folder per stage when a stage produces several scripts: `stage-10/`, `stage-11/`, …
- Every script is **reproducible**: it documents what it does and why it exists
  (the "why" in a short header or in the stage report).
- Scripts never contain secrets. Secrets live in environment variables, `.env` files
  (never committed), or CI secrets.
- A script is committed with the stage that created it, as part of the same meaningful
  commit.

> Scripts are written **after** the manual process is understood (see "Understand before
> automating" in `docs/project-specification.md`).
