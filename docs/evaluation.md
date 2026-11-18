# v0.6 adaptive consultation evaluation

Thirty new paired scenarios cover ordinary natural-language users, experienced practitioners and
users able to formulate a precise brief (ten per cohort). The same gpt-6-astra advisor at medium
effort receives the same opening, fact bank and native-web permission. Follow-up user replies
adapt to actual questions through a separately blinded, fixed-fact router. This is a simulation,
not a human user study. See the [protocol and observed deviations](evaluation-protocol-v0.6.md).

Completed 60/60 consultations with 197 advisor outputs.
Of 30 evaluated pairs, 25 satisfy both runtime and reviewer comparison checks:
Skill preferred **15**, tied **6**, plain preferred **4**.
Limited pairs remain in the original evidence and are not silently replaced or counted as clean
wins. There was no preset win target or post-result alteration of the rubric.

| Cohort | Comparable | Skill preferred | Tied | Plain preferred | Skill absolute gate | Plain absolute gate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| natural | 9/10 | 5 | 2 | 2 | 9/10 | 9/10 |
| experienced | 7/10 | 7 | 0 | 0 | 10/10 | 9/10 |
| expert_prompt | 9/10 | 3 | 4 | 2 | 7/10 | 4/10 |

Six dimensions are each scored 0–4: goal fidelity, core facts, question efficiency/burden,
professional judgment, complete-plan quality and an experience proxy. The absolute gate is
at least 18/24, each dimension at least 2 and no confirmed serious error. Gate counts above
include all observed outputs, including comparison-limited pairs; they are not certifications.
Absolute quality and relative preference are separate: one extra point does not imply a win.
Reviewer-flagged serious errors: Skill 1, plain 0.
These labels require source-level professional review; disputed interpretations remain documented
without silently rewriting the original scores or gate counts.
All failures, ties, first-turn behavior, later corrections and opposing advantages are retained.

Among the 25 comparable pairs, mean core-fact scores are 3.24 for Skill versus 2.56 for plain,
and complete-plan scores 3.56 versus 3.04. Goal fidelity is 3.84 versus 3.88 and the experience
proxy 2.92 versus 2.96; question efficiency/burden is 2.76 versus 2.68. These are descriptive AI
scores, not proof of easier use or statistically established improvements. Skill fails the
absolute gate in N06, P01, P05 and P09. P05/P09 show a recurring weakness: giving a general
framework without actually asking about the user's current constraints. The P01 approval flag
depends on ambiguous wording in the fictional fact bank; the reviewer's clarification assigns
low confidence to unambiguous confirmation of a serious error. The original score remains intact.

The advisor supplied 103 turns for Skill versus 94 for plain, with median advisor time of about
143 versus 110 seconds per consultation, excluding simulation and review. More interaction and
longer outputs are not treated as evidence of higher quality.

The first attempted batch omitted earlier visible messages within a turn from the simulated-user
router. It was stopped and retained separately before full condition-key release. The complete
corrected primary used all visible messages and a frozen direct-relevance routing policy. Its
remaining Markdown quote-matching failures are visible comparison limitations. Every mechanically
affected pair is retested on both sides under a predeclared formatting-only correction; those
supplementary results do not replace or increase the primary win count. Three cases selected by
fixture hash also receive a different review with reversed labels, separately from the primary.

The payload remained frozen throughout the primary batch. 30/30 Skill runs
actually read its entrypoint. The intended-offline cases made 4 observed web calls through another host search connector: disabling the CLI web surface did not close that connector. E03 and P03 are excluded from clean comparison. The remaining intended-offline cases show no web use but do not demonstrate enforced offline isolation.
Structural tests passed (14 repository checks, Skill validation and four adaptive-reply policy
checks), but they do not establish advice quality. Raw transcripts, router choices, native logs,
source evidence, hashes and blinded judgments accompany the protected review archive.

Model-based routing can miss questions or supply related context within a fact group. Fixed answer
capacity and a common second-turn update further limit realism. Reviewers flag material simulator
errors as comparison limitations. One run, changing public pages, possible style leakage and AI
judges cannot establish population-level superiority or real user experience. New scenarios and
a new rubric also prevent causal attribution of changes relative to v0.5. The owner's three reported
human preferences from v0.5 remain separate qualitative evidence, not extra samples in this table.

No new cash purchase or paid API service was added; tests used existing subscription/native tools.
No production system, global configuration, remote branch or visibility was changed. This is an
unreleased local candidate, not a completed independent professional or CC audit.

