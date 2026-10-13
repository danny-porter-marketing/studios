#!/usr/bin/env python3
"""
Export approved outbound sequences to import files for Instantly (email) and
HeyReach (LinkedIn), with each contact's personalised copy stored as custom
variables. The sending tool's sequence is then just {{t1_body}} etc., so every
contact gets their own copy while the tool handles timing and sending.

Usage:
    python export_sequences.py --sequences campaigns/<name>/outbound \
        --contacts campaigns/<name>/contacts.csv --out campaigns/<name>/export \
        [--html-breaks]

contacts.csv columns:
    sequence     file name in --sequences, without .md (e.g. halvard-pay)
    first_name, last_name, email, linkedin_url, company, title

Sequence files follow craft-guidelines/outbound-sequence.md:
    ## Touch N · Day D · Email | LinkedIn ...
    **Subject:** ...           (email touches)
    body...

Writes:
    instantly.csv          email leads + t{N}_subject / t{N}_body variables
    heyreach.csv           LinkedIn leads + linkedin_note variable
    sequence-setup.md      what to put in each step of each tool
    export-report.md       validation results; fix every BLOCKING item before import
Never launches anything. Import into a paused campaign, check, then a person launches.
"""
import argparse
import csv
import re
from pathlib import Path

BANNED = ["leverage", "unlock", "seamless", "cutting-edge", "ai-powered", "delve", "robust",
          "innovative", "synergy", "paradigm", "holistic", "disruptive", "groundbreaking",
          "world-class", "best-in-class", "empower", "streamline", "ecosystem", "utilize",
          "facilitate", "rockstar", "ninja", "game-changing", "revolutionary", "transformative"]
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
HEAD_RE = re.compile(r"^##\s+Touch\s+(\d+)\s*·\s*Day\s+(\d+)\s*·\s*(.+)$")


def parse_sequence(path):
    touches, cur = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEAD_RE.match(line.strip())
        if m:
            cur = {"n": int(m.group(1)), "day": int(m.group(2)),
                   "channel": "linkedin" if "linkedin" in m.group(3).lower() else "email",
                   "subject": "", "lines": []}
            touches.append(cur)
            continue
        if cur is None:
            continue
        s = line.strip()
        if s.startswith("## "):          # next non-touch section (e.g. Audit)
            cur = None
            continue
        if s.startswith("**Subject:**"):
            cur["subject"] = s.replace("**Subject:**", "").strip()
        elif s == "---" or (s.startswith("*(") and s.endswith(")*")):
            continue
        else:
            cur["lines"].append(line.rstrip())
    for t in touches:
        body = "\n".join(t.pop("lines")).strip()
        t["body"] = re.sub(r"\n{3,}", "\n\n", body)
    return touches


