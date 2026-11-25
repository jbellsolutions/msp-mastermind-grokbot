#!/usr/bin/env python3
"""Proves the plumbing on made-up people in a scratch folder: the list, the stages, the opt-out, the send switch, the page."""
import os, pathlib, subprocess, sys, tempfile
REPO = pathlib.Path(__file__).resolve().parent.parent
bad, n = [], [0]
with tempfile.TemporaryDirectory() as t:
    ws = pathlib.Path(t); env = dict(os.environ, BOT_HOME=t)
    for d in ("context", "data", "state", "requests/owner", "content"):
        (ws / d).mkdir(parents=True)
    (ws / "context/suppression.csv").write_text("# opt-outs\nno@example.com,said no,2026-01-01\n")
    (ws / "context/routines-on.md").write_text("Council invitations: test\n")
    (ws / "context/standing-approvals.md").write_text("# approved\n")
    def run(script, *a):
        r = subprocess.run([sys.executable, str(REPO / script), *a], env=env, capture_output=True, text=True); return r.returncode, r.stdout + r.stderr
    def ok(name, cond):
        n[0] += 1
        if not cond: bad.append(name)
    C = "tools/council.py"
    (ws / "in.csv").write_text("First Name,Last Name,Email Address,Company Name\nAda,Test,ada@example.com,Test IT\nBo,Test,no@example.com,Gone IT\nAda,Test,ADA@example.com,Test IT\n")
    ok("import adds one, skips the opt-out and the duplicate", "added 1, skipped 2" in run(C, "import", str(ws / "in.csv"), "--source", "selftest")[1])
    run(C, "fit", "p0001", "5", "runs an MSP, test row")
    ok("list shows fit", "fit 5" in run(C, "list")[1])
    item = ws / "requests/owner/i1.item"
    item.write_text("ITEM: i1\nROLE: msp-mastermind\nTYPE: first_touch\nPERSON: p0001\n---PAYLOAD---\nTO: ada@example.com\nSUBJECT: hello\nTEXT:\nHi Ada.\n---END---\n")
    ok("draft is logged", "logged" in run("convlog/gate.py", "drafted", str(item), "--agent", "council")[1])
    ok("nothing goes out on test", "i1.item" not in run(C, "outbox", "--routine", "Council invitations")[1])
    (ws / "context/standing-approvals.md").write_text("first_touch: auto 2026-01-01 yes\n")
    ok("approved type still held while the routine is on test", "i1.item" not in run(C, "outbox", "--routine", "Council invitations")[1])
    (ws / "context/routines-on.md").write_text("Council invitations: on\n")
    ok("approved and on: it may go", "i1.item" in run(C, "outbox", "--routine", "Council invitations")[1])
    (ws / "context/STOP").write_text(""); ok("STOP holds everything", "i1.item" not in run(C, "outbox", "--routine", "Council invitations")[1]); (ws / "context/STOP").unlink()
    ok("export", "1 rows" in run(C, "export", "--type", "first_touch")[1])
    run(C, "done", str(item)); ok("done moves the person to invited", "invited" in run(C, "list")[1])
    ok("sent line passes the log's audit", run("convlog/convlog.py", "audit")[0] == 0)
    run(C, "stage", "p0001", "joined", "paid"); ok("stats", "joined 1" in run(C, "stats", "--days", "1")[1])
    run(C, "stage", "p0001", "no", "asked to stop"); ok("no goes on the opt-out list", run("guards/scripts/suppression.py", "check", "ada@example.com")[0] == 1)
    ok("page waits for owner.md", run(C, "page")[0] == 1)
    (ws / "context/owner.md").write_text("name: Test <Council>\nhost: A Host\npromise: Peers helping peers\nbooking_link: https://example.com/book\nprice: 1\nshow_price: no\n")
    run(C, "page"); p = (ws / "content/invitation.html").read_text() if (ws / "content/invitation.html").exists() else ""
    ok("page is written, escaped, with the price hidden", "Test &lt;Council&gt;" in p and "https://example.com/book" in p and "Membership" not in p)
print(f"ok: {n[0]} checks" if not bad else "FAILED: " + "; ".join(bad))
sys.exit(1 if bad else 0)
