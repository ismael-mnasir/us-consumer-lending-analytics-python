"""Exploratory Data Analysis (EDA) module.
Handles initial data profiling, descriptive statistics, and distribution checks.
"""

import pandas as pd


def perform_exploratory_data_analysis(df_raw: pd.DataFrame):
  """Prints key statistical summaries and data profiling metrics."""
  print("=" * 75)
  print("            EXPLORATORY DATA ANALYSIS (EDA) SUMMARY            ")
  print("=" * 75)

  # 1. Dataset Shape and Memory Usage
  print(f"• Total Rows: {df_raw.shape[0]:,}")
  print(f"• Total Columns: {df_raw.shape[1]}")

  # 2. Missing Values Overview
  missing_counts = df_raw.isnull().sum()
  missing_pct = (missing_counts / len(df_raw)) * 100
  missing_df = pd.DataFrame(
      {"Missing Values": missing_counts, "Percentage (%)": missing_pct}
  )
  print("\nTop Missing Value Columns:")
  print(missing_df[missing_df["Missing Values"] > 0].head(5).round(2))

  # 3. Numerical Summary Statistics
  print("\nDescriptive Statistics for Key Numerical Features:")
  key_num_cols = ["loan_amnt", "funded_amnt", "int_rate", "annual_inc", "dti"]
  print(df_raw[key_num_cols].describe().round(2))

  print("=" * 75 + "\n")
