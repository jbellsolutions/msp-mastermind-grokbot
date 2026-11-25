# Install

One line, pasted into one new Grok bot:

> Install the MSP Mastermind bot. Download https://github.com/jbellsolutions/msp-mastermind-grokbot/releases/latest/download/msp-mastermind.zip, unpack it into /workspace/msp-mastermind/repo/, run python3 /workspace/msp-mastermind/repo/tools/install.py and do what it prints, in order. Ask me nothing until it is all done, then send me one message that ends with the checklist. Nothing sends or posts until I say yes.

That is the whole install for the owner. The rest of this page is what the bot does.

**Already have an owner.md?** Attach it to the same message. The bot saves it as `/workspace/msp-mastermind/context/owner.md` after step 1.

**Update.** Paste the same line again. Files in `context/`, `data/` and `requests/` are kept.

## What the bot does

1. **Unpack and run the installer.** It makes the workspace, the switch files and the setup page, runs the checks and prints the next steps. It asks nothing and can be run again.
2. **Set itself up.** `python3 /workspace/msp-mastermind/repo/tools/team.py setup` prints the memory to save, the skill to save, the seven routines to create, and one command to run.
3. **Install the two CLIs** and run `python3 /workspace/msp-mastermind/repo/tools/job.py status`.
4. **Send the owner one message**: what is set up, what `job.py status` said, any failed check, then the whole checklist from `requests/owner/CHECKLIST.md`, starting `NEEDS YOU:`. Then stop.

## What can go wrong, and what to do

| If | Then |
|---|---|
| The download fails | Ask the owner once to attach `msp-mastermind.zip` from the release, then carry on from step 1 |
| A CLI will not install or does not answer | Carry on. Each job falls to the bot itself and is recorded as such, until the owner signs it in |
| A check fails | Carry on, and put the failed line in the one message |

## What is on after the install

Every routine runs on **test**: its job runs and makes drafts. A message goes out only when its type says auto and its routine is on, and never to someone who opted out. The owner changes a switch by saying it in the bot's chat.
