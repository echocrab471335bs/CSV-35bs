"""CSV profiler: prints basic statistics for a CSV file."""

import csv, sys

def profile(path):
    with open(path, newline='') as f:
        rdr = csv.DictReader(f)
        cols = rdr.fieldnames or []
        stats = {c: {'missing':0, 'unique':set(), 'sample':None} for c in cols}
        rows = 0
        for r in rdr:
            rows += 1
            for c in cols:
                v = r[c]
                if v == '':
                    stats[c]['missing'] += 1
                else:
                    stats[c]['unique'].add(v)
                    if stats[c]['sample'] is None:
                        stats[c]['sample'] = v
    print(f"Columns: {len(cols)}")
    print(f"Rows: {rows}")
    for c in cols:
        s = stats[c]
        print(f"\nColumn: {c}")
        print(f"  Missing: {s['missing']}")
        print(f"  Unique values: {len(s['unique'])}")
        print(f"  Sample: {s['sample']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_profile.py <csv_file>")
        sys.exit(1)
    profile(sys.argv[1])