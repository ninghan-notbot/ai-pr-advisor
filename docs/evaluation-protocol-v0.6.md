# v0.6 adaptive-user comparison

Thirty new fictional scenarios: ten ordinary natural-language users, ten experienced practitioners,
and ten practitioners able to formulate a more precise brief. Each cohort contains five Chinese
and five English openings. Twenty-one pairs explicitly enable host-native browsing; nine were intended to be offline (the observed connector-isolation failure is disclosed below). Neither
condition receives a prewritten professional plan directory in the user prompt.

Compare plain Codex against the same model with the frozen 26-file 0.6.0-dev.1 Skill installed.
The advisor model is gpt-6-astra at medium effort, using native session continuation and existing
subscription access. Identical host restrictions permit native web only; no third-party search API,
purchases, external contact, secret access or production writes. Model labels can be checked in
native logs; server weight revisions and random seeds are unavailable.

Both conditions begin with the same user message, hidden fictional fact bank, update schedule,
response capacity and stop policy. Subsequent user messages depend on what the advisor actually
asks. A separate, blinded gpt-6-astra router at medium effort maps verbatim requests to fact IDs.
It reads all visible messages in the latest turn and cannot use tools or invent facts. The harness emits canonical bank text, at most two, three or
four fact groups per reply for the three respective personas. Unknown details remain unknown;
public research requests are returned to the advisor. These short fact groups can contain related
context, so this is an approximation of a user answer, not a human interview.

A common new fact arrives after the second advisor response. A final usable recommendation is
requested when there are no further questions after that point, or after the fourth response.
There are at most five advisor turns. This bounded design measures how well the model prioritizes
questions and works with incomplete facts; it is not evidence of unlimited conversational ability.
Different information discovered by different questions is an intended outcome. Material routing
mistakes must be flagged; they must not be silently repaired or counted as clean comparisons.

The rubric, fixtures, payload and runner are hashed before the primary batch. An infrastructure
pilot is retained separately and excluded. All failed, tied and incomplete runs remain visible;
there is no win-rate target and no post-result change of thresholds or selection of only good cases.

Blind reviewers score six dimensions from 0 to 4: goal fidelity; core-fact identification; question
efficiency and burden; professional judgment; complete-plan quality; user-experience proxy.
0 is absent/harmful/unusable, 1 a major deficiency, 2 useful with a material omission or burden,
3 strong with minor correctable gaps, and 4 consistently precise, efficient and usable throughout,
justified by specific evidence. Absolute quality requires at least 18/24, every dimension at least
2 and no confirmed serious error. This is a provisional AI gate, not professional acceptance.
Relative A/B/TIE preference concerns meaningful practical differences and is recorded separately;
length, tables, terminology and citation count earn no automatic credit.

Reviewers record first-response behavior, final delivery, weaknesses on both sides, contrary
advantages, and simulator limitations. Material fabricated evidence/approval, consequential false
facts, unauthorized spending presented as approved, private-data disclosure and a consequential
final replacement of the explicit goal without agreement are serious errors. Offering an alternative
or explaining why a goal is infeasible is not automatically a violation.

One hash-selected case per cohort receives a second review with reversed labels and a different
reviewer. This small diagnostic never replaces primary judgments. Raw model messages, routing
choices, actual user replies, tool logs and hashes are kept outside the repository. Evaluation
scripts and full fictional fixtures accompany the review evidence for reproduction.

One run, synthetic personas, grouped facts, live pages, developer-authored scenarios and AI judges
limit conclusions. Experience scores are proxies, not ratings by real users. New-case performance
cannot by itself prove improvement over v0.5, which used different scenarios and a different rubric.
The three owner-reported human preferences from v0.5 are retained as separate qualitative evidence.

An initial attempted batch incorrectly passed only the final message to the user router. Blind
review identified omitted questions and asymmetric fact exposure. That batch, incomplete sessions
and its ten initial reviews are retained separately and excluded. Before a full corrected rerun,
the router was changed to receive every visible message in a turn, require direct fact relevance
and use medium effort. Six retained-turn regressions check the correction. Advisor payload,
fixtures and quality criteria were unchanged; no condition key had been revealed at that decision.

During final runtime review, two intended-offline consultations (one in each condition) were
found to use the host search connector, which remained available despite disabling the CLI web
surface. The first auditor had missed these MCP events. All tool surfaces are now included in
observed counts; E03 and P03 remain in raw evidence but fail the intended-offline runtime check.
The other seven intended-offline pairs show no observed browsing, without proving tool closure.
No original output or judgment was changed. The formatting-only supplement does not fix or
revalidate this separate permission-control defect. The administrator necessarily sees
condition-labelled runtime records; independent judges do not receive the condition key.
