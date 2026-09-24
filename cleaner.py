"""Data cleaning, missing value imputation, and feature engineering module.
Prepares clean dimensional data and calculates financial metrics.
"""

import numpy as np
import pandas as pd
from config import COMPLETED_STATUSES


def clean_and_engineer_features(df_raw: pd.DataFrame) -> pd.DataFrame:
  """Filters completed loans, handles missing values, and creates risk features."""

  # 1. Filter out ongoing or current loans (keep only completed outcomes)
  df_clean = df_raw[df_raw["loan_status"].isin(COMPLETED_STATUSES)].copy()

  # 2. Impute missing numerical values with medians to prevent skewness
  df_clean["annual_inc"] = df_clean["annual_inc"].fillna(
      df_clean["annual_inc"].median()
  )
  df_clean["dti"] = df_clean["dti"].fillna(df_clean["dti"].median())
  df_clean["revol_util"] = df_clean["revol_util"].fillna(
      df_clean["revol_util"].median()
  )

  # 3. Fill missing recovery dollars and collection fees with zero
  df_clean["total_rec_late_fee"] = df_clean["total_rec_late_fee"].fillna(0)
  df_clean["recoveries"] = df_clean["recoveries"].fillna(0)
  df_clean["collection_recovery_fee"] = df_clean[
      "collection_recovery_fee"
  ].fillna(0)

  print(
      f"Retained Completed Loans: {len(df_clean):,} of {len(df_raw):,} raw"
      " records"
  )

  # 4. Feature Engineering: Credit Tiers, Churn Flag, Net CLV, and Recovery Rates
  df_clean["fico_avg"] = (
      df_clean["fico_range_low"] + df_clean["fico_range_high"]
  ) / 2
  df_clean["Credit_Tier"] = pd.cut(
      df_clean["fico_avg"],
      bins=[0, 580, 670, 740, 850],
      labels=["Poor", "Fair", "Good", "Exceptional"],
  )

  df_clean["issue_d"] = pd.to_datetime(df_clean["issue_d"], format="%b-%Y")
  df_clean["Origination_Year"] = df_clean["issue_d"].dt.year

  # Binary Churn/Default Flag (1 = Charged Off/Default, 0 = Fully Paid)
  df_clean["Is_Churned"] = (
      df_clean["loan_status"].isin(["Charged Off", "Default"]).astype(int)
  )

  # Net Customer Lifetime Value (CLV)
  df_clean["Net_CLV"] = (
      df_clean["total_pymnt"]
      + df_clean["total_rec_late_fee"]
      - df_clean["funded_amnt"]
  ).round(2)

  # Net Recovery Amount and Recovery Rate Percentage
  df_clean["Net_Recovery"] = (
      df_clean["recoveries"] - df_clean["collection_recovery_fee"]
  ).clip(lower=0)
  df_clean["Recovery_Rate_Pct"] = np.where(
      df_clean["Is_Churned"] == 1,
      (
          df_clean["Net_Recovery"]
          / df_clean["funded_amnt"].replace(0, np.nan)
      )
      * 100,
      0,
  ).round(2)
  df_clean["Recovery_Rate_Pct"] = df_clean["Recovery_Rate_Pct"].fillna(0)

  # Net Profit Yield Percentage
  df_clean["Net_Profit_Yield_Pct"] = (
      (df_clean["Net_CLV"] / df_clean["funded_amnt"].replace(0, np.nan)) * 100
  ).round(2)

  print(f"Missing Values After Cleaning: {df_clean.isnull().sum().sum()}\n")
  return df_clean
