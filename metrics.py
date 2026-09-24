"""Core business question aggregations.
Answers business questions Q1 through Q6 using portfolio data.
"""

import pandas as pd


def calculate_business_metrics(df_clean: pd.DataFrame):
  """Computes quantitative summaries for all 6 business questions."""

  print("=" * 75)
  print("        US CONSUMER LENDING: CORE BUSINESS ANSWERS (Q1–Q6)         ")
  print("=" * 75)

  # Q1: Portfolio Retention vs. Churn Breakdown
  retention_rate = (1 - df_clean["Is_Churned"].mean()) * 100
  churn_rate = df_clean["Is_Churned"].mean() * 100
  print(f"\n[Q1] PORTFOLIO RETENTION VS. CHURN BREAKDOWN")
  print(f"• Fully Paid (Retained Borrowers): {retention_rate:.2f}%")
  print(f"• Charged Off / Default (Churned Borrowers): {churn_rate:.2f}%")

  # Q2 & Q3: Credit Risk & Net Profitability by FICO Credit Tier
  fico_clv_summary = (
      df_clean.groupby("Credit_Tier", observed=False)
      .agg(
          Total_Loans=("id", "count"),
          Avg_FICO=("fico_avg", "mean"),
          Default_Rate_Pct=("Is_Churned", lambda x: x.mean() * 100),
          Avg_Funded_Amount=("funded_amnt", "mean"),
          Avg_Net_CLV=("Net_CLV", "mean"),
          Total_Net_Profit=("Net_CLV", "sum"),
      )
      .reset_index()
  )
  print(f"\n[Q2 & Q3] CREDIT RISK & NET CLV BY FICO TIER")
  print(fico_clv_summary.round(2))

  # Q4: Debt Recovery Rate (LGD) by Credit Grade
  defaulted_df = df_clean[df_clean["Is_Churned"] == 1]
  recovery_summary = (
      defaulted_df.groupby("grade")
      .agg(
          Total_Defaults=("id", "count"),
          Avg_Funded_At_Default=("funded_amnt", "mean"),
          Avg_Net_Recovered=("Net_Recovery", "mean"),
          Avg_Recovery_Rate_Pct=("Recovery_Rate_Pct", "mean"),
      )
      .reset_index()
  )
  print(f"\n[Q4] DEBT RECOVERY PERFORMANCE (LGD) BY CREDIT GRADE")
  print(recovery_summary.round(2))

  # Q5: Macroeconomic Vintage Cohort Trends (2007–2018)
  vintage_summary = (
      df_clean.groupby("Origination_Year")
      .agg(
          Total_Loans=("id", "count"),
          Total_Funded_Volume=("funded_amnt", "sum"),
          Default_Rate_Pct=("Is_Churned", lambda x: x.mean() * 100),
          Avg_Net_CLV=("Net_CLV", "mean"),
          Avg_Interest_Rate=("int_rate", "mean"),
      )
      .reset_index()
  )
  print(f"\n[Q5] VINTAGE COHORT TIME-SERIES PERFORMANCE (2007–2018)")
  print(vintage_summary.round(2))

  # Q6: Underwriting Net Profit Yield Efficiency by Credit Grade
  yield_summary = (
      df_clean.groupby("grade")
      .agg(
          Total_Loans=("id", "count"),
          Avg_Interest_Rate=("int_rate", "mean"),
          Default_Rate_Pct=("Is_Churned", lambda x: x.mean() * 100),
          Avg_Net_CLV=("Net_CLV", "mean"),
          Avg_Net_Profit_Yield_Pct=("Net_Profit_Yield_Pct", "mean"),
      )
      .reset_index()
  )
  print(f"\n[Q6] NET PROFIT YIELD EFFICIENCY BY CREDIT GRADE")
  print(yield_summary.round(2))
  print("=" * 75 + "\n")
