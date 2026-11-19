# Installation / 安装

Version: **0.6.4-draft.2**, beta candidate. The complete fixed package and SHA-256 values are listed in [install-manifest.json](install-manifest.json). Do not copy only SKILL.md: relative reference files are part of the Skill.

## Verified scope as of 2026-11-19

| Entry | Installation evidence | Consultation evidence | Natural-language installation |
|---|---|---|---|
| ChatGPT Work, account with Skills | Standard ZIP imported; full file tree visible | One bounded draft.2 scenario broadly usable; no overall advantage claim | Not yet verified |
| Claude ordinary desktop | Standard ZIP replaced existing skill, draft.2 visible | Fresh natural-language task did not list AI PR Advisor in session skills; unsupported commitments appeared | Not verified; do not recommend as a completed chain |
| QwenWork web | Standard ZIP imported via Skills, same-name replacement; selected skill used | Three-turn draft.2 check completed; material consistency issues remain | Not verified |
| Doubao web, New Work Task | Doubao-layout ZIP imported; manual selection | Earlier draft.2 check had substantive policy/fact errors | Not verified; not a recommended reliable entry |
| Gemini web | Gemini-layout package available | No new draft.2 consultation; earlier failures are not converted into current results | Not verified |
| WorkBuddy desktop | Official local-skill directory documented; live client setup pending | Not run | Pending live verification |

These rows describe specific entries, not all products offered by those companies. Availability on mobile, free accounts or other workspaces is not established. The Skill itself requires no payment; host access and usage allowances vary. Stop at payment, quota, subscription or permission changes that you did not intend.

## Existing manual import paths (development evidence)

These **do not meet the one-sentence installation goal**:

- Claude ordinary desktop: Customize → Skills → Add → Upload skill → standard ZIP. Replace the same-name skill only when that is intended.
- QwenWork web: 技能·扩展 → 技能 → 添加 → 从电脑上传 → standard ZIP. Confirm version 0.6.4-draft.2. New task → choose ai-pr-advisor.
- ChatGPT Work: Skills → Add skill → upload standard ZIP; use the installed Skill in a fresh Work task. This is not a claim about ordinary ChatGPT chat or all personal accounts.
- Doubao: 插件·技能·连接器 → 技能 → 添加 → upload Doubao-layout ZIP; New Work Task → choose skill. Ordinary New Chat is not verified.
- Gemini: use only its documented custom-skill import with the Gemini-layout ZIP if your account provides it; no current quality recommendation.

## Agent-readable installation route

An agent with official local file access can read the fixed manifest, download the complete standard archive, verify its SHA-256 and all listed file hashes, and place the whole `ai-pr-advisor/` directory in the host's persistent skills location. For WorkBuddy the official SkillHub documentation names `~/.workbuddy/skills/`. The installer should report any native approval, collision or unavailable persistence capability, and must not claim that reading a document once is installation.

This route is **not yet a verified friend instruction**. It will be marked verified only after the host itself installs the fixed public files and the Skill is available in a new task.

Official references: [WorkBuddy Skills](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market), [SkillHub installation](https://skillhub.cn/install/skillhub.md). Conversational market installation is separate from installing an unpublished local Skill. This project is not listed in that market.
