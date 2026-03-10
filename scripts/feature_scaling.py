"""
Phase 5: Feature scaling
Standardize neural features so they are comparable before clustering analysis.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

print("\n--- PHASE 5: FEATURE SCALING STARTED ---\n")

# 1. Load the dataset created in Phase 4
FILE_PATH = "data/processed/eeg_personality_practice.csv"

df = pd.read_csv(FILE_PATH)

print("Dataset loaded.")
print("Dataset shape:", df.shape)

# 2. Select neural feature columns
# These are the features used for clustering.
# Personality variables (MBTI, EI) are excluded.
feature_columns = [
    "mean_delta",
    "mean_theta",
    "mean_alpha",
    "mean_beta",
    "std_alpha",
    "std_beta",
    "beta_alpha_ratio",
    "theta_beta_ratio",
    "alpha_beta_ratio",
    "max_beta",
    "range_beta"
]

print("\nNeural features selected for scaling:")
print(feature_columns)

print("\nNumber of neural features:", len(feature_columns))

# Verify columns exist
missing_columns = [col for col in feature_columns if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing expected columns: {missing_columns}")

features = df[feature_columns]

# 3. Apply standardization
# StandardScaler transforms each feature so that:
# mean = 0
# standard deviation = 1
# This ensures all features contribute equally
# to distance calculations in K-means clustering.
scaler = StandardScaler()

scaled_features = scaler.fit_transform(features)

scaled_df = pd.DataFrame(
    scaled_features,
    columns=feature_columns
)

# 4. Combine scaled features with participant info
scaled_df["participant"] = df["participant"]
scaled_df["MBTI"] = df["MBTI"]
scaled_df["EI"] = df["EI"]

# Reorder columns for readability
scaled_df = scaled_df[
    ["participant"] + feature_columns + ["MBTI", "EI"]
]

# Round values for readability
scaled_df = scaled_df.round(3)

print("\nScaling complete.")
print("Preview of scaled dataset:")

print(scaled_df.head())

# 5. Save the scaled dataset
OUTPUT_PATH = "data/processed/eeg_scaled_features_practice.csv"

scaled_df.to_csv(OUTPUT_PATH, index=False)

print("\nScaled dataset saved to:")
print(OUTPUT_PATH)

print("\n--- PHASE 5 COMPLETE ---\n")
