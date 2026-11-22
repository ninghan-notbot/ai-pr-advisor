[English](README.md) | [简体中文](README.zh-CN.md)

# SCI Studio · Strategic Communications Intelligence Studio

SCI Studio helps you work through public relations, communication and brand decisions: clarify the goal, compare options and risks, and prepare practical actions and communication materials. It comes as a local desktop app using your chosen model API, and as an Agent Skill using a compatible host's model and tools.

**Public alpha pre-release for personal and internal evaluation, not a stable product.** Professional gains over ordinary AI have not been established. Review facts, progress and commitments before using outgoing text.

The repository remains **`ninghan-notbot/ai-pr-advisor`**. The Skill identifier, application data identifiers and frozen filenames retain `ai-pr-advisor` for compatibility.

## Download the frozen candidate

| Download | Version and actual scope |
|---|---|
| [Mac · Apple silicon](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/ai-pr-advisor-desktop-0.7.0-alpha.13-mac-arm64.zip) | Desktop **0.7.0-alpha.13**; tested on Apple-silicon Mac with the DeepSeek configuration below. No Intel Mac build. |
| [Windows · x64 portable EXE](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/ai-pr-advisor-desktop-0.7.0-alpha.13-win-x64.exe) | Desktop **0.7.0-alpha.13**; **this build has not been run on Windows**. Matching bundled code does not establish native compatibility. |
| [Complete Agent Skill ZIP](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/ai-pr-advisor-skill-0.7.0-content.7-generic.zip) | Professional content **0.7.0-content.7**, also bundled in Alpha13; **not yet installed and validated in WorkBuddy or another host**. |

[Release notes / installation details](https://github.com/ninghan-notbot/ai-pr-advisor/releases/tag/desktop-v0.7.0-alpha.13) · [SHA-256 checksums](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/SHA256SUMS.txt)

**Use these dedicated assets.** GitHub's automatic “Source code” archives are not desktop apps and contain the older repository Skill. Cloning `main`, importing the repository URL or using its old installation manifest does **not** install content.7.

## Start using it

**Desktop:** download the matching asset, extract the Mac ZIP or open the Windows portable EXE, then open **Models & Settings**. Select your provider, enter your own API key and model, and review the usage limits before approving requests. Describe your goal, market, facts and available resources in ordinary Chinese or English. TXT, Markdown and CSV materials are supported; images, PDF and Word are not.

The app has 13 provider presets and a custom compatible endpoint. **Only Apple-silicon Mac with the official DeepSeek `deepseek-v4-pro` API, web search disabled, has been tested for this candidate.** Other presets do not constitute real-connection verification. Native web search was not retested for Alpha13. Provider API charges apply; the app does not top up balances or automatically retry failures. Estimated usage limits are not a provider billing guarantee.

Unsigned builds may trigger operating-system checks. See the release notes; do not disable system security globally.

**Skill:** obtain the complete **content.7 ZIP above**, then use a host's supported custom-Skill import. Keep `SKILL.md` and all reference files together. Enable/select it in a new task using that host's controls. WorkBuddy's import and invocation path for content.7 remains unverified; the earlier manual import of 0.6.4-draft.2 does not validate this version. Natural-language installation is an experience goal, not a verified capability. Host eligibility, tools, model and charges apply.

## Versions, data and limitations

- Desktop: **0.7.0-alpha.13**. Bundled professional content and downloadable Skill: **0.7.0-content.7**.
- **Code / main remains Skill 0.6.4-draft.2.** Its files and installation records are historical material, not the route for installing the new Skill.
- Desktop source code is not published. The repository contains the previously public Skill, public documentation and release downloads.
- Desktop projects and materials are stored locally in **unencrypted JSON**. Relevant project records, recent conversation and professional guidance are sent to your chosen model provider. API keys use protected local storage or session-only storage. Provider terms govern retention and training; Skill data handling depends on its host.
- Small tests do not establish general reliability. Drafts may still add unsupported services, dates, progress or promises. Check outgoing text and fill or remove placeholders. A model-generated “included / excluded” basis line is not independent verification. Copying a whole answer may include analysis as well as the draft.

## Licenses and attribution

- **Skill and original professional summaries:** [MIT License](LICENSE), also included in the content.7 ZIP.
- **Desktop binaries:** [Desktop Alpha Evaluation License](https://github.com/ninghan-notbot/ai-pr-advisor/releases/download/desktop-v0.7.0-alpha.13/DESKTOP_LICENSE.txt), allowing personal or internal evaluation of official unmodified binaries. This does not publish or open-source the desktop source.
- Third-party publications retain their rights and are linked in the package's source notes. [Project identifier guidance](TRADEMARKS.md) preserves ordinary attribution without implying endorsement. No private research library or consultation transcript is distributed.
