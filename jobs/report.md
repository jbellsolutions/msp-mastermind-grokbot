# Job: report

The night's count and tomorrow's one thing.

## Run and read
- `python3 repo/tools/council.py stats --days 1`, `council.py stats --days 7`, `council.py due`.
- `python3 repo/tools/job.py audit --days 1`, `python3 repo/convlog/gate.py day`, `python3 repo/guards/scripts/beat.py status`.
- `context/owner.md` (goal), today's `daily/<today>/*.md`, `requests/owner/` (oldest first), `context/routines-on.md`, `context/standing-approvals.md`.

## Write `daily/<today>/report.md`, under 180 words

```
<mastermind name>, <date>
Seats: N joined of N. Goal: <goal line>.
Today: N messages sent, N replies, N calls booked, N held, N invited in, N joined. Ready and waiting on you: N.
Week: the same five numbers.
Best next person: <id and the reason>
Waiting on you: the three oldest, one line each, with the file
Tomorrow: the one thing most likely to fill a seat
Engines: Claude Code N jobs, Codex N, the bot itself N
```

Sent means an app confirmed it. No owner.md: the first line of "Waiting on you" is to fill it in. Nothing can go out until a type is approved and its routine is on: say which switch is next, once.

## Also write
`vault/Daily/<today>.md`: the report. On Fridays, one line in `vault/Decisions.md`: which source gave the most replies and calls, and what to do more of.
