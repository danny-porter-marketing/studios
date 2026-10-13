#!/usr/bin/env python3
"""
Build a Google-Sheets-ready dashboard workbook (.xlsx) from a cleaned CSV and a JSON spec.

Every number on the Summary and Dashboard tabs is a live formula that points back at the
"Clean data" tab, so anyone opening the sheet can click a cell and see how it was built.

Usage:
    python build_dashboard.py spec.json output.xlsx

Spec shape (see examples/practice_spec.json for a full example):
{
  "title": "Marketing performance, Jan to Sep 2026",
  "clean_csv": "clean.csv",            # required, already cleaned; flags as 1/0 columns
  "raw_csv": "raw.csv",                # optional, kept untouched for audit
  "extra_tables": [{"name": "Spend", "csv": "spend.csv"}],
  "kpis": [
    {"label": "Leads", "agg": "count"},
    {"label": "SQLs", "agg": "sum", "column": "is_sql"},
    {"label": "Spend", "agg": "sum_table", "table": "Spend", "column": "spend_eur", "format": "eur"},
    {"label": "Cost per SQL", "ratio": ["Spend", "SQLs"], "format": "eur"}
  ],
  "breakdowns": [
    {
      "title": "By channel",
      "group_by": "channel",
      "metrics": [
        {"label": "Leads", "agg": "count"},
        {"label": "SQLs", "agg": "sum", "column": "is_sql"},
        {"label": "Spend", "agg": "lookup", "table": "Spend", "key": "channel", "column": "spend_eur", "format": "eur"},
        {"label": "SQL rate", "ratio": ["SQLs", "Leads"], "format": "pct", "highlight": "high_good"},
        {"label": "Cost per SQL", "ratio": ["Spend", "SQLs"], "format": "eur", "highlight": "low_good"}
      ],
      "sort_by": "SQLs",
      "exclude": ["(none)"],          # optional: groups to leave out of this table
      "chart": {"metric": "Cost per SQL", "type": "bar"}
    }
  ],
  "notes": {"findings": ["..."], "cleaning": ["..."], "caveats": ["..."], "next_steps": ["..."]}
}

Formats: "int" (default), "eur", "usd", "gbp", "pln", "pct", "dec".
Highlights: "high_good" (green high, red low), "low_good" (reverse).
"""
import json
import sys
from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

NAVY = "1F2A44"
LIGHT = "EEF1F6"
MID = "C9D1DE"
WHITE = "FFFFFF"
TITLE_FONT = Font(name="Arial", size=16, bold=True, color=NAVY)
H_FONT = Font(name="Arial", size=11, bold=True, color=WHITE)
SECTION_FONT = Font(name="Arial", size=12, bold=True, color=NAVY)
BODY_FONT = Font(name="Arial", size=10)
BOLD_FONT = Font(name="Arial", size=10, bold=True)
KPI_LABEL_FONT = Font(name="Arial", size=9, color="5A6478")
KPI_VALUE_FONT = Font(name="Arial", size=18, bold=True, color=NAVY)
HEADER_FILL = PatternFill("solid", fgColor=NAVY)
TOTAL_FILL = PatternFill("solid", fgColor=LIGHT)
KPI_FILL = PatternFill("solid", fgColor=LIGHT)
THIN = Side(style="thin", color=MID)
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

FORMATS = {
    "int": "#,##0",
    "dec": "#,##0.00",
    "pct": "0.0%",
    "eur": "€#,##0",
    "usd": "$#,##0",
    "gbp": "£#,##0",
    "pln": "#,##0 \"zł\"",
}


def q(name):
    """Quote a sheet name for use in a formula."""
    return "'" + name.replace("'", "''") + "'"


def write_table(ws, df, start_row=1):
    for c, col in enumerate(df.columns, 1):
        cell = ws.cell(row=start_row, column=c, value=str(col))
        cell.font = H_FONT
        cell.fill = HEADER_FILL
    for r, row in enumerate(df.itertuples(index=False), start_row + 1):
        for c, val in enumerate(row, 1):
            if pd.isna(val):
                val = None
            elif hasattr(val, "item"):
                val = val.item()
            ws.cell(row=r, column=c, value=val).font = BODY_FONT
    ws.freeze_panes = ws.cell(row=start_row + 1, column=1)
    for c, col in enumerate(df.columns, 1):
        width = max([len(str(col))] + [len(str(v)) for v in df[col].head(200)]) + 2
        ws.column_dimensions[get_column_letter(c)].width = min(max(width, 8), 45)


