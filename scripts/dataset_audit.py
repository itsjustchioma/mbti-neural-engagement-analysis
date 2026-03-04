import pandas as pd

# 1. Load dataset
file_path = "dataset/practice/test_dataset.xlsx"
df = pd.read_excel(file_path)

print("\n--- DATASET LOADED SUCCESSFULLY ---\n")

# 2. Basic Structure
print("Dataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nColumn data types:")
print(df.dtypes)

# 3. Participant Information
print("\nNumber of unique participants:")
print(df["participant"].nunique())

print("\nParticipant IDs:")
print(df["participant"].unique())

# 4. Sensor Type Check
print("\nUnique sensor types in dataset:")
print(df["osc_address_sensor"].unique())

print("\nNumber of EEG rows:")
print((df["osc_address_sensor"] == "eeg").sum())

# 5. Missingness Check (EEG Core Columns)
eeg_columns = [
    "delta",
    "theta",
    "alpha",
    "beta"
]

print("\nNumber of rows where ALL core EEG values are NaN:")
empty_eeg_rows = df[eeg_columns].isna().all(axis=1).sum()
print(empty_eeg_rows)

# 6. Check Gamma and Unused Columns
print("\nIs Gamma column entirely NaN?")
print(df["osc_data_gamma"].isna().all())

print("\nIs Unused column entirely NaN?")
print(df["osc_data_unused"].isna().all())

# 7. Timestamp Check
print("\nTimestamp summary:")
print("Minimum timestamp:", df["timestamp"].min())
print("Maximum timestamp:", df["timestamp"].max())

print("\nmuse_timestamp preview:")
print(df["muse_timestamp"].head())


print("\n--- PHASE 1 AUDIT COMPLETE ---\n")