def check_copy(text):
    issues = []
    if "\u2014" in text:
        issues.append("em dash")
    low = text.lower()
    issues += [f"banned word '{w}'" for w in BANNED if re.search(rf"\b{re.escape(w)}\b", low)]
    if "{{" in text or "}}" in text:
        issues.append("unfilled placeholder")
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sequences", required=True)
    ap.add_argument("--contacts", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--html-breaks", action="store_true", help="Convert line breaks to <br> for tools that need HTML")
    a = ap.parse_args()

    seq_dir, out = Path(a.sequences), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    contacts = list(csv.DictReader(open(a.contacts, encoding="utf-8")))

    blocking, warnings, inst_rows, hr_rows = [], [], [], []
    email_steps, li_steps, seen_emails = {}, {}, set()

    for c in contacts:
        who = f"{c.get('first_name', '')} {c.get('last_name', '')} ({c.get('sequence', '?')})".strip()
        path = seq_dir / f"{c.get('sequence', '')}.md"
        if not path.exists():
            blocking.append(f"{who}: no sequence file {path}")
            continue
        touches = parse_sequence(path)
        if not touches:
            blocking.append(f"{who}: no touches found in {path.name}")
            continue
        for f in ("first_name", "last_name"):
            if not c.get(f):
                blocking.append(f"{who}: missing {f}")

        emails = [t for t in touches if t["channel"] == "email"]
        lis = [t for t in touches if t["channel"] == "linkedin"]
        fix = (lambda s: s.replace("\n", "<br>")) if a.html_breaks else (lambda s: s)

        if emails:
            e = (c.get("email") or "").strip()
            if not EMAIL_RE.match(e):
                blocking.append(f"{who}: missing or invalid email '{e}'")
            elif e.lower() in seen_emails:
                blocking.append(f"{who}: duplicate email {e}")
            seen_emails.add(e.lower())
            row = {"email": e, "first_name": c.get("first_name", ""), "last_name": c.get("last_name", ""),
                   "company_name": c.get("company", ""), "title": c.get("title", "")}
            for t in emails:
                k = f"t{t['n']}"
                row[f"{k}_subject"], row[f"{k}_body"] = t["subject"], fix(t["body"])
                email_steps[k] = t["day"]
                words = len(t["body"].split())
                if words > 120:
                    warnings.append(f"{who}: touch {t['n']} is {words} words (craft guide limit 120)")
                if not t["subject"]:
                    blocking.append(f"{who}: touch {t['n']} has no subject")
                for i in check_copy(t["subject"] + "\n" + t["body"]):
                    blocking.append(f"{who}: touch {t['n']}: {i}")
            inst_rows.append(row)

        if lis:
            url = (c.get("linkedin_url") or "").strip()
            if "linkedin.com/in/" not in url:
                blocking.append(f"{who}: missing LinkedIn profile URL (HeyReach drops these silently)")
            note = lis[0]["body"]
            if len(note) > 300:
                blocking.append(f"{who}: LinkedIn note is {len(note)} characters (LinkedIn limit 300)")
            elif len(note) > 200:
                warnings.append(f"{who}: LinkedIn note is {len(note)} characters (craft guide: under 200)")
            for i in check_copy(note):
                blocking.append(f"{who}: LinkedIn note: {i}")
            li_steps["linkedin_note"] = lis[0]["day"]
            hr_rows.append({"profileUrl": url, "firstName": c.get("first_name", ""), "lastName": c.get("last_name", ""),
                            "companyName": c.get("company", ""), "position": c.get("title", ""),
                            "linkedin_note": note})

    def write(name, rows):
        if not rows:
            return
        cols = list(dict.fromkeys(k for r in rows for k in r))
        with open(out / name, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(rows)

    write("instantly.csv", inst_rows)
    write("heyreach.csv", hr_rows)

    setup = ["# Sequence setup", "", "Import into a **paused** campaign. Send a test to yourself. A person launches.", ""]
    if email_steps:
        setup += ["## Instantly (email)", "", "Import `instantly.csv`. Map the extra columns as custom variables.", "",
                  "| Step | Delay from start | Subject | Body |", "|---|---|---|---|"]
        for k in sorted(email_steps, key=lambda x: int(x[1:])):
            setup.append(f"| {k} | day {email_steps[k]} | `{{{{{k}_subject}}}}` | `{{{{{k}_body}}}}` |")
        setup += ["", "Steps after the first: Instantly sets delays between steps, so enter the gap from the previous step.", ""]
    if li_steps:
        setup += ["## HeyReach (LinkedIn)", "", "Import `heyreach.csv` (or push via the API's add-leads-to-campaign endpoint with `customUserFields`).", "",
                  f"Connection request on day {li_steps['linkedin_note']}, message: `{{linkedin_note}}` (add it from the variable dropdown).", ""]
    (out / "sequence-setup.md").write_text("\n".join(setup), encoding="utf-8")

    rep = ["# Export report", "",
           f"Contacts in: {len(contacts)}  |  Instantly leads: {len(inst_rows)}  |  HeyReach leads: {len(hr_rows)}", "",
           f"## Blocking ({len(blocking)})", ""] + ([f"- {b}" for b in blocking] or ["- none"]) + \
          ["", f"## Warnings ({len(warnings)})", ""] + ([f"- {w}" for w in warnings] or ["- none"]) + \
          ["", "## Verdict", "", "**Fix blocking items before importing.**" if blocking else "**Ready to import into paused campaigns.**"]
    (out / "export-report.md").write_text("\n".join(rep), encoding="utf-8")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
