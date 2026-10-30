# ADR-0009 — Infrastructure as Code: Terraform + cloud-init, Ansible for bootstrap

**Status:** Accepted
**Date:** 2026-10-29
**Context:** Audit 2026-10-29 — Phase 10 (VPS provisioning) is redefined from "manual Oracle console clicks" to infrastructure-as-code. Builds on ADR-0005 (zero cost). Renumbered by ADR-0016 (v2.1: product first, then infrastructure).

---

## Decision

The VPS is provisioned **with Terraform** (infrastructure as code) plus **cloud-init** for
first boot, and configured **with Ansible** (reproducible bootstrap). Everything is free
software. Provider rule: **Oracle Cloud Always Free is the default**; if a Hetzner VPS is
*already owned*, prefer it (no incremental cost, simpler provider, ARM/x86 choice).

## Context & Problem

The old plan created the server by clicking through the Oracle console. That produces a
server, but not a portfolio artifact: nothing is reproducible, reviewable, or re-creatable,
and "I clicked buttons" is not an interview answer. The audit (finding: IaC absent, 0/10)
identified Terraform/Ansible as the single biggest missing differentiator for a DevOps
Junior. The zero-cost rule (ADR-0005) stays absolute.

## Alternatives Considered

- **Manual console provisioning** — rejected: not reproducible, not versionable.
- **Pulumi / CDK** — rejected: smaller community, Terraform is the interview standard and
  the best-documented free option.
- **Ansible-only provisioning** — rejected: Ansible is weak at creating cloud VMs;
  Terraform + cloud-init is the standard split (infra vs config).
- **Terraform + Ansible both for everything** — rejected: cloud-init covers first boot
  cheaply; Ansible takes over the *configuration* work (users, firewall, Docker) in
  Phase 11.

## Why This Option

- `terraform plan/apply/destroy` makes the server reproducible, reviewable and free to
  recreate — the difference between a tutorial and an engineering project.
- cloud-init (built into Ubuntu images, free) installs the SSH key and basic hardening at
  first boot, no agent required.
- Ansible (free, agentless over SSH) turns Phase 10/11 server setup into one idempotent
  playbook — another interview-ready artifact.
- Both tools cost $0 and run on the student's Windows host.

## Consequences

- New repo structure: `infra/` (Terraform HCL files) + `ansible/` (playbook) added in
  Phase 9/11.
- Provider decision is a **documented gate** at the start of Stage 10 (Oracle needs card
  verification but no charge; Hetzner only if already owned). The server is sized from
  the product's known stack (ADR-0015/0016): app + MySQL + Nginx + monitoring.
- Oracle ARM A1 shape forces multi-arch images → ADR-0010.
- New competencies: HCL, state files, providers, plan/apply lifecycle, idempotency.

## If It Disappeared

The server would exist only as long as nobody touches the console; the portfolio would
lose the artifact interviewers ask about first: "can you create your infrastructure from
code?"