The three formatting-only supplementary pairs completed all six consultations and passed runtime
checks. E01 and E04 were comparable and favored Skill; N08 remained comparison-limited because
an overly broad unknown-information reply could alter subsequent questioning. All six outputs
passed the provisional absolute gate. These results are separate, never pooled with the primary.
Three preselected, reversed-label second reviews agreed on preference, with differing absolute
scores; three cases do not establish reviewer reliability.

GPT should review the failed consultations and approval ambiguity before a further targeted CC
audit is scheduled. Test-tool isolation and simulator answer scope need repair; no new research
collection, product architecture or public performance promise is justified by these results.

## Earlier v0.5 evidence (preserved)

# Development evaluation, 2026-11-17

Version **0.5.0-dev.1** completed 20 paired, four-turn scripted consultations: 160 final
outputs, 10 Chinese and 10 English scenarios, 18 native-web-enabled pairs and two offline pairs.
The same gpt-6-astra model label and medium effort were observed in native session records;
server weight revisions and seeds were not exposed. Each pair used identical successive user
inputs and web permissions, with no forced Skill invocation. See the
[frozen protocol](evaluation-protocol-v0.5.md) and included fictional fixtures.

Independent AI reviewers, without the condition key, preferred the Skill in **4/20** pairs,
preferred ordinary AI in **0/20**, and tied **16/20**. Neither condition had a confirmed serious
error under the predefined rubric. The target of at least 14 Skill preferences was **not met**.
This is neither proof of overall superiority nor proof of equivalence. No independent human
professional acceptance or CC audit has been performed on this development version.

| Scenario | Blind preference | Plain /28 | Skill /28 |
| --- | --- | ---: | ---: |
| S01 | TIE | 27 | 28 |
| S02 | TIE | 27 | 27 |
| S03 | TIE | 27 | 28 |
| S04 | TIE | 27 | 28 |
| S05 | TIE | 27 | 27 |
| S06 | TIE | 27 | 28 |
| S07 | TIE | 28 | 28 |
| S08 | TIE | 28 | 28 |
| S09 | skill | 25 | 28 |
| S10 | skill | 26 | 28 |
| S11 | TIE | 27 | 27 |
| S12 | TIE | 27 | 28 |
| S13 | TIE | 28 | 28 |
| S14 | TIE | 28 | 28 |
| S15 | TIE | 28 | 27 |
| S16 | skill | 25 | 28 |
| S17 | skill | 27 | 28 |
| S18 | TIE | 27 | 27 |
| S19 | TIE | 28 | 28 |
| S20 | TIE | 27 | 28 |

Scores are auxiliary; a one-point difference does not automatically imply preference. The four
preferences concerned internal-judgment wording and actual refund completion (S09), decision
rights and a funding deadline (S10), event safety/authorization and remedy receipt (S16), and
realistic staffing and emergency-supply access (S17). Ordinary AI also supplied useful details
that the Skill omitted. No advantage is inferred from longer answers, more tables or citations.

Small Skill defects remain: assigning a clinic administrator production-change approval without
confirming that authority (S11); omitting the qualified wording in a UK breach-reporting deadline
(S15); and weaker explicit night-shift evacuation coverage in one plan (S18). Reviewers did not
classify these as serious errors in the conditional plans; they remain visible for professional
review. Minor ordinary-AI defects and ties are retained as well. Two deterministically selected
pairs received a second blind review with reversed labels: one remained tied and one changed
from tied to a narrow Skill preference. Primary results were not replaced. This small diagnostic
is not a reliability estimate, and the high scores warrant expert scrutiny for ceiling effects.

All 20 Skill consultations read the entrypoint, index and full-plan guide; all 18 live cases read
the investigation guide. Five read the relevant new historical precedent file. Successful reads
show availability, not correct application. Native tool logs recorded 57 web actions for plain
and 72 for Skill; the offline cases made zero web calls. No synthetic private marker appeared in
external queries. Median consultation times were 130.63 seconds (plain) and 155.86 (Skill),
including tool waits. Skill output tokens were 187,031 versus 148,738; extra resource use did not
produce majority preference. Token telemetry is not a bill and concurrent runs affect timing.

An environment precheck unexpectedly inherited a third-party search skill and made three basic
queries. It was stopped and retained separately, including incomplete sessions, then excluded.
The entire primary comparison was rerun after identical host-only restrictions were applied to
both conditions. Payload and fixtures were unchanged; no business coaching was added to plain.
Those queries used existing free allowance, with observed pay-as-you-go usage zero. No new
purchase or incremental cash charge was observed; model runs used the existing subscription.

One run per condition, developer-authored fixed four-turn inputs, changing live pages and AI
review limit the conclusion. Users did not actually choose their next answer in response to the
model's questions. Writing style may reveal conditions despite label blinding. The Skill payload
was frozen before the primary tests and was not tuned against the resulting scores. Complete
raw evidence, failed batches, session records and blinded reviews remain outside the public
repository; the professional review package includes all visible consultations and final outputs.

