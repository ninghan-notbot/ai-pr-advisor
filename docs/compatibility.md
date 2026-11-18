# Installation and observed host support

Evidence dates are recorded below. A prepared directory or ZIP is not proof of installation or runtime behavior.

| Product surface | Install format | Actual state |
| --- | --- | --- |
| Codex CLI 0.169.0-alpha.11.1 | Project `.agents/skills/ai-pr-advisor` | Project installation and natural-language invocation observed; native multi-turn consultations tested on gpt-6-astra. This does not prove every model or prompt will select the Skill. |
| 豆包工作 / Doubao Work | Flat ZIP with SKILL.md at root | FORMAT_PREPARED / UNVERIFIED. No local app available for actual import and runtime validation. Ordinary Doubao chat is not a substitute. |
| Kimi Code CLI | Project `.agents/skills/ai-pr-advisor` | FORMAT_PREPARED / BLOCKED: usable local installation/account unavailable. Kimi chat and Agent mode are separate products. |
| Claude Code | Project `.claude/skills/ai-pr-advisor` | FORMAT_PREPARED / UNVERIFIED: CLI 2.1.97 observed on 2026-11-18; Skill installation and triggering not tested in this cycle. The earlier authentication block is a historical observation, not a new login check. |

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

## v0.5 development evidence

On 2026-11-17, the official Codex GitHub URL installer was tested in an isolated project with
existing private-repository authorization. Authenticated **download** installed all 22 baseline
payload files byte-for-byte from commit `30af387ade8343a4cb1ed8d7fbe8faee823f6e5b`.
A normal one-turn consultation in that GitHub-installed baseline then read the entrypoint, index
and relevant cards without naming the Skill or requesting file reads. This is a baseline runtime
check, not a remote v0.5 test.
The repository-root **Git sparse-checkout** method reported success but omitted subdirectories;
its failed installation was retained. Do not use that fallback for this repository layout.
The download method also copies repository documentation/tools; it is not the minimal 22-file package.
No global installation or account setting changed. The v0.5 development payload has 26 files and
was tested locally; remote installation of that payload was NOT_TESTED in the v0.5 handoff.

No new Doubao Work, Kimi Code or Claude Code runtime validation is claimed. The owner's formal
Doubao session follows internal review. Native web availability is a host/account capability;
a successful Codex web test does not certify another platform's browsing or Skill installation.

## v0.6 local development evidence

The frozen 0.6.0-dev.1 payload completed 30 native multi-turn consultations in an isolated Codex
project, paired with 30 plain-model consultations. 30/30 runs read the Skill
entrypoint without an explicit user file-read request. This verifies the observed local workflow,
not every model, automatic invocation or professional outcome. Evaluation limitations and
separate supplementary runs are described in [evaluation](evaluation.md). The v0.6 handoff kept
its changes local and used 0.4.0-rc.2 for the recorded GitHub installation check. No new Doubao Work,
Kimi Code or Claude Code installation/runtime claim is made.

## Global scope and additional hosts — 2026-11-18

One standard Agent Skill core is maintained. Codex, Doubao Work, Kimi and Claude Code remain
priority targets. Kimi CLI is still absent in this local environment; no new runtime validation
of the other priority hosts is claimed from documentation or a folder layout.

ChatGPT, DeepSeek, Muse and other products are **UNVERIFIED** for installing and triggering this
package: a precise supported product surface and an actual install/activation record are needed.
Ordinary chat uploads, fluent responses or another host's successful test are not substitutes.
No host-specific copy of the consulting methodology is created.

English and Chinese are the priority consultation languages. Actual country, audience, industry
and local obligations determine localization; language alone does not. Japanese, Korean and other
language support is planned for later validation, without adding country libraries in V1.

## v0.6.1 observed local state

The 26-file dev.1 package was installed in an isolated Codex project and naturally activated in
all eight targeted consultations; actual decision-guide reads were recorded. The final dev.2
package was separately installed and checked in five first-turn loading probes. Those probes
all read the decision guide before further references; two did not meet the intended delivery
stage criterion. Full multi-turn professional results for dev.1 are not relabeled as dev.2 results.
That development check performed no additional host installation or GitHub upload. It does not
state the live remote HEAD. Check the selected GitHub ref and installed SKILL version when testing
a newer candidate. Platform claims above remain limited to their recorded observations.
