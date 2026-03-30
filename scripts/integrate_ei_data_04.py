"""
Phase 4: Integrate EI categories into dataset
- Loads final EEG + MBTI dataset
- Loads EI dataset (categorical)
- Cleans EI values
- Maps EI category to participants
- Performs data quality checks
"""

import pandas as pd

# 1. Load main dataset
EEG_PATH = "processed_data/final/eeg_timeseries_final_03.csv"
df = pd.read_csv(EEG_PATH)

print("EEG dataset loaded.")
print("Shape:", df.shape)

# 2. Load EI dataset
EI_PATH = "dataset/EQ_Surveys.csv"
ei_df = pd.read_csv(EI_PATH)

print("\nEI dataset loaded.")
print("Shape:", ei_df.shape)

# 3. Clean EI dataset
ei_df = ei_df.rename(columns={
    "STUDENT_ID": "participant",
    "EQ_TYPE": "EI"
})

# 4. Clean EI values
ei_df["EI"] = ei_df["EI"].replace("No Survey results", pd.NA)
ei_df["EI"] = ei_df["EI"].str.strip()

# ⚠️ Handle multiple EI values (e.g. "social skill,empathy")
ei_df["EI"] = ei_df["EI"].str.split(",").str[0]

# 5. Keep only needed columns
ei_df = ei_df[["participant", "EI"]]

print("\nCleaned EI data.")

# 6. Merge EI into main dataset (FIXED)
df = pd.merge(
    df,
    ei_df,
    on="participant",
    how="left",
    suffixes=("", "_new")
)

# 🔥 Fix duplicate EI columns
if "EI_new" in df.columns:
    df["EI"] = df["EI_new"]
    df = df.drop(columns=["EI_new"])

print("\nEI merged into dataset.")
print("Shape:", df.shape)

# 7. Round numeric values
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].round(4)

# 8. Save final dataset
OUTPUT_PATH = "processed_data/final/eeg_timeseries_final_version_04.csv"
df.to_csv(OUTPUT_PATH, index=False)

print("\nFinal dataset saved to:")
print(OUTPUT_PATH)

# 9. SANITY CHECKS (IMPORTANT)
# Row-level missing values
print("\nMissing EI values (rows):", df["EI"].isna().sum())
print("Missing MBTI values (rows):", df["MBTI"].isna().sum())

# Unique participants
total_participants = df["participant"].nunique()
print("\nTotal participants:", total_participants)

# Participant-level summary
participant_summary = (
    df.groupby("participant")
    .agg({
        "MBTI": "first",
        "EI": "first"
    })
    .reset_index()
)

# Missing both
missing_both = participant_summary[
    participant_summary["MBTI"].isna() &
    participant_summary["EI"].isna()
]

print("\nParticipants with NO MBTI AND NO EI:", len(missing_both))
print("List:", missing_both["participant"].tolist())

# Missing only MBTI
missing_mbti_only = participant_summary[
    participant_summary["MBTI"].isna() &
    participant_summary["EI"].notna()
]

# Missing only EI
missing_ei_only = participant_summary[
    participant_summary["MBTI"].notna() &
    participant_summary["EI"].isna()
]

print("\nParticipants missing ONLY MBTI:", len(missing_mbti_only))
print("Participants missing ONLY EI:", len(missing_ei_only))

# Unique EI categories
print("\nUnique EI categories:", df["EI"].dropna().unique())

print("\n--- PHASE 4 COMPLETE ---\n")

# for claude
# # 6. WORK DONE – RESULTS
# You need to include a work done chapter which can vary according to the selected project:
# 6.1 Design, interface, code… (project A)
# 6.2 Interface design, screen flows…(project B)
# 6.3 Diagrams, dashboards…. (project C)
# 6.4 Comparative analysis of solutions found in literature searches (project D)

# 7. FINDINGS
# You need to include a findings chapter which can vary according to the selected project:
# 7.1 Testing & user evaluation (project A)
# 7.2 Testing & user evaluation (project B)
# 7.3 Overview of patterns observed (project C)
# 7.4 Functionality comparison tables and visualisations of prominent features and/or visualisation of literature review analysis(project D)

