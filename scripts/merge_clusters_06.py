import pandas as pd

# 1. Load main dataset
MAIN_PATH = "processed_data/final/eeg_clustering_dataset_05.csv"
df_main = pd.read_csv(MAIN_PATH)

print("Main dataset loaded:", df_main.shape)

# 2. Load cluster output
CLUSTER_PATH = "processed_data/final/csv_result-clusters_output_001.csv"
df_clusters = pd.read_csv(CLUSTER_PATH)

print("Cluster dataset loaded:", df_clusters.shape)

# 3. Extract cluster column
# (WEKA sometimes names it differently — adjust if needed)
print("\nCluster columns:", df_clusters.columns.tolist())

# Usually it's called 'cluster'
cluster_col = df_clusters.columns[-1]  # safest fallback

# 4. Add cluster column to main dataset
df_main["cluster"] = df_clusters[cluster_col]

print("\nCluster column added.")

# 5. Save final dataset
OUTPUT_PATH = "processed_data/final/eeg_clustering_with_labels_06.csv"
df_main.to_csv(OUTPUT_PATH, index=False)

print("\nFinal dataset saved to:")
print(OUTPUT_PATH)

# 6. Quick check
print("\nCluster counts:")
print(df_main["cluster"].value_counts())

print("\n--- MERGE COMPLETE ---\n")
