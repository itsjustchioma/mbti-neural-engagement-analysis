import pandas as pd

print("\n--- PHASE 2: EEG PREPROCESSING STARTED ---\n")

# 1. Load practice dataset
file_path = "dataset/practice/test_dataset.xlsx"
df = pd.read_excel(file_path)

print("Dataset loaded.")
print("Original shape:", df.shape)


# 2. Filter EEG rows only
eeg_df = df[df["osc_address_sensor"] == "eeg"]

print("\nEEG rows isolated.")
print("EEG dataset shape:", eeg_df.shape)


# 3. Drop unnecessary columns
columns_to_drop = [
    "timestamp",
    "osc_address_sensor",
    "osc_type",
    "osc_data_gamma",
    "osc_data_unused"
]

eeg_df = eeg_df.drop(columns=columns_to_drop)

print("\nUnused columns removed.")
print("Remaining columns:", eeg_df.columns.tolist())


# 4. Save clean dataset
output_path = "data/processed/eeg_clean_practice.csv"
eeg_df.to_csv(output_path, index=False)

print("\nClean EEG dataset saved to:")
print(output_path)

print("\n--- PHASE 2 COMPLETE ---\n")
