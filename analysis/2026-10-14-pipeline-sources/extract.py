import openpyxl, csv, sys
wb = openpyxl.load_workbook(sys.argv[1])
ws = wb["Raw data"]
with open("raw.csv", "w", newline="") as f:
    w = csv.writer(f)
    for r in ws.iter_rows(values_only=True):
        w.writerow(["" if v is None else v for v in r])
# also report raw cell types for numeric-looking columns
types = {}
for r in ws.iter_rows(min_row=2, values_only=True):
    for i, v in enumerate(r):
        types.setdefault(i, {}).setdefault(type(v).__name__, 0)
        types[i][type(v).__name__] += 1
print(types)
