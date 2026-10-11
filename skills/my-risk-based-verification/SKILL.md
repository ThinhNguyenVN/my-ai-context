---
name: my-risk-based-verification
description: "Use when deciding which checks to run for a change. Pick the smallest useful code or UI check and skip broad suites. Not a code review and not the implementation style guide."
---

# my-risk-based-verification

Read [verification workflow](references/verification.md). Choose checks for concrete risks; no mandatory baseline or full suite. Ask before expensive/broad checks. Repeat only for new changes, failures or unresolved risks. Relevant platforms may be desktop/mobile web, iOS and Android; do not claim all verified from one pass. This skill only chooses and runs checks. It does not review the change or set coding conventions.
