"""
Phase 1: Combine and clean raw EEG datasets

- Loads all raw participant CSV files
- Uses 'user' column as participant ID
- Filters only EEG sensor data
- Removes invalid rows (NaN + zero signal)
- Outputs one clean combined EEG dataset
"""

import os
import pandas as pd

# 1. Path to dataset folder
DATASET_PATH = "dataset"

# 2. Get all CSV files (exclude MBTI file)
files = [
    f for f in os.listdir(DATASET_PATH)
    if f.endswith(".csv") and "MBTI" not in f
]

print(f"Found {len(files)} participant files.")

# 3. Load and combine all files
all_data = []

for file in files:
    file_path = os.path.join(DATASET_PATH, file)

    df = pd.read_csv(file_path)

    # ✅ Keep only EEG sensor data early (important)
    df = df[df["sensor"] == "eeg"]

    # ✅ Use correct participant ID from dataset
    df["participant"] = df["user"]

    all_data.append(df)

# Combine all into one dataframe
df = pd.concat(all_data, ignore_index=True)

print("All files combined.")
print("Shape:", df.shape)

# 4. Keep only relevant columns
df = df[
    [
        "participant",
        "elapsed_sec",
        "delta",
        "theta",
        "alpha",
        "beta"
    ]
]

# 5. Rename elapsed_sec → time_seconds
df = df.rename(columns={"elapsed_sec": "time_seconds"})

# 6. Remove missing EEG values
df = df.dropna(subset=["delta", "theta", "alpha", "beta"])

print("\nRemoved NaN values.")
print("Shape:", df.shape)

# 7. Remove rows where ALL signals are zero
zero_rows = (
    (df["delta"] == 0) &
    (df["theta"] == 0) &
    (df["alpha"] == 0) &
    (df["beta"] == 0)
)

removed = zero_rows.sum()
df = df[~zero_rows]

print(f"\nRemoved {removed} zero-signal rows.")
print("Final shape:", df.shape)

# 8. Sort data (VERY IMPORTANT for time series later)
df = df.sort_values(by=["participant", "time_seconds"])

# 9. Save clean dataset
OUTPUT_PATH = "processed_data/final/eeg_combined_clean_01.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nClean dataset saved to:")
print(OUTPUT_PATH)

# 10. Sanity checks
print("\nNumber of participants:", df["participant"].nunique())
print("Time range:", df["time_seconds"].min(), "to", df["time_seconds"].max())

print("\n--- PHASE 1 COMPLETE ---\n")
