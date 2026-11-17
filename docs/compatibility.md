# Installation and observed host support

Checked 2026-11-17. A prepared directory or ZIP is not proof of installation or runtime behavior.

| Product surface | Install format | Actual state |
| --- | --- | --- |
| Codex CLI 0.169.0-alpha.11.1 | Project `.agents/skills/ai-pr-advisor` | Project installation and natural-language invocation observed; native multi-turn consultations tested on gpt-6-astra. This does not prove every model or prompt will select the Skill. |
| 豆包工作 / Doubao Work | Flat ZIP with SKILL.md at root | FORMAT_PREPARED / UNVERIFIED. No local app available for actual import and runtime validation. Ordinary Doubao chat is not a substitute. |
| Kimi Code CLI | Project `.agents/skills/ai-pr-advisor` | FORMAT_PREPARED / BLOCKED: usable local installation/account unavailable. Kimi chat and Agent mode are separate products. |
| Claude Code | Project `.claude/skills/ai-pr-advisor` | FORMAT_PREPARED / BLOCKED: CLI is present but local authentication reports not logged in. |

## Folder installation

Use `tools/install.py --project /path/to/project --platform codex` (or `claude`, `kimi`).
The destination project must already exist. Installation refuses a different existing payload.
For an upgrade, preserve any local changes and move the previous Skill aside deliberately before installing.
For uninstall, remove only this project's ai-pr-advisor Skill folder, after preserving any user changes.
The installer does not alter global settings or user consultation records.

## ZIP import

The standard ZIP contains an ai-pr-advisor directory. The import ZIP puts SKILL.md, LICENSE,
NOTICE and the reference folders directly at archive root. The Doubao official developer guide
indexed on the check date specifies this root layout and ZIP size constraints. Its direct page
was not text-readable to this checker; developer submission requirements do not prove the same
UI flow in every Doubao Work account. Use the actual Skill import entry where offered, then
confirm it appears installed and that a normal problem activates it. Uploading a ZIP to an
ordinary chat does not establish installation. No plugin marketplace submission was performed.

## Reference documentation

- [Codex Skill discovery](https://learn.chatgpt.com/docs/build-skills)
- [Kimi Code Skills](https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Doubao official Skill integration guide](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide)

The optional local state helper uses Python 3 and POSIX locking. Windows and nonlocal filesystems
remain UNVERIFIED. No server or private-store connector is needed or supplied.
