# Stage 10 — VPS Provisioning with Terraform + cloud-init

> **Phase:** Phase 10 — VPS Provisioning (route v2.1, sized from the product)
> **Estimated duration:** 3–4 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 09 complete (Deploy Journal built, tested, containerized and
> published). ADR-0009 (IaC), ADR-0005 (zero cost), ADR-0010 (multi-arch),
> ADR-0016 (product-first: the product's stack sizes the server).

---

## Objective

Provision the **first real server from code** with Terraform + cloud-init —
reproducible, reviewable, free — sized from the known product stack (Deploy Journal +
MySQL + Nginx + monitoring), and connect over SSH understanding every choice.

## Scenario (real world)

*"The product is ready and published. Now create the server it will run on — in a way
anyone on the team can review and recreate, and with exactly the resources the product
needs (no more, no less)."* Clicking through a console is not an answer.

## Concepts (why first)

- **Product-derived infrastructure (ADR-0016):** the stack is known (app + DB + proxy +
  monitoring) → the server shape is chosen from that fact, not guessed.
- **Infrastructure as Code:** the server is a set of versioned files (`infra/`).
  Provider, resources, state; `plan` shows, `apply` creates, `destroy` removes.
- **cloud-init:** first-boot hook built into Ubuntu images: user, SSH key, disabled
  password auth, unattended-upgrades.
- **Zero-cost decision (ADR-0005/0009):** Oracle Always Free (A1.Flex ARM — card for
  identity verification only, no charge) or an **already-owned Hetzner VPS** (no
  incremental cost). Decision gate at Session 0.
- **ARM consequence:** A1.Flex is ARM64; our images are multi-arch (ADR-0010), so they
  run there without `exec format error`.
- **Budget alert:** a free $0-threshold alert proves "nothing generates a bill" is
  watched, not hoped.

## Pre-flight

- [ ] Stage 09 complete (product + images published).
- [ ] ADR-0009 read; provider decision made (Oracle vs owned Hetzner) and logged.
- [ ] A card available for Oracle identity verification (no charge) — or Hetzner path.
- [ ] Terraform CLI installed locally (free).
- [ ] Zero-cost rule understood: **nothing that can generate a bill** (ADR-0005).

## Checklist

### Session 0 — Decision gate & Terraform

- [ ] Read ADR-0009 + ADR-0005 + ADR-0016; decide provider; record decision + reason
- [ ] Install Terraform CLI; verify `terraform -version`
- [ ] Explain: provider / state / resource / plan / apply / destroy

### Session 1 — Account & quotas

- [ ] Create the cloud account (Always Free — or log into owned Hetzner)
- [ ] Understand "Always Free" vs trial credits; record live limits
- [ ] Configure a **budget alert** (Oracle $0 threshold / Hetzner project limit) —
      evidence screenshot

### Session 2 — The `infra/` module

- [ ] `infra/main.tf`: provider configuration
- [ ] Network: VCN/subnet (Oracle) or network/firewall (Hetzner): ingress 22/80/443
- [ ] Instance: Ubuntu LTS; shape sized from the product stack (A1.Flex ARM on Oracle)
- [ ] **cloud-init** user-data: `ubuntu` user, `id_ed25519_vps.pub`, disable password
      auth, unattended-upgrades
- [ ] Outputs: public IP
- [ ] `terraform plan` (review) → `terraform apply` → server Running

### Session 3 — First contact (read-only) + reproducibility drill

- [ ] `ssh mi-vps` works (alias in `~/.ssh/config`)
- [ ] Observe: `whoami`, `cat /etc/os-release`, `free -h`, `nproc`, `df -h`, `ip a`
- [ ] Reproducibility drill: `terraform destroy` → `terraform apply`
- [ ] Verify `unattended-upgrades` active (cloud-init did its job)

### Close-out

- [ ] Mentor Questions answered in the Report
- [ ] Evidence in `screenshots/stage-10/` (plan/apply output, budget alert, ssh login)
- [ ] Session log entry; execution-plan Phase 10 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. Why Terraform instead of clicking the console?
2. What does `terraform state` remember, and why is it stored?
3. How did the product's stack determine the server size (ADR-0016)?
4. What does cloud-init do before you ever log in?
5. Why did we choose this provider under the zero-cost rule? What would generate a bill?
6. Why does the ARM shape force multi-arch images (ADR-0010)?
7. What proves that our server is "code" and not a manual artifact?

---

## Report (student fills after the session)

### What I did

### How it works / why

### Commands I used

| Command | Why I used it |
|---|---|
| `terraform init` | Download the provider plugin |
| `terraform plan` | Preview changes before applying |
| `terraform apply` | Create the real infrastructure |
| `terraform destroy` | Prove the server is disposable code |
| `ssh mi-vps` | First real connection (Stage 08 in action) |
| `free -h` / `nproc` / `df -h` | Observe the free-tier resources |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> 5–10 sentences: what a VPS is now that you have one *created from code*, and why the
> reproducibility drill matters.

### Evidence

- [ ] `terraform plan/apply/destroy` outputs saved
- [ ] Budget alert configured (screenshot)
- [ ] SSH first connection screenshot
- [ ] Private key stored securely, **not** committed
- [ ] Session log + execution plan updated
- [ ] Memory folder synced to `C:\Repo2`

> 🚀 **Next:** Stage 11 — Linux Server Administration + Ansible.
