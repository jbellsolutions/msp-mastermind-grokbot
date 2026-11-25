# Job: list

Decide who could sit in the room. Quality over number.

## Read first
- `context/owner.md` (if it is missing, say "practice" at the top of the daily file and use made-up people in `data/practice.csv` only).
- `repo/playbook/PATH.md`, what makes a fit. `python3 repo/tools/council.py stats --days 7`.

## Do
1. **The owner's own people first.** For every file in `data/contacts/` not yet in `state/imported.txt`: `python3 repo/tools/council.py import <file> --source "<what it is>"`, then add its name to that file. The sources that work best: people the owner met, alumni and member directories the owner belongs to, past clients' IT providers, the owner's own newsletter.
2. **Score** up to 25 people with no fit yet (`council.py list --stage listed`): `council.py fit <id> <0-5> "<reason>"`. 5 runs an MSP and brings something the room lacks; 3 runs one; 1 is adjacent; 0 is not a fit (then `council.py stage <id> later "not a fit"`). Use what the list says and their public website. No paid data, nothing guessed.
3. **Only if fewer than 10 people are listed at 4 or 5:** up to 5 new ones from public pages (MSP community speakers, podcast guests, chapter leaders, association boards), each with the page in `--why`. `council.py add --name ... --company ... --linkedin ... --source "<page>" --why "<reason>"`.
4. **Gaps.** Which verticals, specialties and regions the joined and offered people cover, and which are missing.

## Write
`daily/<today>/list.md`: how many added, scored and at 4 or 5 (counts and ids); the gaps; the five to invite next, by id, with the reason.
