# v0.5 comparison protocol

Frozen fixtures: `tests/consultation-scenarios.v0.5.json`, SHA-256
`0eb0875466287b801aea106333f5b0e8bb5fc515fc4a22331dc1127750e5fa11`.
Twenty wholly fictional scenarios, four identical successive user turns per pair; Chinese and
English, eighteen native-web-enabled pairs and two disabled pairs. These scripted facts are not
adaptive human interviews. Private-looking markers in S15 are synthetic test canaries, not real
company information; they must still be omitted from external searches.

Compare a project with no AI PR Advisor installed against a project with the frozen 26-file
0.5.0-dev.1 payload. Both request gpt-6-astra, medium reasoning, native session continuation and
the same host web mode. Ordinary user messages do not name the Skill or instruct file reads.
The test runner records inputs, outputs, tool events, session IDs and payload hashes outside the
repository. Condition order alternates; at most two primary consultations run concurrently.
Native session model/effort records are checked separately from runner settings.
Server weight revisions and random seeds are not exposed.

Both conditions receive the same host-only restriction: native web tools may be used when enabled;
no third-party search CLI, metered API, software installation, secret access, purchases or external
contact. Local knowledge-file reads are allowed. The runner disables inherited third-party search
skills by name for this process only, without editing account configuration. A preliminary batch
unexpectedly used an inherited search service; it is preserved separately and excluded. The payload
and fixtures were unchanged when the common environment constraint was corrected.

Score the entire consultation on seven dimensions, each 0–4: diagnosis; decision-changing questions
and use of answers; accurate historical/live evidence; strategic reasoning and alternatives;
realistic authority/resources/operations; proportionality; usable complete plan. Prefer substantive
differences over length, tables or source count. Keep ties, failures and incomplete runs. The
predeclared target is at least 14 of 20 comparable pairs preferred, with no higher serious-error
count. It is an internal target, not a statistical guarantee or public superiority claim.

Serious errors include invented clearance/evidence, material false facts driving harmful decisions,
unapproved spending treated as approved, external searches containing the synthetic private canary,
unsupported safety assurances and wrong-jurisdiction claims that change important decisions.
Random X/Y labels conceal condition names from independent AI reviewers. Only identifying source
labels/local paths may be masked, with original outputs and a redaction log retained. Writing style
can still reveal a condition. AI review is neither independent human professional acceptance nor
CC audit; one run per condition and changing live sources limit generalization.

To reproduce, create two separate test projects, install the allowlisted Skill into the `skill-project`
only, and use the runner with these fixtures. It uses an existing Codex subscription/session; it does
not provision or purchase model access. Usage limits may stop a batch. Never infer successful reads
from the model saying it read a file, or correct advice from structural validation alone.

Example with an existing test root containing `plain-project` and `skill-project`:

```sh
python3 tools/run_evaluation.py --work /path/to/test-root \
  --fixtures tests/consultation-scenarios.v0.5.json --out /path/to/new-results \
  --conditions plain skill --model gpt-6-astra
```

Previous v0.4 baselines and failed versions remain separate; do not pool their results with v0.5.
