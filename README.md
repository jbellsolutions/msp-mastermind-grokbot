# MSP Mastermind: GrokBot pack

One Grok bot that gets people signed up for a mastermind of managed service provider owners, and keeps the ones who join.

**Install:** paste this into one new Grok bot.

> Install the MSP Mastermind bot. Download https://github.com/jbellsolutions/msp-mastermind-grokbot/releases/latest/download/msp-mastermind.zip, unpack it into /workspace/msp-mastermind/repo/, run python3 /workspace/msp-mastermind/repo/tools/install.py and do what it prints, in order. Ask me nothing until it is all done, then send me one message that ends with the checklist. Nothing sends or posts until I say yes.

Version 1.0.0. The pack holds no names, prices or lists: the bot takes those from you in chat.

## How it works

The bot only orchestrates. Each routine hands one job to the **Claude Code CLI** (`tools/job.py`), with the **Codex CLI** as the second engine, so the work runs on your own subscriptions and not on Grok usage.

| Job | What it does | When (UTC) |
|---|---|---|
| [list](jobs/list.md) | Who belongs in the room: your own people first, scored with a reason | 12:10 weekdays |
| [invite](jobs/invite.md) | First messages and short follow-ups, one person at a time | 13:10 weekdays |
| [replies](jobs/replies.md) | Every reply answered in draft and moved one step | 12:40, 15:40, 18:40, 21:40 daily |
| [calls](jobs/calls.md) | A brief before each conversation, the next step after it | 12:20 weekdays |
| [members](jobs/members.md) | Welcome, next session, who else belongs | 15:10 Monday |
| [content](jobs/content.md) | Posts, a talk idea, the invitation page | 14:10 Monday, Wednesday, Friday |
| [report](jobs/report.md) | Seats, what moved, what waits on you | 23:30 daily |

## What is in the pack

| | |
|---|---|
| [INSTALL.md](INSTALL.md), [CHECKLIST.md](CHECKLIST.md) | The one line; everything only you can do |
| [playbook/](playbook/) | The voice, the path from a name to a seat, the blank owner.md |
| [tools/council.py](tools/council.py) | The people list, the stages, what may go out, the export for a cold-email tool, the invitation page |
| `tools/job.py`, `skills/claude-code-cli/` | Hands every job to Claude Code, then Codex, and counts which engine did it |
| `guards/`, `convlog/` | The send switch, the opt-out list, the log of every draft, send and reply |
| `tools/install.py`, `team.py`, `check.py`, `selftest.py` | The installer and the checks |
