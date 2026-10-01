# Adapter setup and verification

Version 0.1.0 — 2026-10-01. File installer tested in fixtures and applied on personal Mac. Codex core injection observed in this chat after installation; other runtime loading and skill discovery NOT YET VERIFIED. Installing files does not grant permission to read every file on a machine.

| Surface | Installation | Runtime acceptance |
| --- | --- | --- |
| Claude Code | Managed core block in `~/.claude/CLAUDE.md`, my-* skills in `~/.claude/skills` | New session: inspect `/context` memory and skills, invoke my-feature-workflow with a discussion-only request; confirm no edits |
| Codex | Core in `~/.codex/AGENTS.md`, skills in `~/.agents/skills`; refuse existing override/custom CODEX_HOME until mapping reviewed | New session in real repo, check loaded instruction sources/skill catalog, test discussion vs implementation boundary |
| Cursor local | my-* skills in shared `~/.agents/skills`; core via User Rules UI | Customize → Rules: append core below without replacing existing rules; verify in fresh Agent chat and skill list |
| Copilot VS Code | my-* skills shared `~/.agents/skills`; core via user instruction in active VS Code profile | Agent Customizations → Instructions → user scope, apply to all files; inspect loaded references and skill listing in fresh chat |
| Claude Desktop/Cowork | Manual skill upload if that mode/account supports it; otherwise profile/project instructions and relevant references | Verify on the actual mode; Claude Code adapter is not proof of Cowork/chat behavior |
| ChatGPT web/app | Manual custom/project instructions and relevant profile/reference attachment | Verify actual surface; no claim local skills or filesystem sync applies to normal chat |

## Core for manual setup

Use `context/core.md`, remove draft label, add the main repo path on that machine. User Rules that sync account-wide must NOT hardcode a personal Mac path; use a routing note: “Use my-ai-context at the configured primary workspace on this machine; ask for its path if unavailable.” Detailed profile is not always-on instruction.

VS Code core: create a user-scoped instruction using the Agent Customizations UI for the selected harness and frontmatter `applyTo: '**'`. Preserve existing user instructions. Profile folder is machine/profile dependent; installer does not guess or rewrite settings.json. Selecting Copilot target installs skills only, not this always-on core.

Cursor account User Rules may sync via account; shared skill files do not automatically sync between local Macs. Do not enable cloud sync of company content without approval. Avoid additionally installing the same my-* skills into cursor/copilot roots unless required by a validated client.

## Plugin steps (not run by bin/context)

Figma: follow vendor's official client-specific plugin setup, sign in with appropriate account and test a permitted frame. Claude Code official plugin command, after explicit installation permission: `claude plugin install figma@claude-plugins-official`. Cursor: official Figma setup link/plugin instructions. Check design context and screenshot for the same frame, map current project components. OAuth is per machine; secrets stay outside Git.

Frontend-design: select official Anthropic plugin for exploratory UI after comparison with existing design skills; do not auto-enable for approved Figma/Hive tasks. OpenSpec remains per-project; do not initialize in a repo without permission.

Sources checked 2026-10-01:
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/skills
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/build-skills
- https://prod.cursor.com/help/customization/rules
- https://prod.cursor.com/help/customization/skills
- https://code.visualstudio.com/docs/agent-customization/agent-skills
- https://code.visualstudio.com/docs/agent-customization/custom-instructions
- https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/

## Pilot checklist

1. Record client/version, source version, actual loaded core and selected skill, not just AI self-report.
2. Ask to discuss a feature: require clarifying options/recommendation, zero implementation.
3. Explicit small edit in an allowed repo: complete scope; zero new branch/commit/push.
4. Figma UI: read frame/context first, use existing system; report inaccessible design honestly.
5. Backend: inspect current convention; do not introduce JWT/repository pattern/ORM by default.
6. Verification: choose affected platforms and minimal checks; ask before broad/expensive runs.
7. New machine: same approved source, no local edits overwritten; last-known-good available offline.

Full behavioral pilot has not been run in live clients; fixture tests establish installer behavior, and current Codex instruction context establishes core injection only. Core token count pending actual tokenizer/client evidence; file size is not a token count.
