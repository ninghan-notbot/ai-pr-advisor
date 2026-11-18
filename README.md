[English](README.md) · [简体中文](README.zh-CN.md)

# AI PR Advisor

An installable Agent Skill for public relations decisions and practical business action.
Describe your situation in ordinary English or Chinese: a customer complaint, a disputed claim,
a service failure, or a media opportunity. The adviser helps clarify the real problem, takes new
facts into account, and works toward a proportionate communications and execution plan.

Designed for global users with different levels of professional experience. Language does not
set the market: advice should follow the actual country, audience, industry and available resources.
English and Chinese are the priority languages; other languages and markets need further validation.

**0.6.1-rc.1 — release candidate.** Installation and professional results are verified separately;
broader superiority over ordinary AI is not established. Public release requires owner approval.

## Install from GitHub

With repository access, ask the Codex Skill installer to install
[AI PR Advisor from GitHub](https://github.com/ninghan-notbot/ai-pr-advisor/tree/main), repository
path `.`, Skill name `ai-pr-advisor`, using authenticated download.

GitHub installation uses the selected repository ref. Confirm its commit and the version in
`SKILL.md` before testing; this checkout describes **0.6.1-rc.1**. The authenticated download path
was observed on the earlier audited **0.4.0-rc.2** baseline; later refs need their own installation
check. While the repository is Private, access authorization is required. The root-level Git
sparse-checkout fallback omitted reference folders and should not be used for this layout.
See [installation and actual platform status](docs/compatibility.md).

From an authorized local checkout, install into an existing project:

```sh
python3 tools/install.py --project /path/to/your-project --platform codex
```

The same core can be packaged for other hosts. Use `--platform claude` or `--platform kimi` for
prepared project-folder layouts; these options alone do not prove installation or activation on
those products. Doubao Work remains a priority for actual import and user testing. Uploading a
prompt or document to an ordinary chat is not proof of Skill installation.

## Start with your problem

“Our repair bookings are late and customers are losing confidence. What should we do today?”

Then answer the questions you can. You can ask for a plan immediately, supply a draft for review,
or explain that some facts are unavailable. Where the host supports automatic Skill selection,
a normal request can activate it; otherwise use the host's Skill picker or explicit invocation.

The intended result is a useful decision with reasons, practical remedies, realistic responsibility
and approval, suitable communication, and a way to revise the plan as facts change. Short advice
may be enough for a small team; a complex issue can need a fuller plan. Relevant references and
current public research are used on demand, within the host's capabilities.

## Scope and availability

No server, paid API client or private-research connection is required or supplied. Running a
consultation uses your existing model account and tool allowance. Advice and drafts do not
publish, contact others or authorize spending on your behalf.

Codex has observed installation and consultation evidence. Doubao Work, Kimi, Claude Code,
ChatGPT, DeepSeek, Muse and other hosts are assessed by their actual installation and triggering
capabilities; a shared file format is not a compatibility guarantee.

[Evidence and limitations](docs/evaluation.md) · [Platform status](docs/compatibility.md) ·
[Development and packaging](docs/release.md) · [MIT license](LICENSE) · [Third-party rights](NOTICE.md) · [Project names and marks](TRADEMARKS.md)
