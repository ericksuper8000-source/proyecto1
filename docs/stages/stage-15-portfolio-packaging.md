# Stage 15 — Portfolio & Interview Packaging

> **Phase:** Phase 15 — Portfolio (route v2)
> **Estimated duration:** 2–3 sessions
> **Status:** ⬜ Pending
> **Prerequisites:** Stages 09–14 complete. ADR-0014 (public curation).

---

## Objective

Turn the project into a **public, curated, demo-able story** that a stranger
understands in 5 minutes — and that the student can defend line by line.

## Scenario (real world)

A recruiter opens your GitHub profile with 30 other candidates. You have one minute
of their attention before they decide whether to invite you to a technical interview.

## Concepts (why first)

- **Curation (ADR-0014):** the public repo shows the product, not the kitchen. ADRs and
  stage reports stay public (they are the story); the AI session diary and operating
  manuals move to a private place.
- **The README is the demo:** one-liner, mermaid architecture diagram, stack, quickstart,
  operations runbook, live URL, CI badges. A stranger must be able to run it.
- **Evidence over claims:** screenshots/GIF/video of the real system (pipeline green,
  terraform plan, HTTPS, dashboards, alert received, restore drill).
- **Releases & tags:** semantic versions + GitHub Releases give the "product" signal;
  `CHANGELOG.md` tells the story over time.
- **The defense:** every "why" already exists in the ADRs (0001–0014) and the learning
  roadmap. The rehearsal is connecting them in one flow.

## Checklist

### Session 1 — Public README v2 & repository polish

- [ ] README v2: one-liner, mermaid architecture diagram, stack table, quickstart
      (run tests → build → deploy), operations (deploy/rollback/backup/monitoring),
      live demo link, CI badges
- [ ] `LICENSE` (MIT) + `CHANGELOG.md`
- [ ] Git tags (`v0.1.0` …) + GitHub Releases for each tag
- [ ] Remove `nuevo.py`; rename the repo to `ci-cd-pipeline-labs` (free, redirects
      preserved)

### Session 2 — Curation (ADR-0014)

- [ ] Move internal docs out of the public repo: `AGENTS.md`, `session-log.md`,
      `mentor-constitution.md`, session instructions, internal delivery-story notes
      (private repo or excluded folder)
- [ ] Resolve the GitLab decision: public curated mirror (recommended) or stop calling
      it public — record in session log
- [ ] Verify no secrets/keys in history (gitleaks clean) — evidence

### Session 3 — Evidence, demo, rehearsal

- [ ] Real screenshots/GIF/video: pipeline green, registries, `terraform plan`, HTTPS
      padlock, Grafana dashboards, alert received, restore drill
- [ ] Final architecture diagram + 5-minute walkthrough video (Loom-style, free)
- [ ] Interview rehearsal: walk the repo phase by phase; answer every ADR question and
      every learning-roadmap competency; mentor rival pass
- [ ] Optional stretch recorded: k3s mini-lab (conceptual only per spec)

### Close-out

- [ ] Final portfolio review with the mentor (rival pass)
- [ ] Execution plan Phase 15 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\Repo2`

---

## Mentor Questions

1. What should a stranger understand from your repo in the first minute?
2. Why do the internal AI docs leave the public repo (ADR-0014)?
3. What is the difference between a screenshot and evidence?
4. Defend: why three registries? why Terraform? why MySQL? why rollback by tag?
5. What is the one sentence that describes the whole project?

## Report (student fills after the session)

### What I did

### How it works / why

### Lessons learned / self-explanation

> In your own words: what changed between the first commit and today, in one paragraph
> — that paragraph is your interview opening.

### Evidence

- [ ] Public README v2 live on GitHub
- [ ] Releases + tags + LICENSE + CHANGELOG
- [ ] Demo video link
- [ ] gitleaks clean report
- [ ] Session log + execution plan updated; memory folder synced

> 🏁 **Project complete.** The portfolio is a curated repo, a live demo, and a student
> who can defend every decision.
