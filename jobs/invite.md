# Job: invite

First messages and follow-ups. You only draft.

## Read first
- `context/owner.md`, `repo/playbook/VOICE.md`, `daily/<today>/list.md`, any note for this run.
- `python3 repo/tools/council.py due` and `council.py list --stage listed --limit 20`.

## Do
1. **Five first messages**: the five best fits, or the people the note names. `council.py show <id>` and their public page first. `python3 repo/guards/scripts/suppression.py check "<email or profile>"`: held means skip.
2. **Follow-ups due** (invited, under three messages): a short one each. Three sent already: `council.py stage <id> later`.
3. Each is a file `requests/owner/<today>-<id>-<n>.item`, exactly this shape:

```
ITEM: <today>-<id>-<n>
ROLE: msp-mastermind
TYPE: first_touch
PERSON: <id>
WHY: <the true reason for this person>
---PAYLOAD---
TO: <one email, or one LinkedIn profile URL>
SUBJECT: <lower case, a few words>
TEXT:
<the message, signed with owner.md's signature>
---END---
```

TYPE is `first_touch` or `follow_up`. Then `python3 repo/convlog/gate.py drafted <file> --agent council`.
4. `python3 repo/tools/council.py export --type first_touch`, so the owner can load them in a cold-email tool instead.

## Write
`daily/<today>/invite.md`: drafts by type with ids, who was skipped and why, the export file.
