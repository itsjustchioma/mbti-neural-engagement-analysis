"""
Phase 3: Feature engineering.
Aggregate EEG signals into participant-level neural features and remove invalid rows.
"""

import pandas as pd

print("\n--- PHASE 3: FEATURE ENGINEERING STARTED ---\n")

# 1. Load the cleaned EEG dataset produced in Phase 2
FILE_PATH = "data/processed/eeg_clean_practice.csv"
df = pd.read_csv(FILE_PATH)

print("Dataset loaded.")
print("Shape before cleaning:", df.shape)

# 2. Basic data quality report
# Before cleaning, we inspect the dataset for common issues
# such as duplicate rows, missing values, signal dropouts,
# and extreme values.
print("\n--- DATA QUALITY REPORT ---")

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

missing_values = df[["delta", "theta", "alpha", "beta"]].isna().sum()
print("\nMissing values per EEG band:")
print(missing_values)

zero_rows = (
    (df["delta"] == 0) &
    (df["theta"] == 0) &
    (df["alpha"] == 0) &
    (df["beta"] == 0)
)

print("\nRows where all EEG bands are zero:", zero_rows.sum())

print("\nBasic beta statistics:")
print(df["beta"].describe())

# 3. Remove duplicate rows
df = df.drop_duplicates()

print("\nDuplicates removed.")
print("Shape after duplicate removal:", df.shape)

# 4. Remove rows with missing EEG values
df = df.dropna(subset=["delta", "theta", "alpha", "beta"])

print("\nRows with missing EEG values removed.")
print("Shape after NaN removal:", df.shape)

# 5. Remove invalid signal rows
# Rows where all EEG bands equal zero represent signal
# dropout from the Muse headset rather than real neural
# activity, so they are excluded from analysis.
zero_rows = (df[["delta", "theta", "alpha", "beta"]] == 0).all(axis=1)

removed = zero_rows.sum()

df = df[~zero_rows]

print("\nRows removed due to signal dropout:", removed)
print("Shape after cleaning:", df.shape)

# 6. Verify beta value distribution
# This helps confirm that the beta range values later
# are not caused by abnormal sensor spikes.
print("\n--- BETA VALUE CHECK ---")

print("Minimum beta value:", df["beta"].min())
print("Maximum beta value:", df["beta"].max())

print("\nFive smallest beta values:")
print(df["beta"].nsmallest(5))

# 7. Aggregate EEG data to participant-level features
# Each participant has thousands of EEG samples recorded
# over time. For clustering analysis we summarise each
# participant's neural activity using statistical features.
features = df.groupby("participant").agg(

    # Average bandpower levels
    mean_delta=("delta", "mean"),
    mean_theta=("theta", "mean"),
    mean_alpha=("alpha", "mean"),
    mean_beta=("beta", "mean"),

    # Variability of engagement / relaxation
    std_alpha=("alpha", "std"),
    std_beta=("beta", "std"),

    # Peak engagement values
    max_beta=("beta", "max"),
    min_beta=("beta", "min")

).reset_index()

# 8. Derived engagement metrics
# Ratios help interpret behavioural states such as
# engagement intensity and internal cognitive processing.
features["beta_alpha_ratio"] = features["mean_beta"] / features["mean_alpha"]
features["theta_beta_ratio"] = features["mean_theta"] / features["mean_beta"]
features["alpha_beta_ratio"] = features["mean_alpha"] / features["mean_beta"]

# Beta fluctuation range
features["range_beta"] = features["max_beta"] - features["min_beta"]

# min_beta was only required to compute the range
features = features.drop(columns=["min_beta"])

print("\nParticipant feature dataset created.")
print("Number of participants:", features.shape[0])
print("Feature columns:", features.columns.tolist())

# 9. Round values for readability
# Calculations above use full floating-point precision.
# We round to 3 decimal places only for readability in
# the exported dataset.
features = features.round(3)

# 10. Save the aggregated dataset
OUTPUT_PATH = "data/processed/eeg_features_practice.csv"
features.to_csv(OUTPUT_PATH, index=False)

print("\nFeature dataset saved to:")
print(OUTPUT_PATH)

print("\n--- PHASE 3 COMPLETE ---\n")
