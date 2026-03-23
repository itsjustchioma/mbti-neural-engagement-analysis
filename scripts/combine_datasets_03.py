"""
Phase 3: Combine old and new EEG datasets
- Loads new full dataset (40+ participants)
- Loads old dataset (4 participants)
- Combines both datasets
- Removes duplicates
- Outputs final unified dataset
"""

import pandas as pd

# 1. Load new dataset
NEW_PATH = "processed_data/final/eeg_timeseries_full_02.csv"
new_df = pd.read_csv(NEW_PATH)

print("New dataset loaded.")
print("Shape:", new_df.shape)

# 2. Load old dataset
OLD_PATH = "processed_data/initial_4_man_data/eeg_timeseries_seconds.csv"
old_df = pd.read_csv(OLD_PATH)

print("\nOld dataset loaded.")
print("Shape:", old_df.shape)

# ⚠️ Ensure column consistency (important)
old_df = old_df[new_df.columns]

# 3. Combine datasets
combined_df = pd.concat([new_df, old_df], ignore_index=True)

print("\nDatasets combined.")
print("Shape:", combined_df.shape)

# 4. Remove duplicates
combined_df = combined_df.drop_duplicates()

print("\nDuplicates removed.")
print("Final shape:", combined_df.shape)

# 5. Sort data
combined_df = combined_df.sort_values(by=["participant", "time_seconds"])

# 6. Save final dataset
OUTPUT_PATH = "processed_data/final/eeg_timeseries_final_03.csv"
combined_df.to_csv(OUTPUT_PATH, index=False)

print("\nFinal dataset saved to:")
print(OUTPUT_PATH)

# 7. Sanity check
print("\nTotal participants:", combined_df["participant"].nunique())

print("\n--- PHASE 3 COMPLETE ---\n")
