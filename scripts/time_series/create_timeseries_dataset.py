"""
Phase 1: Create time-series behavioural dataset

This script prepares the EEG dataset for time-series analysis.
It creates time_seconds, engagement metrics, and merges MBTI data.
"""

import pandas as pd
import numpy as np

print("\n--- PHASE 1: TIME-SERIES DATASET CREATION STARTED ---\n")

FILE_PATH = "processed_data/eeg_clean.csv"

df = pd.read_csv(FILE_PATH)

print("Dataset loaded.")
print("Shape:", df.shape)

# Convert timestamp to datetime
df["muse_timestamp"] = pd.to_datetime(df["muse_timestamp"])

# Create time_seconds variable
df["time_seconds"] = (
    df.groupby("participant")["muse_timestamp"]
    .transform(lambda x: (x - x.min()).dt.total_seconds())
)

print("Time variable created.")

# Create engagement metric
df["engagement"] = df["beta"] / df["alpha"]

# Create cognitive workload metric
df["cognitive_workload"] = df["theta"] / df["alpha"]

print("Behavioural metrics created.")

# Replace infinite values caused by division by zero
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Create personality dataset
personality_data = {
    "participant": ["A14", "B14", "C13", "D13"],
    "MBTI": ["ESFP", "INFJ", "ESFP", "ESFJ"],
    "EI": [None, "self-awareness", "empathy", None]
}

personality_df = pd.DataFrame(personality_data)

# Merge EEG + personality data
df = pd.merge(
    df,
    personality_df,
    on="participant",
    how="left"
)

print("Personality data merged.")

df["IE"] = df["MBTI"].str[0]
df["SN"] = df["MBTI"].str[1]
df["TF"] = df["MBTI"].str[2]
df["JP"] = df["MBTI"].str[3]

print("MBTI dimensions created.")

df = df[
    [
        "participant",
        "muse_timestamp",
        "time_seconds",
        "delta",
        "theta",
        "alpha",
        "beta",
        "engagement",
        "cognitive_workload",
        "MBTI",
        "EI",
        "IE",
        "SN",
        "TF",
        "JP",
    ]
]

df = df.sort_values(
    by=["participant", "time_seconds"]
)
df["time_seconds"] = df["time_seconds"].round(5)
df = df.round(4)

# Save dataset
OUTPUT_PATH = "processed_data/eeg_timeseries.csv"
df.to_csv(OUTPUT_PATH, index=False)

print("\nTime-series dataset saved to:")
print(OUTPUT_PATH)

print("\n--- PHASE 1 COMPLETE ---\n")
