#!/usr/bin/env python3
"""
Upload an .xlsx to Google Drive and convert it to a native Google Sheet.

Sends the file straight to the Drive API, so large datasets don't have to pass
through Claude's context the way they do with the Drive connector.

One-time setup (about 10 minutes):
  1. Go to https://console.cloud.google.com, create a project (e.g. "studios-sheets").
  2. APIs & Services > Library > enable "Google Drive API".
  3. APIs & Services > OAuth consent screen > External, add your own Gmail as a test user.
  4. APIs & Services > Credentials > Create credentials > OAuth client ID > "Desktop app".
  5. Download the JSON and save it as  ~/.studios/google_credentials.json
  6. pip install google-api-python-client google-auth-oauthlib
  The first run opens a browser to sign in. After that a token is cached in
  ~/.studios/google_token.json and runs are silent.

Usage:
    python upload_to_sheets.py dashboard.xlsx "Sheet title" [--folder FOLDER_ID]
Prints the Google Sheets URL.
"""
import argparse
import sys
from pathlib import Path

SCOPES = ["https://www.googleapis.com/auth/drive.file"]  # only files this script creates
HOME = Path.home() / ".studios"
CREDS = HOME / "google_credentials.json"
TOKEN = HOME / "google_token.json"
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


def service():
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        sys.exit("Missing libraries. Run: pip install google-api-python-client google-auth-oauthlib")
    if not CREDS.exists():
        sys.exit(f"No credentials at {CREDS}. See setup steps at the top of this script.")
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES) if TOKEN.exists() else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = InstalledAppFlow.from_client_secrets_file(str(CREDS), SCOPES).run_local_server(port=0)
        HOME.mkdir(exist_ok=True)
        TOKEN.write_text(creds.to_json())
    return build("drive", "v3", credentials=creds)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("xlsx")
    p.add_argument("title")
    p.add_argument("--folder", help="Drive folder ID to put the sheet in")
    a = p.parse_args()
    from googleapiclient.http import MediaFileUpload

    meta = {"name": a.title, "mimeType": "application/vnd.google-apps.spreadsheet"}
    if a.folder:
        meta["parents"] = [a.folder]
    media = MediaFileUpload(a.xlsx, mimetype=XLSX, resumable=True)
    f = service().files().create(body=meta, media_body=media, fields="id,webViewLink").execute()
    print(f["webViewLink"])


if __name__ == "__main__":
    main()
