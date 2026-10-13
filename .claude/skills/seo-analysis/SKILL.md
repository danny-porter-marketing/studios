---
name: seo-analysis
description: Analyse SEO and website analytics data (Semrush or Ahrefs keyword exports, Search Console, GA4 exports) to choose keywords, find quick wins and content gaps, spot cannibalisation, and judge which pages and channels drive conversions, with all maths in code. Use when given keyword, traffic, GA4 or Search Console data, or asked which keywords to target or how the website is performing.
---

# SEO and web analytics

Same rules as every analysis in Studios: profile before cleaning, clean with code, calculate with code, state assumptions, end with decisions. Tools like Semrush and GA4 estimate and sample; say so.

## 1. Save and profile
Save the export as given to `analysis/YYYY-MM-DD-<name>/raw/`. Profile it with a short pandas script: rows, duplicates (including case differences in keywords), blanks, numbers stored as text, unusual sources, date coverage. Tell the operator what you found before cleaning.

## 2a. Keyword data (Semrush, Ahrefs, Search Console)

**Decide the filters first, and show them:**
- `--brand`: the brand's own name. Brand terms are defended, not targeted.
- `--exclude`: words that signal the wrong audience. For Corvane: jobs, careers, salary (job seekers), cheap, freelance, wordpress (wrong buyer). Check each against the persona files: would a CTO or VP Engineering search this?
- `clusters.json`: topic groups that map to one page each. List specific clusters before broad ones; first match wins. Start from `examples/clusters.json`.

**Run:**
```
python <skill>/scripts/seo_analysis.py keywords <export.csv> --brand <name> \
  --exclude <words> --clusters <clusters.json> --out analysis/<folder>
```

**Interpret:**
- **Quick wins** (ranking 4 to 20, achievable difficulty): improve the page that already ranks. Usually the fastest return.
- **Content gaps** (not ranking, low difficulty): new pages or articles. Match intent: informational terms become guides (craft: blog-article), commercial terms become service or industry pages (craft: landing-page).
- **Clusters:** plan one page per cluster, not one per keyword.
- **Cannibalisation:** two URLs ranking for the same cluster split their strength. Decide which URL should own the cluster, then merge, redirect or re-target the other.
- **Long shots:** high-volume head terms you won't win soon. Say why you're not chasing them.
- **Defend:** top-3 terms. Keep them fresh; don't neglect them.

## 2b. GA4 data

**Run:**
```
python <skill>/scripts/seo_analysis.py ga4 <export.csv> --out analysis/<folder>
```

**Interpret:**
- **Spam and junk:** the script removes spam referrals and flags `(not set)`. Name them.
- **Tracking breaks:** a week where every channel drops at once is a tag problem, not a demand problem. Excluded from trends, confirmed with whoever owns the tag.
- **Traffic vs conversion:** separate pages that bring visitors from pages that convert them. Blog posts usually bring traffic and few conversions; that's their job only if they pass visitors to pages that convert. Check internal links.
- **Pages to exclude from marketing judgement:** careers and support pages attract the wrong audience.
- **Key events are not pipeline.** GA4 conversions are form submissions. Join them to the CRM (`revops/`) before judging a channel's value.

## 3. Connect the two
The best SEO plan sits where both datasets agree:
- A quick-win keyword whose ranking page already converts well in GA4 is the top priority.
- A high-traffic page that converts poorly needs a conversion fix (CTA, internal links), not more traffic.
- Content gaps that match current priorities (`priorities.md`) beat bigger gaps that don't.

## 4. Output
- Dashboard and report: build a spec from the script's CSVs and run `sheets-dashboard` (Sheet plus HTML report).
- **SEO action plan** in `analysis/<folder>/seo-plan.md`: top 5 actions, each with the keyword or cluster, target page, action (optimise, create, merge, fix conversion), expected extra clicks from the script, and the priority it serves.
- Content briefs: for each new page, add a brief to the backlog for `campaign-pack` or the blog-article craft guide.
- Experiments: title and meta description changes can be tested with `experiment-design`, as a before-and-after on a group of pages with a control group. SEO tests are slower and noisier than email tests; say so.

## Report
Data problems found and fixed, top 3 quick wins, top 3 content gaps, any cannibalisation, the channel and page story from GA4, the assumptions (click-through curve, tool estimates, key events vs pipeline), and the first 3 actions.
