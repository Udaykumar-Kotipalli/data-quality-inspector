import sys
from pathlib import Path
import pandas as pd

def quality_report(path: str) -> None:
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"File not found: {file}")

    df = pd.read_csv(file)

    missing = int(df.isna().sum().sum())
    empty = int((df.astype(str).apply(lambda col: col.str.strip() == "")).sum().sum())
    duplicates = int(df.duplicated().sum())

    email_issues = 0
    if "email" in df.columns:
        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        email_values = df["email"].dropna().astype(str).str.strip()
        email_issues = int((~email_values.str.match(email_pattern)).sum())

    print("\nDATA QUALITY REPORT")
    print("-" * 19)
    print(f"Rows:              {len(df)}")
    print(f"Columns:           {len(df.columns)}")
    print(f"Duplicate rows:    {duplicates}")
    print(f"Missing cells:     {missing}")
    print(f"Empty strings:     {empty}")
    print(f"Potential bad email:{email_issues}")

    status = "PASS" if (missing + empty + duplicates + email_issues) == 0 else "REVIEW REQUIRED"
    print(f"\nOverall status: {status}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quality_report.py <csv-file>")
        raise SystemExit(1)
    quality_report(sys.argv[1])
