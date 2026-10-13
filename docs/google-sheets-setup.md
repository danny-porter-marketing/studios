# Google Sheets setup (one time, about 15 minutes)

Lets the `sheets-dashboard` skill create Google Sheets directly from a Claude Code cloud session. Free: no billing account needed.

The credential uses the `drive.file` scope, so it can only see files it creates. It can't read anything else in your Drive.

---

## Part A: Google Cloud (about 8 minutes)

Sign in to Google with the account whose Drive should hold the dashboards.

1. Go to **console.cloud.google.com**. Accept the terms if asked. Skip any free trial or billing prompt.
2. **Create a project:** project picker at the top > **New project** > name it `studios` > **Create**. Make sure it's selected in the picker.
3. **Turn on the Drive API:** search bar at the top > type `Google Drive API` > open it > **Enable**.
4. **Set up the consent screen:** search `Google Auth Platform` (older UI: **APIs & Services > OAuth consent screen**) > **Get started**.
   - App name: `Studios`. Support email: yours. **Next**.
   - Audience: **External**. **Next**.
   - Contact email: yours. **Next**. Tick the agreement. **Create**.
5. **Stop the token expiring:** go to **Audience** > **Publish app** > **Confirm**. (Apps left in "Testing" issue tokens that stop working after 7 days.)
6. **Create the client:** go to **Clients** (older UI: **Credentials > Create credentials > OAuth client ID**) > **Create client**.
   - Application type: **Web application**
   - Name: `studios`
   - Under **Authorised redirect URIs** click **Add URI** and paste: `https://developers.google.com/oauthplayground`
   - **Create**.
7. Copy the **Client ID** and **Client secret** into a note. Download the JSON too: newer consoles only show the secret once.

## Part B: Get the refresh token (about 3 minutes)

8. Go to **developers.google.com/oauthplayground**.
9. Click the **gear icon** (top right) > tick **Use your own OAuth credentials** > paste the Client ID and Client secret > close the panel.
10. In the left panel, find the box at the bottom (**Input your own scopes**) and paste: `https://www.googleapis.com/auth/drive.file` > **Authorize APIs**.
11. Sign in with the same Google account. If you see **Google hasn't verified this app**, click **Advanced** > **Go to Studios (unsafe)**. It's your own app. Click **Continue**.
12. Back in the Playground, Step 2: click **Exchange authorization code for tokens**.
13. Copy the **Refresh token** (starts with `1//`). Copy all of it.

## Part C: Claude Code (about 2 minutes)

14. Go to **claude.ai/code**. Open the environment selector, hover over your environment and click the **settings icon**.
15. In **Environment variables**, paste (one per line, no spaces around `=`):
    ```
    GOOGLE_CLIENT_ID=your-client-id
    GOOGLE_CLIENT_SECRET=your-client-secret
    GOOGLE_REFRESH_TOKEN=your-refresh-token
    ```
16. Optional, saves time each session. In **Setup script**, paste:
    ```
    pip install --quiet google-api-python-client google-auth google-auth-oauthlib pandas openpyxl
    ```
17. Leave **Network access** on **Trusted**. Google's API (`*.googleapis.com`) is already allowed.
18. Save.

## Part D: Test

Start a **new** session on the `studios` repo and say:

```
Run: python .claude/skills/sheets-dashboard/scripts/upload_to_sheets.py --check
```

"Google credential OK." means it works. Then run the dashboard skill as normal: it ends with a Google Sheets link instead of an .xlsx.

---

## Troubleshooting

- **redirect_uri_mismatch** in the Playground: the redirect URI in step 6 is missing or has a typo. Edit the client and fix it.
- **invalid_grant** later: the refresh token expired (app still in Testing) or was revoked. Repeat Part B and replace `GOOGLE_REFRESH_TOKEN`.
- **access_denied** at sign-in: the app is in Testing and your account isn't a test user. Either publish the app (step 5) or add yourself under **Audience > Test users**.

## Security notes

- Anyone who can use the Claude Code environment can read its environment variables. Keep it a personal environment.
- To revoke access at any time: **myaccount.google.com/permissions** > Studios > **Remove access**.
- Never commit these values to the repo.
