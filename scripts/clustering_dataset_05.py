"""
Phase 5: Build participant-level dataset for clustering
- Loads final time-series dataset
- Creates presentation phases (early, mid, late)
- Computes participant-level behavioural + neural features
- Outputs ONE row per participant (for WEKA clustering)
"""

import pandas as pd

# 1. Load dataset
FILE_PATH = "processed_data/final/eeg_timeseries_final_version_04.csv"
df = pd.read_csv(FILE_PATH)

print("Dataset loaded.")
print("Shape:", df.shape)

# 2. Create divergence (flow vs strain)
df["divergence"] = df["engagement"] - df["cognitive_workload"]

print("\nDivergence created.")

# 3. Create presentation phases (based on time)
# You can tweak thresholds if needed
max_time = df["time_seconds"].max()

df["phase"] = pd.cut(
    df["time_seconds"],
    bins=[0, max_time/3, 2*max_time/3, max_time],
    labels=["early", "middle", "late"]
)

print("Presentation phases created.")

# 4. Compute participant-level features

# Early / Mid / Late engagement
phase_engagement = (
    df.groupby(["participant", "phase"])["engagement"]
    .mean()
    .unstack()
)

# Rename columns
phase_engagement.columns = [
    "early_engagement",
    "mid_engagement",
    "late_engagement"
]

# 5. Other participant-level metrics
participant_metrics = df.groupby("participant").agg({
    "engagement": "mean",
    "cognitive_workload": "mean",
    "divergence": "mean",
    "alpha": "mean",
    "beta": "mean",
    "theta": "mean"
}).rename(columns={
    "engagement": "mean_engagement",
    "cognitive_workload": "mean_workload",
    "divergence": "mean_divergence"
})

# 6. Engagement volatility (std dev)
volatility = df.groupby("participant")["engagement"].std()
volatility = volatility.rename("engagement_volatility")

# 7. Combine everything
df_final = pd.concat(
    [phase_engagement, participant_metrics, volatility],
    axis=1
).reset_index()

# 8. Add MBTI + EI back (for interpretation later)
meta = df.groupby("participant")[["MBTI", "IE", "SN", "TF", "JP", "EI"]].first().reset_index()

df_final = df_final.merge(meta, on="participant", how="left")

# 9. Round values
numeric_cols = df_final.select_dtypes(include="number").columns
df_final[numeric_cols] = df_final[numeric_cols].round(4)

# 10. Save dataset
OUTPUT_PATH = "processed_data/final/eeg_clustering_dataset_05.csv"
df_final.to_csv(OUTPUT_PATH, index=False)

print("\nClustering dataset saved to:")
print(OUTPUT_PATH)

# 11. Final checks
print("\nFinal shape (should be ~number of participants):", df_final.shape)
print("Unique participants:", df_final["participant"].nunique())

print("\nColumns:")
print(df_final.columns.tolist())

print("\n--- PHASE 5 COMPLETE ---\n")