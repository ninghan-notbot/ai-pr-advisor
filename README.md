# AI PR Advisor

A bilingual Agent Skill for public relations decisions and practical business remedies. Describe a
complaint, service failure or communications problem in ordinary Chinese or English. The adviser
asks questions that change the decision, adapts to your resources, and proposes accountable action.

**Version 0.4.0-rc.2 — release candidate.** Local tests are evidence for specific workflows, not a
guarantee of professional results or compatibility with every host.

## Install

From the repository folder, install into an existing project:

```sh
python3 tools/install.py --project /path/to/your-project --platform codex
```

For Claude Code use `--platform claude`; for Kimi Code use `--platform kimi`. These create real
project-local Skill folders and refuse to overwrite a different installation. An existing model
account is required; the Skill itself makes no API calls or purchases.

Alternatively extract the standard ZIP and place the complete `ai-pr-advisor` folder under the
host's Skill directory. Keep LICENSE, NOTICE and references with SKILL.md. For importers requiring
SKILL.md at ZIP root, including the documented Doubao developer import, use the flat ZIP. See
[installation and actual host status](docs/compatibility.md); ordinary chat uploads are not proof
of Skill installation.

## Try a consultation

“Our bookstore's collection orders are running late and customers are complaining. What should we do?”

In a host with implicit Skill discovery, no file-reading instruction is needed. If the host does not
select it, use its Skill picker or the host's explicit Skill command. Then continue with the facts
you have; you need not complete a questionnaire before receiving useful advice.

The package includes 40 concise decision cards in eight groups, loaded as relevant. It does not
include or query an external private research library. It will not contact media, publish or spend
money on your behalf. Proposed remedies remain proposals until authorized.

## Development and packaging

```sh
python3 -m unittest discover -s tests -v
python3 tools/validate.py
python3 tools/package.py --output /path/to/ai-pr-advisor.zip
python3 tools/package.py --layout flat --output /path/to/ai-pr-advisor-import.zip
```

[中文](README.zh-CN.md) · [Evidence and limits](docs/evaluation.md) ·
[MIT license](LICENSE) · [Third-party rights](NOTICE.md) · [Roadmap](docs/roadmap.md)
