"""Data ingestion module.
Handles loading the raw dataset efficiently using selected columns.
"""

import pandas as pd
from config import FILE_PATH, SELECTED_COLUMNS


def load_lending_data(file_path: str = FILE_PATH) -> pd.DataFrame:
  """Loads the raw LendingClub dataset into memory using only essential columns."""
  print(f"Loading raw dataset from {file_path}...")
  df_raw = pd.read_csv(file_path, usecols=SELECTED_COLUMNS, low_memory=False)
  print(
      f"Loaded successfully! Rows: {df_raw.shape[0]:,} | Columns:"
      f" {df_raw.shape[1]}\n"
  )
  return df_raw