The 14 repository unit checks, structural validation and six private-registry evidence-gate checks
passed. These establish neither advice quality nor compatibility with untested platforms.

## Preserved 0.4.0-rc.2 evaluation


Version 0.4.0-rc.2 was installed as a project Skill in Codex CLI
0.169.0-alpha.11.1. All conditions requested gpt-6-astra with medium reasoning.
The plain condition had no installed Skill; the core condition had the repaired instructions
and earlier compact references; the enhanced condition added 40 decision cards and their loader.
Normal user prompts never named the Skill or requested a file read. The host selected the
installed Skill. Native session resume preserved each three-turn consultation.

Four fictional consultations covered a small bookstore, a multi-store bookstore, a China–US
education service and a nonprofit festival. Each condition received identical successive facts.
All four final enhanced consultations read the entrypoint, card index and relevant card groups.
Plans changed when new facts invalidated the initial diagnosis; approved spending purposes
remained distinct from proposed compensation, and permanent guarantees were rejected.
Questions stopped when the user requested a plan. These are scripted conversations, not a
study with independent human participants.

Eight further prompts each contained five short, separate decisions: 40 card applications in
all. The core and final enhanced conditions produced 16 outputs. All eight enhanced responses
had successful tool evidence of reading the relevant group. Developer review found useful
actions, owners and evidence boundaries across the 40 decisions, but no general superiority
over the core. A toy recall answer provided weaker interim consumer instructions than the core;
it remains unsuitable as an unreviewed operational safety notice. Cards support planning and
do not replace qualified safety, medical, legal or financial review.

The primary evidence contains 36 multi-turn outputs and 16 card-probe outputs (52 total).
An earlier enhanced candidate's 20 outputs remain separately retained: 3 of its 8 card probes
and 1 of its 4 consultations did not read the relevant card group. A loader correction was
followed by rerunning all enhanced scenarios. One initial invocation pilot is separate.
All 73 captured outputs are retained; earlier-version results are not pooled into final scores.

Integrity checks compare exact inputs, output hashes, payload hashes, successful full-file reads
and continuity of session identifiers. They do not grade advice. Professional comparison examines
decision changes, resource fit, approval boundaries, actionable remedies and language consistency.
Length, tables and number of steps are not quality measures.

The ordinary model and core performed strongly. Overall incremental quality gain is **not
established**. Some enhanced answers added useful precision, but one unblinded developer review,
one run per prompt/condition, directed card probes, nonrandom version order and tool-access
differences cannot establish causal or statistical superiority. Server-resolved model and seeds
were not exposed. No new paid API was used; existing subscription capacity was consumed.

Raw consultation and tool evidence is stored outside the public repository. The reproducible
runner and integrity checker are included; runtime evidence and professional acceptance remain
distinct. Other hosts require their own installation and behavior checks.

## v0.6.1 targeted development regression — 2026-11-18

The 0.6.1-dev.1 candidate was tested in eight fresh fictional multi-turn pairs on the same
observed gpt-6-astra/medium configuration. Six pairs shared live-web permission; two offline
pairs were functional checks and were excluded from the comparative denominator. Two blinded
AI reviewers preferred the Skill in four of the six comparable pairs and tied two. This small,
purposive AI assessment is not human validation or evidence of overall superiority. Both
reviewers passed all eight Skill consultations under the fixed absolute rubric; they disagreed
on one plain-model approval error. Longer answers received no credit merely for length.

Actual returned file content established first-turn decision-guide loading once in all eight
Skill consultations. Four initially combined or parallelized it with other references. The
0.6.1-dev.2 entrypoint makes subsequent reference selection depend on that completed read.
Five separate loading probes observed the intended sequential reads, but two still loaded the
delivery guide during an intended diagnostic opening: three passed the complete stage criterion,
two failed. The eight paired professional outcomes remain attributed to dev.1; dev.2 has not
repeated the full paired consultations. A separate missing-reference probe retained useful
initial advice and disclosed the missing guide.

Current offline controls removed exposed web/browser/connectors and image generation, found no
configured resource endpoints, and observed OS denial of a direct-IP connection. Delegation
remained exposed despite flags; an actual test child inherited the absent network tools and OS
denial. Formal offline consultations used no external tools or delegation. These observations
apply to this host configuration, not to every platform or future host version.

Remaining issues include premature delivery-reference selection, repeated or lengthy guidance,
and limited independent human/platform validation. Development evidence is retained privately;
no private research corpus, account data or raw user materials belong in the public package.
GPT review remains next; this work does not authorize publication or start CC audit.
