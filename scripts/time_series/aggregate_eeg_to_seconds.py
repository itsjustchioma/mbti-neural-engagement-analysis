"""
Phase 2: Aggregate EEG signals into 1-second time bins.

This script reduces the high-frequency EEG dataset into
one row per participant per second. This makes time-series
visualisations clearer and easier to interpret in Tableau.
"""

import pandas as pd

print("\n--- EEG TIME BINNING STARTED ---\n")

# 1 Load the time-series dataset
FILE_PATH = "processed_data/eeg_timeseries.csv"

df = pd.read_csv(FILE_PATH)

print("Dataset loaded.")
print("Original shape:", df.shape)

# 2 Create integer second bins
# Example:
# 0.001 → second 0
# 0.532 → second 0
# 1.203 → second 1
df["second"] = df["time_seconds"].astype(int)

print("\nSecond bins created.")

# 3 Aggregate EEG signals per participant per second
# We compute the average signal within each second.
df_seconds = (
    df.groupby(["participant", "second"])
    .agg({
        "alpha": "mean",
        "beta": "mean",
        "theta": "mean",
        "delta": "mean",
        "MBTI": "first",
        "EI": "first",
        "IE": "first",
        "SN": "first",
        "TF": "first",
        "JP": "first"
    })
    .reset_index()
)

print("\nSignals aggregated per second.")
print("New dataset shape:", df_seconds.shape)

# 4 Recalculate behavioural metrics using averaged bandpower
df_seconds["engagement"] = df_seconds["beta"] / df_seconds["alpha"]
df_seconds["cognitive_workload"] = df_seconds["theta"] / df_seconds["alpha"]

print("\nBehavioural metrics recalculated.")

# 5 Rename column for clarity
df_seconds.rename(columns={"second": "time_seconds"}, inplace=True)

# 6 Round values for readability
df_seconds = df_seconds.round(4)

# 7 Save the dataset
OUTPUT_PATH = "processed_data/eeg_timeseries_seconds.csv"

df_seconds.to_csv(OUTPUT_PATH, index=False)

print("\nAggregated dataset saved to:")
print(OUTPUT_PATH)

print("\n--- EEG TIME BINNING COMPLETE ---\n")
