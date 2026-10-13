#!/usr/bin/env python3
"""
Upload an .xlsx to Google Drive and convert it to a native Google Sheet.

Sends the file straight to the Drive API, so large datasets never pass through
Claude's context the way they do with the Drive connector.

Credentials, checked in this order:

  1. Environment variables (cloud sessions, e.g. Claude Code on the web)
       GOOGLE_CLIENT_ID
       GOOGLE_CLIENT_SECRET
       GOOGLE_REFRESH_TOKEN
     Set them in the cloud environment's "Environment variables" box.
     The refresh token comes from the OAuth Playground with your own client
     (see docs/google-sheets-setup.md). Network: *.googleapis.com is in the
     default Trusted allowlist, so no network change is needed.

  2. Local files (running on your own computer)
       ~/.studios/google_credentials.json   OAuth client JSON ("Desktop app")
       ~/.studios/google_token.json         created on first run via browser sign-in

Scope is drive.file: the credential can only see files this script creates,
nothing else in your Drive.

Usage:
    python upload_to_sheets.py dashboard.xlsx "Sheet title" [--folder FOLDER_ID]
    python upload_to_sheets.py --check        # test the credential, upload nothing
Prints the Google Sheets URL.
"""
import argparse
import os
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/drive.file"]
HOME = Path.home() / ".studios"
CREDS = HOME / "google_credentials.json"
TOKEN = HOME / "google_token.json"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
TOKEN_URI = "https://oauth2.googleapis.com/token"


def credentials():
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
    except ImportError:
        sys.exit("Missing libraries. Run: pip install google-api-python-client google-auth google-auth-oauthlib")

    env = {k: os.environ.get(k) for k in ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REFRESH_TOKEN")}
    if all(env.values()):
        creds = Credentials(
            token=None,
            refresh_token=env["GOOGLE_REFRESH_TOKEN"],
            client_id=env["GOOGLE_CLIENT_ID"],
            client_secret=env["GOOGLE_CLIENT_SECRET"],
            token_uri=TOKEN_URI,
            scopes=SCOPES,
        )
        try:
            creds.refresh(Request())
        except Exception as e:  # noqa: BLE001
            sys.exit(
                "Google rejected the stored credential. Usually the refresh token has expired "
                "(tokens from an app left in 'Testing' last 7 days) or was copied incompletely. "
                f"Get a new one from the OAuth Playground. Detail: {e}"
            )
        return creds
    if any(env.values()):
        missing = [k for k, v in env.items() if not v]
        sys.exit(f"Some Google variables are set but these are missing: {', '.join(missing)}")

    if not CREDS.exists():
        sys.exit(
            "No Google credential found. In a cloud session, set GOOGLE_CLIENT_ID, "
            "GOOGLE_CLIENT_SECRET and GOOGLE_REFRESH_TOKEN in the environment's variables. "
            f"Locally, save an OAuth client JSON to {CREDS}. See docs/google-sheets-setup.md."
        )
    from google_auth_oauthlib.flow import InstalledAppFlow

    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES) if TOKEN.exists() else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = InstalledAppFlow.from_client_secrets_file(str(CREDS), SCOPES).run_local_server(port=0)
        HOME.mkdir(exist_ok=True)
        TOKEN.write_text(creds.to_json())
    return creds


def main():
    p = argparse.ArgumentParser()
    p.add_argument("xlsx", nargs="?")
    p.add_argument("title", nargs="?")
    p.add_argument("--folder", help="Drive folder ID to put the sheet in")
    p.add_argument("--check", action="store_true", help="Test the credential without uploading")
    a = p.parse_args()

    creds = credentials()
    if a.check:
        print("Google credential OK.")
        return
    if not a.xlsx or not a.title:
        p.error("xlsx and title are required unless --check is used")

    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    meta = {"name": a.title, "mimeType": "application/vnd.google-apps.spreadsheet"}
    if a.folder:
        meta["parents"] = [a.folder]
    media = MediaFileUpload(a.xlsx, mimetype=XLSX, resumable=True)
    drive = build("drive", "v3", credentials=creds, cache_discovery=False)
    f = drive.files().create(body=meta, media_body=media, fields="id,webViewLink").execute()
    print(f["webViewLink"])


if __name__ == "__main__":
    main()
