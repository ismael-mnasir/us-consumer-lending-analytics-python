"""Main execution pipeline runner.
Coordinates data loading, EDA profiling, cleaning, metrics, and visuals.
"""

from cleaner import clean_and_engineer_features
from eda import perform_exploratory_data_analysis
from loader import load_lending_data
from metrics import calculate_business_metrics
from visualizer import generate_exploratory_visualizations


def main():
  print("Starting US Consumer Lending Analytics Pipeline...\n")

  # Step 1: Ingest Raw Data
  df_raw = load_lending_data()

  # Step 2: Perform Initial Exploratory Data Analysis (EDA) Profiling
  perform_exploratory_data_analysis(df_raw)

  # Step 3: Clean Data & Engineer Financial Features
  df_clean = clean_and_engineer_features(df_raw)

  # Step 4: Compute Business Answers for Questions Q1 through Q6
  calculate_business_metrics(df_clean)

  # Step 5: Generate All 9 EDA & Diagnostic Visualizations
  generate_exploratory_visualizations(df_clean)

  print("Pipeline execution completed successfully!")


if __name__ == "__main__":
  main()
