"""Visualizer module containing all 9 EDA and diagnostic charts
answering core portfolio questions and uncovering underwriting trends.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")


def generate_exploratory_visualizations(df_clean: pd.DataFrame):
  """Generates all 9 EDA and diagnostic charts for the project report."""

  # ---------------------------------------------------------------------------
  # VISUAL 1: Loan Status Outcome Distribution (Q1)
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(7, 4))
  ax = sns.countplot(
      x="loan_status",
      data=df_clean,
      palette=["#2ecc71", "#e74c3c"],
      order=["Fully Paid", "Charged Off"],
  )
  plt.title(
      "Visual 1: Portfolio Outcome Breakdown (Fully Paid vs. Defaulted)",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Loan Status")
  plt.ylabel("Total Count")

  total_obs = len(df_clean)
  for p in ax.patches:
    h = p.get_height()
    pct = (h / total_obs) * 100
    ax.annotate(
        f"{h:,.0f} ({pct:.1f}%)",
        (p.get_x() + p.get_width() / 2, h / 2),
        ha="center",
        va="center",
        color="white",
        fontweight="bold",
    )
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 2: Default Rate Escalation Across Credit Grades (Q2 / Q4)
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(9, 4))
  grade_default = df_clean.groupby("grade")["Is_Churned"].mean().reset_index()
  grade_default["Default_Rate_Pct"] = grade_default["Is_Churned"] * 100
  sns.barplot(
      x="grade",
      y="Default_Rate_Pct",
      data=grade_default,
      palette="Reds_r",
      order=["A", "B", "C", "D", "E", "F", "G"],
  )
  plt.title(
      "Visual 2: Default Rate Escalation Curve Across Credit Grades (A–G)",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Credit Grade")
  plt.ylabel("Default Rate (%)")
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 3: Net Profit Yield Efficiency by Credit Grade (Q6)
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(9, 4))
  sns.barplot(
      x="grade",
      y="Net_Profit_Yield_Pct",
      data=df_clean,
      palette="RdYlGn_r",
      errorbar=None,
      order=["A", "B", "C", "D", "E", "F", "G"],
  )
  plt.axhline(0, color="black", linestyle="--", linewidth=1)
  plt.title(
      "Visual 3: Net Profit Yield % by Credit Grade (The Underwriting Sweet"
      " Spot)",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Credit Grade")
  plt.ylabel("Average Net Yield (%)")
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 4: Vintage Cohort Churn Trends Over Time (Q5)
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(10, 4))
  vintage_trend = (
      df_clean.groupby("Origination_Year")["Is_Churned"].mean().reset_index()
  )
  vintage_trend["Churn_Pct"] = vintage_trend["Is_Churned"] * 100
  sns.lineplot(
      x="Origination_Year",
      y="Churn_Pct",
      data=vintage_trend,
      marker="o",
      color="#e74c3c",
      linewidth=2.5,
  )
  plt.title(
      "Visual 4: Macroeconomic Trend - Default Rate by Origination Vintage"
      " (2007–2018)",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Origination Year")
  plt.ylabel("Default Rate (%)")
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 5: Interest Rate Spread Comparison (Fully Paid vs Charged Off)
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(8, 4))
  sns.boxplot(
      x="loan_status",
      y="int_rate",
      data=df_clean,
      palette=["#2ecc71", "#e74c3c"],
      order=["Fully Paid", "Charged Off"],
  )
  plt.title(
      "Visual 5: Interest Rate Distribution Comparison by Outcome",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Loan Status")
  plt.ylabel("Interest Rate (%)")
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 6: Debt-to-Income (DTI) Distribution Across Risk Tiers
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(9, 4))
  sns.boxplot(
      x="Credit_Tier",
      y="dti",
      data=df_clean,
      palette="Blues",
      order=["Exceptional", "Good", "Fair", "Poor"],
  )
  plt.title(
      "Visual 6: Borrower Debt-to-Income (DTI) Levels Across FICO Credit Tiers",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("FICO Credit Tier")
  plt.ylabel("Debt-to-Income (DTI)")
  plt.ylim(0, 40)
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 7: Loan Amount Distribution by Outcome
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(8, 4))
  sns.kdeplot(
      data=df_clean,
      x="loan_amnt",
      hue="loan_status",
      common_norm=False,
      palette=["#2ecc71", "#e74c3c"],
      fill=True,
      alpha=0.4,
  )
  plt.title(
      "Visual 7: Funded Loan Amount Density Curves by Loan Status",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Loan Amount ($)")
  plt.ylabel("Density")
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 8: Revolving Line Utilization vs. Default Risk
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(9, 4))
  sns.barplot(
      x="Credit_Tier",
      y="revol_util",
      data=df_clean,
      palette="Purples",
      errorbar=None,
      order=["Exceptional", "Good", "Fair", "Poor"],
  )
  plt.title(
      "Visual 8: Average Revolving Line Utilization (%) by FICO Credit Tier",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("FICO Credit Tier")
  plt.ylabel("Revolving Utilization (%)")
  plt.tight_layout()
  plt.show()

  # ---------------------------------------------------------------------------
  # VISUAL 9: Net Customer Lifetime Value (CLV) Performance by Grade
  # ---------------------------------------------------------------------------
  plt.figure(figsize=(9, 4))
  sns.barplot(
      x="grade",
      y="Net_CLV",
      data=df_clean,
      palette="Blues_r",
      errorbar=None,
      order=["A", "B", "C", "D", "E", "F", "G"],
  )
  plt.axhline(0, color="black", linestyle="--", linewidth=1)
  plt.title(
      "Visual 9: Average Net Customer Lifetime Value ($) Across Credit Grades",
      fontsize=11,
      fontweight="bold",
  )
  plt.xlabel("Credit Grade")
  plt.ylabel("Average Net CLV ($)")
  plt.tight_layout()
  plt.show()
