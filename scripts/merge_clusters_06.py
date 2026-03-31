import pandas as pd

# 1. Load main dataset
main_path = "processed_data/final/eeg_clustering_dataset_05.csv"
df_main = pd.read_csv(main_path)

print("Main dataset loaded:", df_main.shape)

# 2. Load cluster output
cluster_path = "processed_data/final/csv_result-clusters_output_001.csv"
df_clusters = pd.read_csv(cluster_path)

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
output_path = "processed_data/final/eeg_clustering_with_labels_06.csv"
df_main.to_csv(output_path, index=False)

print("\nFinal dataset saved to:")
print(output_path)

# 6. Quick check
print("\nCluster counts:")
print(df_main["cluster"].value_counts())

print("\n--- MERGE COMPLETE ---\n")