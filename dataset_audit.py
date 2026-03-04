# import pandas as pd

# # --------------------------------------------------
# # PHASE 1: DATASET STRUCTURAL AUDIT
# # --------------------------------------------------

# # 1. Load dataset
# file_path = "dataset/test_dataset.xlsx"
# df = pd.read_excel(file_path)

# print("\n--- DATASET LOADED SUCCESSFULLY ---\n")

# # --------------------------------------------------
# # 2. Basic Structure
# # --------------------------------------------------

# print("Dataset shape (rows, columns):")
# print(df.shape)

# print("\nColumn names:")
# print(df.columns.tolist())

# print("\nColumn data types:")
# print(df.dtypes)


# # --------------------------------------------------
# # 3. Participant Information
# # --------------------------------------------------

# print("\nNumber of unique participants:")
# print(df["osc_address_person"].nunique())

# print("\nParticipant IDs:")
# print(df["osc_address_person"].unique())


# # --------------------------------------------------
# # 4. Sensor Type Check
# # --------------------------------------------------

# print("\nUnique sensor types in dataset:")
# print(df["osc_address_sensor"].unique())


# # --------------------------------------------------
# # 5. Missingness Check (EEG Core Columns)
# # --------------------------------------------------

# eeg_columns = [
#     "osc_data_Delta",
#     "osc_data_Theta",
#     "osc_data_Alpha",
#     "osc_data_Beta"
# ]

# print("\nNumber of rows where ALL core EEG values are NaN:")
# empty_eeg_rows = df[eeg_columns].isna().all(axis=1).sum()
# print(empty_eeg_rows)


# # --------------------------------------------------
# # 6. Check Gamma and Unused Columns
# # --------------------------------------------------

# print("\nIs Gamma column entirely NaN?")
# print(df["osc_data_Gama"].isna().all())

# print("\nIs Unused column entirely NaN?")
# print(df["osc_data_Unused"].isna().all())


# # --------------------------------------------------
# # 7. Timestamp Check
# # --------------------------------------------------

# print("\nTimestamp summary:")
# print("Minimum timestamp:", df["timestamp"].min())
# print("Maximum timestamp:", df["timestamp"].max())

# print("\nMuse_timestamp preview:")
# print(df["Muse_timestamp"].head())


# print("\n--- PHASE 1 AUDIT COMPLETE ---\n")