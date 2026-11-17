# Optional local consultation state

Use normal conversation context unless the user wants a local continuity record. With that
authorization, use the bundled Python 3 script; it has no network or private-store integration.
Choose a path in the user's own working folder outside a shared repository.

```sh
python3 scripts/session.py init ./sessions/example.json --language zh
python3 scripts/session.py add ./sessions/example.json --kind internal --claim opening-hours --text 'The manager expects the reading room to reopen at 14:00; staffing is not confirmed' --source 'User, current consultation'
python3 scripts/session.py show ./sessions/example.json
```

Kinds: `verified`, `internal`, `unknown`, `assumption`, `decision`. A verified entry requires a
source and a scope. To revise a claim use its same identifier with `--supersedes EVENT_ID`; history
is retained. The helper validates structure, not truth. It never upgrades confidence automatically.
An `unknown` entry can record new doubt or retract an unsupported claim. Do not put customer data,
credentials or unnecessary personal information in records. Future V2 retrieval must be separately
authorized, tenant-scoped and provenance-preserving; V1 does not implement it.
