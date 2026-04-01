"""
Phase 2: Build time-series dataset with MBTI (EI placeholder)
- Loads cleaned EEG dataset
- Merges MBTI data using STUDENT_ID
- Creates behavioural metrics
- Splits MBTI into dimensions
- Adds empty EI column (to be filled later)
"""

import pandas as pd

# 1. Load EEG dataset
EEG_PATH = "processed_data/final/eeg_combined_clean_01.csv"
df = pd.read_csv(EEG_PATH)

print("EEG dataset loaded.")
print("Shape:", df.shape)

# 2. Load MBTI dataset
MBTI_PATH = "dataset/MBTI_EI_raw.csv"
mbti_df = pd.read_csv(MBTI_PATH)

print("\nMBTI dataset loaded.")
print("Shape:", mbti_df.shape)

# 3. Clean MBTI dataset
mbti_df = mbti_df.rename(columns={
    "STUDENT_ID": "participant",
    "MBTI_TYPE": "MBTI"
})

# Keep ONLY participant + MBTI (remove VARK)
mbti_df = mbti_df[["participant", "MBTI"]]

# 4. Merge datasets
df = pd.merge(
    df,
    mbti_df,
    on="participant",
    how="left"
)

print("\nDatasets merged.")
print("Shape:", df.shape)

# 5. Create engagement metric
df["engagement"] = df["beta"] / df["alpha"]

# 6. Create cognitive workload metric
df["cognitive_workload"] = df["theta"] / df["alpha"]

print("\nBehavioural metrics created.")

# 7. Split MBTI into dimensions
df["IE"] = df["MBTI"].str[0]
df["SN"] = df["MBTI"].str[1]
df["TF"] = df["MBTI"].str[2]
df["JP"] = df["MBTI"].str[3]

print("MBTI dimensions created.")

# 8. Add EI column (empty for now)
df["EI"] = None

# When the data comes in:
# df["EI"] = df["participant"].map(ei_mapping)

print("EI column added (empty placeholder).")

# 9. Sort data
df = df.sort_values(by=["participant", "time_seconds"])

# Round numeric columns to 4 decimal places
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[numeric_cols] = df[numeric_cols].round(4)

# 10. Save dataset
OUTPUT_PATH = "processed_data/final/eeg_timeseries_full_02.csv"
df.to_csv(OUTPUT_PATH, index=False)

print("\nFinal dataset saved to:")
print(OUTPUT_PATH)

# 11. Sanity checks
print("\nMissing MBTI values:", df["MBTI"].isna().sum())
print("Unique participants:", df["participant"].nunique())

print("\n--- PHASE 2 COMPLETE ---\n")
