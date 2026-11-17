# Candidate packaging

Build only the explicit package allowlist. Directory and flat archives contain the same payload,
including LICENSE and NOTICE. Flat archives place SKILL.md at the ZIP root; directory archives
place it inside ai-pr-advisor. Packaging does not upload, publish or change repository visibility.

Before distributing a new version, check the exact archive, file hashes, linked references,
installation, natural invocation and relevant behavior tests. Retain failures in the evaluation
record. The owner must approve public release; local checks do not supply that approval.
