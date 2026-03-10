"""
Phase 4: Personality data integration
Merge EEG features with MBTI and emotional intelligence data for each participant.
"""

import pandas as pd

print("\n--- PHASE 4: MERGING PERSONALITY DATA ---\n")

# 1 Load EEG feature dataset from Phase 3
EEG_PATH = "data/processed/eeg_features_practice.csv"
eeg_df = pd.read_csv(EEG_PATH)

print("EEG feature dataset loaded.")
print("Shape:", eeg_df.shape)

# 2 Create MBTI + EI dataset (from Ariadne's email)
personality_data = {
    "participant": ["A14","B14","C13","D13"],
    "MBTI": ["ESFP","INFJ","ESFP","ESFJ"],
    "EI": [None,"self-awareness","empathy",None]
}

psych_df = pd.DataFrame(personality_data)

print("\nPersonality dataset created.")
print(psych_df)

# 3 Merge EEG + personality data
merged_df = pd.merge(
    eeg_df,
    psych_df,
    on="participant",
    how="left"
)

print("\nDatasets merged.")
print("Final dataset shape:", merged_df.shape)

# 4 Save merged dataset
OUTPUT_PATH = "data/processed/eeg_personality_practice.csv"
merged_df.to_csv(OUTPUT_PATH, index=False)

print("\nMerged dataset saved to:")
print(OUTPUT_PATH)

print("\n--- PHASE 4 COMPLETE ---\n")
