# NEEDS YOU

Everything only the owner can do, in one list. The bot works on drafts without any of it.

| # | What | The exact step | Unblocks |
|---|---|---|---|
| 1 | [ ] Your details | Send the bot your `owner.md`, or say the details and it fills in `context/owner.md`: name, host, who it's for, format, seats, price and how it's paid, goal, booking link, who books, signature | Drafts as you instead of practice |
| 2 | [ ] Claude Code and Codex | Say "CLI status". If either is "not answering": for Claude Code run `claude setup-token` on your own computer and give the token at the hidden prompt (saved as `CLAUDE_CODE_OAUTH_TOKEN`), or sign in from the bot's terminal; for Codex run `codex login` in the bot's terminal | The work running on your subscriptions |
| 3 | [ ] Three names | Tell the bot three people you would invite today, and why each one | The first messages, with no list and no inboxes needed |
| 4 | [ ] Your lists | Send the files: contacts, directory exports, event attendees, newsletter. Any CSV | The warm list |
| 5 | [ ] Mailbox, calendar, LinkedIn | Sign the bot's browser or connected apps in to the ones it may read and send from | Replies read, calls briefed, messages sent |
| 6 | [ ] Say yes to the first messages | Read the drafts in `requests/owner/`. Change what you want. Then say "first_touch: auto" and "Council invitations: on" | Messages going out |
| 7 | [ ] People to leave alone | Send your opt-outs and anyone the bot should never invite | Nobody gets a message they shouldn't |
| 8 | [ ] How members pay | Your own checkout or invoice. The bot never takes payment; put the line in owner.md `payment` | Joining |
| 9 | [ ] The invitation page | Say "make the page", read `content/invitation.html`, and publish it where you like | A link to send after a good call |

## The switches that make it run without you

After you have seen a type's drafts, say "<type>: auto": `first_touch`, `follow_up`, `reply`, `invitation`, `member_note`, `host_pitch`. Say "<routine>: on" to take a routine off test. Say "stop" to stop everything. Price, terms, payment and anyone upset stay with you.
