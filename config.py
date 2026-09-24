"""Configuration settings, file paths, and column schemas.
Keeps all project constants and configuration in one centralized place.
"""

# Path to the raw LendingClub dataset
FILE_PATH = "accepted_2007_to_2018Q4.csv.gz"

# Essential origination columns required for credit risk & profitability analysis
SELECTED_COLUMNS = [
    "id",
    "loan_amnt",
    "funded_amnt",
    "term",
    "int_rate",
    "grade",
    "sub_grade",
    "annual_inc",
    "issue_d",
    "loan_status",
    "dti",
    "revol_util",
    "total_pymnt",
    "total_rec_late_fee",
    "recoveries",
    "collection_recovery_fee",
    "fico_range_low",
    "fico_range_high",
]

# Only include completed loan outcomes to prevent data leakage
COMPLETED_STATUSES = ["Fully Paid", "Charged Off", "Default"]