class Book:
    def __init__(self, spec, base):
        self.spec = spec
        self.base = base
        self.wb = Workbook()
        self.clean = pd.read_csv(base / spec["clean_csv"])
        self.n = len(self.clean)
        self.tables = {}

    # ---- data ranges -------------------------------------------------------
    def col_range(self, column, sheet="Clean data", df=None):
        df = self.clean if df is None else df
        if column not in df.columns:
            raise SystemExit(f"Column '{column}' not found in {sheet}. Columns: {list(df.columns)}")
        letter = get_column_letter(list(df.columns).index(column) + 1)
        return f"{q(sheet)}!${letter}$2:${letter}${len(df) + 1}"

    def table_range(self, table, column):
        return self.col_range(column, sheet=table, df=self.tables[table])

    # ---- sheets ------------------------------------------------------------
    def build(self, out):
        dash = self.wb.active
        dash.title = "Dashboard"
        summary = self.wb.create_sheet("Summary")
        clean_ws = self.wb.create_sheet("Clean data")
        write_table(clean_ws, self.clean)
        for t in self.spec.get("extra_tables", []):
            df = pd.read_csv(self.base / t["csv"])
            self.tables[t["name"]] = df
            write_table(self.wb.create_sheet(t["name"]), df)
        if self.spec.get("raw_csv"):
            raw = pd.read_csv(self.base / self.spec["raw_csv"], dtype=str)
            write_table(self.wb.create_sheet("Raw data"), raw)
        self.build_summary(summary)
        self.build_dashboard(dash)
        self.build_notes(self.wb.create_sheet("Notes"))
        self.wb.save(out)

    def metric_formula(self, m, key_cell, group_by):
        agg = m.get("agg")
        if agg == "count":
            return f"=COUNTIF({self.col_range(group_by)},{key_cell})"
        if agg == "sum":
            return f"=SUMIFS({self.col_range(m['column'])},{self.col_range(group_by)},{key_cell})"
        if agg == "lookup":
            t = m["table"]
            return f"=SUMIFS({self.table_range(t, m['column'])},{self.table_range(t, m['key'])},{key_cell})"
        raise SystemExit(f"Unknown agg '{agg}' in metric {m}")

    def build_summary(self, ws):
        ws["A1"] = self.spec.get("title", "Summary")
        ws["A1"].font = TITLE_FONT
        ws["A2"] = "Every figure here is a formula on the Clean data tab."
        ws["A2"].font = KPI_LABEL_FONT
        row = 4
        self.breakdown_locs = []
        for b in self.spec.get("breakdowns", []):
            gb = b["group_by"]
            metrics = b["metrics"]
            keys = [k for k in self.clean[gb].dropna().unique().tolist() if k not in b.get("exclude", [])]
            sort_by = b.get("sort_by")
            if sort_by:
                m = next(x for x in metrics if x["label"] == sort_by)
                if m.get("agg") == "count":
                    order = self.clean[gb].value_counts()
                elif m.get("agg") == "sum":
                    order = self.clean.groupby(gb)[m["column"]].sum()
                else:
                    order = None
                if order is not None:
                    keys = sorted(keys, key=lambda k: -order.get(k, 0))
            ws.cell(row=row, column=1, value=b["title"]).font = SECTION_FONT
            row += 1
            hdr = row
            headers = [gb.replace("_", " ").title()] + [m["label"] for m in metrics]
            for c, h in enumerate(headers, 1):
                cell = ws.cell(row=hdr, column=c, value=h)
                cell.font = H_FONT
                cell.fill = HEADER_FILL
                cell.alignment = Alignment(horizontal="center" if c > 1 else "left", wrap_text=True)
            col_of = {m["label"]: get_column_letter(i + 2) for i, m in enumerate(metrics)}
            first = hdr + 1
            for i, k in enumerate(keys):
                r = first + i
                ws.cell(row=r, column=1, value=k.item() if hasattr(k, "item") else k).font = BODY_FONT
                for j, m in enumerate(metrics):
                    if "ratio" in m:
                        a, d = m["ratio"]
                        f = f"=IFERROR({col_of[a]}{r}/{col_of[d]}{r},\"\")"
                    else:
                        f = self.metric_formula(m, f"$A{r}", gb)
                    cell = ws.cell(row=r, column=j + 2, value=f)
                    cell.font = BODY_FONT
                    cell.number_format = FORMATS[m.get("format", "int")]
            last = first + len(keys) - 1
            tot = last + 1
            ws.cell(row=tot, column=1, value="Total").font = BOLD_FONT
            for j, m in enumerate(metrics):
                L = col_of[m["label"]]
                if "ratio" in m:
                    a, d = m["ratio"]
                    f = f"=IFERROR({col_of[a]}{tot}/{col_of[d]}{tot},\"\")"
                else:
                    f = f"=SUM({L}{first}:{L}{last})"
                cell = ws.cell(row=tot, column=j + 2, value=f)
                cell.number_format = FORMATS[m.get("format", "int")]
            for c in range(1, len(headers) + 1):
                ws.cell(row=tot, column=c).fill = TOTAL_FILL
                ws.cell(row=tot, column=c).font = BOLD_FONT
            for m in metrics:
                h = m.get("highlight")
                if h:
                    rng = f"{col_of[m['label']]}{first}:{col_of[m['label']]}{last}"
                    lo, hi = ("F8696B", "63BE7B") if h == "high_good" else ("63BE7B", "F8696B")
                    ws.conditional_formatting.add(
                        rng, ColorScaleRule(start_type="min", start_color=lo, mid_type="percentile",
                                            mid_value=50, mid_color="FFEB84", end_type="max", end_color=hi))
            self.breakdown_locs.append({"spec": b, "hdr": hdr, "first": first, "last": last, "col_of": col_of})
            row = tot + 3
        ws.column_dimensions["A"].width = 34
        for c in range(2, 15):
            ws.column_dimensions[get_column_letter(c)].width = 14

    def kpi_formula(self, k, cells):
        if "ratio" in k:
            a, d = k["ratio"]
            return f"=IFERROR({cells[a]}/{cells[d]},\"\")"
        agg = k.get("agg")
        if agg == "count":
            first_col = self.clean.columns[0]
            return f"=COUNTA({self.col_range(first_col)})"
        if agg == "sum":
            return f"=SUM({self.col_range(k['column'])})"
        if agg == "sum_table":
            return f"=SUM({self.table_range(k['table'], k['column'])})"
        if "formula" in k:
            return k["formula"]
        raise SystemExit(f"Unknown KPI {k}")

    def build_dashboard(self, ws):
        ws.sheet_view.showGridLines = False
        ws["B2"] = self.spec.get("title", "Dashboard")
        ws["B2"].font = TITLE_FONT
        ws["B3"] = f"{self.n:,} rows after cleaning. Click any number to see its formula."
        ws["B3"].font = KPI_LABEL_FONT
        cells = {}
        per_row = 4
        for i, k in enumerate(self.spec.get("kpis", [])):
            r = 5 + (i // per_row) * 4
            c = 2 + (i % per_row) * 3
            lab = ws.cell(row=r, column=c, value=k["label"].upper())
            val = ws.cell(row=r + 1, column=c, value=None)
            cells[k["label"]] = f"{get_column_letter(c)}{r + 1}"
            val.value = self.kpi_formula(k, cells)
            val.number_format = FORMATS[k.get("format", "int")]
            lab.font = KPI_LABEL_FONT
            val.font = KPI_VALUE_FONT
            ws.merge_cells(start_row=r, start_column=c, end_row=r, end_column=c + 1)
            ws.merge_cells(start_row=r + 1, start_column=c, end_row=r + 1, end_column=c + 1)
            for rr in (r, r + 1):
                for cc in (c, c + 1):
                    ws.cell(row=rr, column=cc).fill = KPI_FILL
            lab.alignment = Alignment(horizontal="left", indent=1)
            val.alignment = Alignment(horizontal="left", indent=1)
        for col in range(1, 16):
            ws.column_dimensions[get_column_letter(col)].width = 11
        ws.column_dimensions["A"].width = 3
        n_kpi_rows = (len(self.spec.get("kpis", [])) + per_row - 1) // per_row
        chart_row = 5 + n_kpi_rows * 4 + 1
        summary = self.wb["Summary"]
        for i, loc in enumerate(self.breakdown_locs):
            ch = loc["spec"].get("chart")
            if not ch:
                continue
            L = loc["col_of"][ch["metric"]]
            col_idx = ord(L) - 64
            chart = BarChart()
            chart.type = "bar" if ch.get("type", "bar") == "bar" else "col"
            chart.style = 10
            chart.title = f"{ch['metric']} {loc['spec']['title'].lower()}"
            chart.legend = None
            data = Reference(summary, min_col=col_idx, min_row=loc["hdr"], max_row=loc["last"])
            cats = Reference(summary, min_col=1, min_row=loc["first"], max_row=loc["last"])
            chart.add_data(data, titles_from_data=True)
            chart.set_categories(cats)
            chart.y_axis.numFmt = FORMATS[next(m for m in loc["spec"]["metrics"] if m["label"] == ch["metric"]).get("format", "int")]
            chart.y_axis.majorGridlines = None
            chart.height = 7.5
            chart.width = 16
            anchor_col = "B" if i % 2 == 0 else "I"
            anchor_row = chart_row + (i // 2) * 16
            ws.add_chart(chart, f"{anchor_col}{anchor_row}")

    def build_notes(self, ws):
        notes = self.spec.get("notes", {})
        ws["A1"] = "Notes"
        ws["A1"].font = TITLE_FONT
        ws.column_dimensions["A"].width = 110
        row = 3
        for key, label in [("findings", "What the data says"), ("cleaning", "What was cleaned and why"),
                           ("caveats", "What this data can't tell us"), ("next_steps", "Recommended next steps")]:
            items = notes.get(key) or []
            if not items:
                continue
            ws.cell(row=row, column=1, value=label).font = SECTION_FONT
            row += 1
            for it in items:
                c = ws.cell(row=row, column=1, value=f"• {it}")
                c.font = BODY_FONT
                c.alignment = Alignment(wrap_text=True, vertical="top")
                row += 1
            row += 1


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    spec_path = Path(sys.argv[1])
    spec = json.loads(spec_path.read_text())
    Book(spec, spec_path.parent).build(sys.argv[2])
    print(f"Built {sys.argv[2]}")


if __name__ == "__main__":
    main()
