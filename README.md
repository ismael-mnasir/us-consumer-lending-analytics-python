Markdown
# US Consumer Lending Analytics & Credit Risk Pipeline

An end-to-end Python analytics framework examining 2.26M+ LendingClub loan records (2007–2018) to evaluate borrower retention, credit risk, debt recovery, macroeconomic vintage shifts, and underwriting net profit yield efficiency.

---

## Project Structure
This repository is engineered using a modular software design pattern to ensure clean separation of concerns, enterprise maintainability, and scalability:

```text
us_consumer_lending_analytics/
├── .gitignore              # Hides raw multi-gigabyte data files and bytecode
├── README.md               # Project documentation
├── main.py                 # Terminal orchestrator script
├── loader.py               # Data ingestion & schema validation module
├── cleaner.py              # Data cleaning & feature engineering module
├── metrics.py              # Quantitative analytics engine (Q1–Q6 logic)
├── visualizer.py           # Automated diagnostic chart suite
└── lending_analysis.ipynb  # Master Jupyter presentation notebook

Core Business Questions Addressed
Borrower Retention (Q1): Evaluated portfolio completion rates (80.04% fully paid vs. 19.96% default churn).

Credit Risk Tiers (Q2): Mapped default concentration across FICO score buckets.

True Profitability / Net CLV (Q3): Calculated net dollar returns per borrower after default losses.

Capital Recovery / LGD (Q4): Analyzed collection recovery rates (recovering only 5% to 8% of original principal).

Macroeconomic Vintage Trends (Q5): Tracked 11 years of origination cohorts (2007–2018) to capture cyclical risk shifts.

Underwriting Sweet Spot (Q6): Identified grade-level net profit yield efficiency, revealing capital destruction in subprime tiers (Grades E–G).

Key Findings & Strategic Insights
The Sweet Spot: Grade B loans yield optimal risk-adjusted returns (5.39% net profit yield, ~$697 net profit per loan).

The Underwriting Boundary: High interest rates in subprime tiers (Grades E–G) fail to cover default write-offs, driving net profit yields down to -8.82%.

Strategic Recommendation: Establish hard underwriting caps on subprime tiers and reallocate capital toward prime and near-prime volume.
