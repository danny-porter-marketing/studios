# Account Tiers

Tiers decide how much time and money each account gets. Set by the ICP score (`abm/icp-scoring.md`).

---

```
                 Tier 1: 1:1              Tier 2: 1:few             Tier 3: 1:many
------------------------------------------------------------------------------------------------
Accounts         Max 25 at a time         50 to 150                 Everyone else in ICP
Research         Full account file        Short account file        None, list-level data
Contacts         3 to 5, multi-threaded   1 to 3                    Ad audiences
Outreach         Custom sequence per      Sequence per contact,     Ads, newsletter,
                 contact, from Piotr or   personalised by signal    event invites
                 Marta                    and industry
Assets           Custom one-pager or      Industry case study,      Blog, guides, checklists
                 landing page             industry landing page
Owner            Named sales lead +       Sales team                Marketing
                 marketing
Review           Weekly                   Weekly                    Monthly
Success          Scoping call in 60 days  Reply or meeting in 30    Engagement, then score
                                          days                      upgrade
```

---

## Moving between tiers

- **Up:** a new intent signal pushes the score over a threshold. Move within 48 hours, run `account-research`, start the play.
- **Down:** 90 days in Tier 1 with no engagement moves an account to Tier 2. 90 days in Tier 2 moves it to Tier 3.
- **Out:** lost deals go to Watch for 6 months, then re-score.

## Rules

- Tier 1 never exceeds 25 accounts. If a new one comes in, the weakest one moves down.
- Every Tier 1 account has a file in `accounts/`.
- Tier is a CRM field (see `revops/crm-conventions.md`), not a spreadsheet nobody updates.
