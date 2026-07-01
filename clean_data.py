"""
Task 1 - Data Cleaning & Preparation
Dataset : Mall_Customers.csv (Mall Customer Segmentation Data)

What this script does
----------------------
1. Loads the raw CSV
2. Reports missing values
3. Handles missing values (numeric -> median, text -> mode)
4. Removes duplicate rows
5. Standardizes text columns (trim spaces, consistent Title Case)
6. Converts / validates data types (ints stay ints, etc.)
7. Detects & converts any date columns to dd-mm-yyyy (kept generic,
   this dataset has no date column, but the logic is included so the
   script works on other raw datasets too)
8. Renames column headers to clean, lowercase, snake_case format
9. Saves the cleaned dataset + prints/writes a summary of every change

Run:
    python clean_data.py
"""

import pandas as pd
import numpy as np
import re
import os

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
INPUT_FILE = "Mall_Customers.csv"
OUTPUT_FILE = "Mall_Customers_cleaned.csv"
SUMMARY_FILE = "cleaning_summary.txt"

summary_lines = []


def log(msg):
    """Print to console AND store for the summary report."""
    print(msg)
    summary_lines.append(msg)


# ------------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------------
df = pd.read_csv(INPUT_FILE)
original_shape = df.shape
log(f"Loaded '{INPUT_FILE}' -> {original_shape[0]} rows, {original_shape[1]} columns")
log(f"Original columns: {list(df.columns)}")

# ------------------------------------------------------------------
# 2. CLEAN COLUMN HEADERS (lowercase, snake_case, no spaces/symbols)
# ------------------------------------------------------------------
def clean_col_name(col):
    col = col.strip().lower()
    col = re.sub(r"[^\w\s]", "", col)      # drop punctuation like ( ) $ %
    col = re.sub(r"\s+", "_", col)         # spaces -> underscores
    return col

old_columns = list(df.columns)
df.columns = [clean_col_name(c) for c in df.columns]
rename_map = dict(zip(old_columns, df.columns))
log(f"\nRenamed columns: {rename_map}")

# ------------------------------------------------------------------
# 3. MISSING VALUES
# ------------------------------------------------------------------
missing_before = df.isnull().sum()
log(f"\nMissing values BEFORE cleaning:\n{missing_before[missing_before > 0].to_string() if missing_before.sum() else 'None found'}")

for col in df.columns:
    if df[col].isnull().sum() > 0:
        if pd.api.types.is_numeric_dtype(df[col]):
            fill_value = df[col].median()
            df[col] = df[col].fillna(fill_value)
            log(f"  - Filled missing values in numeric column '{col}' with median ({fill_value})")
        else:
            fill_value = df[col].mode()[0] if not df[col].mode().empty else "Unknown"
            df[col] = df[col].fillna(fill_value)
            log(f"  - Filled missing values in text column '{col}' with mode ('{fill_value}')")

missing_after = df.isnull().sum().sum()
log(f"Missing values AFTER cleaning: {missing_after}")

# ------------------------------------------------------------------
# 4. REMOVE DUPLICATE ROWS
# ------------------------------------------------------------------
dupes_found = df.duplicated().sum()
df = df.drop_duplicates().reset_index(drop=True)
log(f"\nDuplicate rows found & removed: {dupes_found}")

# ------------------------------------------------------------------
# 5. STANDARDIZE TEXT COLUMNS (trim whitespace, Title Case)
# ------------------------------------------------------------------
text_cols = df.select_dtypes(include=["object", "string"]).columns.tolist()
for col in text_cols:
    df[col] = df[col].astype(str).str.strip()          # remove leading/trailing spaces
    df[col] = df[col].str.title()                       # e.g. "male"/"MALE" -> "Male"
    df[col] = df[col].replace({"Nan": np.nan})           # restore true NaNs if any slipped in
log(f"\nStandardized text formatting (trimmed spaces, Title Case) in columns: {text_cols}")

# Specific standardization example: Gender column
if "gender" in df.columns:
    df["gender"] = df["gender"].replace({
        "M": "Male", "F": "Female",
        "Man": "Male", "Woman": "Female"
    })
    log(f"Standardized 'gender' values -> {sorted(df['gender'].unique())}")

# ------------------------------------------------------------------
# 6. DETECT & CONVERT DATE COLUMNS TO dd-mm-yyyy (generic, future-proof)
# ------------------------------------------------------------------
date_like_cols = [c for c in df.columns if "date" in c.lower()]
for col in date_like_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce", dayfirst=True)
    df[col] = df[col].dt.strftime("%d-%m-%Y")
    log(f"Converted date column '{col}' to dd-mm-yyyy format")

if not date_like_cols:
    log("\nNo date columns present in this dataset (Mall_Customers.csv has none).")

# ------------------------------------------------------------------
# 7. FIX / VALIDATE DATA TYPES
# ------------------------------------------------------------------
dtype_fixes = {}
for col in ["customerid", "age", "annual_income_k", "spending_score_1100"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
        dtype_fixes[col] = "Int64"

log(f"\nEnforced data types: {dtype_fixes if dtype_fixes else 'No numeric columns needed conversion'}")
log(f"\nFinal dtypes:\n{df.dtypes.to_string()}")

# ------------------------------------------------------------------
# 8. SAVE CLEANED DATA
# ------------------------------------------------------------------
df.to_csv(OUTPUT_FILE, index=False)

final_shape = df.shape
log(f"\nFinal shape: {final_shape[0]} rows, {final_shape[1]} columns "
    f"(removed {original_shape[0] - final_shape[0]} rows total)")
log(f"Cleaned dataset saved to '{OUTPUT_FILE}'")

# ------------------------------------------------------------------
# 9. WRITE SUMMARY FILE
# ------------------------------------------------------------------
with open(SUMMARY_FILE, "w") as f:
    f.write("\n".join(summary_lines))

print(f"\nSummary written to '{SUMMARY_FILE}'")
