# Data Quality Inspector

A lightweight Python utility for checking CSV datasets before they enter a downstream workflow.

## What it checks

- Missing values
- Duplicate rows
- Empty strings
- Basic email-format issues
- Numeric conversion problems
- Column-level quality summary

## Why I built it

Data annotation and evaluation workflows depend on clean, predictable input. This project demonstrates how I approach repetitive quality checks with simple automation.

## Run

```bash
pip install -r requirements.txt
python quality_report.py sample_data.csv
```

## Example output

```text
DATA QUALITY REPORT
-------------------
Rows:              12
Columns:            5
Duplicate rows:     1
Missing cells:      3
Empty strings:      2
Potential bad email:1

Overall status: REVIEW REQUIRED
```

## Stack

Python · Pandas
