# Job: speaker

Get the owner on shows and stages. You only draft.

## Read first
- `context/owner.md` (topics, host_bio), `repo/playbook/FUNCTIONS.md` (speaker), `VOICE.md`, `ITEM.md`; `repo/agents/speaker/PROCESS.md` and its `prompts/`.
- `python3 repo/tools/team.py inbox speaker`, `python3 repo/tools/people.py due --lane speaker`, `people.py list --lane speaker`.

## Do
1. **Find** up to five shows, events or chapters the buyers listen to, active in the last two months: `people.py add --name "<host>" --company "<show>" ... --source "<page>" --why "<recent episode and the angle>" --lane speaker`, then `people.py fit`.
2. **Pitch** up to three at fit 4 or 5: a recent episode, one angle, three things the audience leaves with. TYPE `show_pitch`. A show with a form: the filled answers in `requests/owner/form-<id>.md` with the form's link.
3. **Follow-ups due:** TYPE `show_follow_up`.
4. **Booked or aired:** one line in `requests/owner/appearances.md`, and `team.py give content "<what aired>" --from speaker`.

## Write
`daily/<today>/speaker.md`: shows found, pitches with ids, forms ready, booked.
