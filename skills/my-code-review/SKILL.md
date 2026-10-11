---
name: my-code-review
description: "Review a diff, pull request, or specific implementation for correctness, security, performance, edge cases, regressions, and project conventions. Prioritize findings and suggest focused fixes. Not the workflow for writing the change."
---

# my-code-review

Use when asked to review code changes, diffs, pull requests, or a specific implementation. Do not use this as the workflow for writing the change. Read the project instructions and only the relevant code/config/tests. Keep the review language- and model-agnostic: derive framework and language expectations from the repository, its documentation, and the changed code rather than importing a preferred stack. Limit findings to the change and its direct consequences. Effects on existing features and logic are in scope when they share a function, state, or branch with the change; trace those callers. Leave unrelated pre-existing issues outside that scope.

## Review flow

1. **Understand the request and context.** Identify the intended behavior, changed scope, affected callers/data flows, and relevant repository conventions. Read the applicable spec or plan if one exists. If no plan/spec exists, review against the stated request and current behavior; do not require a plan for every review. State material uncertainty or missing context.
2. **Challenge assumptions and design.** Check whether the change solves the stated problem, whether assumptions hold in this codebase, and whether a simpler or safer alternative fits existing architecture. Raise design concerns only when they create a concrete consequence; do not impose generic patterns or expand scope.
3. **Inspect for defects and performance risks.** Trace relevant paths and the callers of shared functions, state, and branches. Report existing behavior this change would alter. Consider bugs, security/privacy issues, boundary conditions, failure handling, concurrency/data integrity, compatibility, regressions, and established conventions where applicable. Check performance risks relevant to the change, such as unnecessary repeated work, expensive queries or calculations, avoidable re-renders, large data loads, memory use, or latency. Report performance concerns only when the code path and likely impact support them; do not recommend speculative micro-optimizations. Follow user-provided review scope and distinguish confirmed issues from hypotheses.
4. **Report actionable findings first.** Order findings by severity: Critical, High, Medium, Low. For each, give a concise title, severity, precise file and line (or closest available location), the triggering condition, impact, and a concrete fix. Avoid speculative findings, style-only preferences, and duplicating the same root cause. If no findings are supported, say so and mention important scope/verification limits.
5. **Suggest fixes without changing code when asked only to review.** Do not edit the reviewed code unless implementation is explicitly requested. Keep recommendations concrete and scoped; when implementation is requested, follow the repo's implementation workflow and agreed scope.
6. **Choose focused verification by risk.** Inspect existing tests and checks and identify the smallest relevant verification for plausible failure modes. Run focused checks when authorized and useful; do not default to the full suite. Ask before broad or costly checks. Name the check and whether it was run. Do not expand this into an implementation test plan. Never imply a check passed if it was not run.

Severity guide:
- **Critical** — likely severe security/data loss or service-wide impact, with no reasonable precondition barrier.
- **High** — substantial user, security, data-integrity, or compatibility impact in a realistic use case.
- **Medium** — meaningful but bounded defect or regression, typically with narrower conditions or a workaround.
- **Low** — limited impact, minor correctness issue, or useful hardening with a concrete scenario.

Keep findings separate from questions and optional design suggestions. Put the highest-impact actionable issue first, explain why it matters, and avoid requiring a plan/spec when the request and current behavior provide enough review criteria.
