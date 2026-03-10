"""
Phase 1: Dataset audit
Load the OSC dataset and inspect its structure, participants, sensors, and EEG band columns.
"""

import pandas as pd

# 1. Load dataset
FILE_PATH = "dataset/practice/test_dataset.xlsx"
df = pd.read_excel(FILE_PATH)

print("\n--- DATASET LOADED SUCCESSFULLY ---\n")

# 2. Basic structure
print("Dataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nColumn data types:")
print(df.dtypes)

# 3. Participant information
print("\nNumber of unique participants:")
print(df["participant"].nunique())

print("\nParticipant IDs:")
print(df["participant"].unique())

# 4. Sensor type check
print("\nUnique sensor types in dataset:")
print(df["osc_address_sensor"].unique())

print("\nNumber of EEG rows:")
print((df["osc_address_sensor"] == "eeg").sum())

# 5. Missingness check (EEG core columns)
eeg_columns = [
    "delta",
    "theta",
    "alpha",
    "beta"
]

print("\nNumber of rows where ALL core EEG values are NaN:")
empty_eeg_rows = df[eeg_columns].isna().all(axis=1).sum()
print(empty_eeg_rows)

# 6. Check Gamma and Unused columns
print("\nIs Gamma column entirely NaN?")
print(df["osc_data_gamma"].isna().all())

print("\nIs Unused column entirely NaN?")
print(df["osc_data_unused"].isna().all())

# 7. Timestamp check
print("\nTimestamp summary:")
print("Minimum timestamp:", df["timestamp"].min())
print("Maximum timestamp:", df["timestamp"].max())

print("\nmuse_timestamp preview:")
print(df["muse_timestamp"].head())

print("\n--- PHASE 1 AUDIT COMPLETE ---\n")
