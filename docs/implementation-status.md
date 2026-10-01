# Implementation status — 2026-10-01

## Implemented and checked

- Version 0.1.0 manifest and 8 local skills: context, interview, research, feature, Figma UI, risk-based verification, backend review and context maintenance.
- Profile/workflow canonical files rendered into installed references; only relevant skill bodies/references loaded by agent selection.
- bin/context: status, install, update, uninstall, rollback; dry-run default, explicit apply, backup/history/checksum/lock, unmanaged/drift/symlink refusal, transactional recovery, shared destinations.
- README update workflow works from any project but targets the primary checkout.
- 12 fixture checks passed: preview no writes, preservation/idempotency/uninstall, drift atomic refusal, unmanaged/symlink refusal, rollback incremental/update/uninstall, override refusal, reference rendering, shared-root deduplication, write failure restoration, writer lock.
- Thịnh approved the concrete 38-file preview. Applied on personal Mac: Claude global core + local skill copies; Codex global core + shared skills for Codex/Cursor/Copilot. Status: 38 managed files, zero drift, zero pending source changes. No Git operations performed.
- Codex current session subsequently received the installed AGENTS.md core v0.1.0 as instruction context. This verifies core injection on this surface; the current session skill catalog also subsequently lists all 8 my-* skills. Core/catalog discovery verified here; full behavioral pilot remains unverified.

## Pending, not represented as completed

- Fresh-session skill discovery and behavioral pilot in each client; Codex core injection already observed. Claude core file installed but runtime loading not yet observed.
- Cursor/Copilot always-on core via profile UI; desktop/chat integrations remain manual until tested in actual surface.
- Figma official plugin installation/authentication and frame test; frontend-design comparison/activation.
- Full third-party source/license/version audit and managed import. Current 14 technical bundles remain in place; React differs, most local bundles lack LICENSE copies. MIT license files found upstream for Expo and web-interface-guidelines; root license endpoints for Vercel agent-skills and NestJS returned not found. Do not infer no license from that alone; inspect upstream metadata before import.
- Source synchronization: no background automation or implicit Git pull/merge. Remote still has no pushed playbook content; commit/push requires request.
- Company Mac/Copilot runtime not accessed; plan requires separate setup there.
- Core token measurement unavailable in bundled Python (no tiktoken); no token cap claim yet.

This is a working first release of local skills/installer, not verified end-to-end coverage of all apps.

Skill metadata and installed reference rendering validated by installer/fixture checks. Bundled quick_validate.py could not run because PyYAML is absent; no package installed solely for this check. Local skill frontmatter intentionally uses JSON-quoted strings valid in YAML and is validated without dependencies.

Portable entrypoint: context.sh added at repo root. All 14 fixture checks passed, including invoking from a different working directory with spaces in the repo path and moving the checkout then refreshing installed paths. README now uses commands run inside the repo and describes private clone/setup on another machine.
