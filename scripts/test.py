import pandas as pd

df = pd.read_csv("processed_data/final/eeg_clustering_with_labels_06.csv")

# 1. Count clusters
print("\nCluster sizes:")
print(df["cluster"].value_counts())

# 2. MBTI distribution per cluster
print("\nMBTI per cluster:")
print(pd.crosstab(df["cluster"], df["MBTI"]))

# 3. EI distribution per cluster
print("\nEI per cluster:")
print(pd.crosstab(df["cluster"], df["EI"]))

# 4. View extreme clusters
print("\nCluster 1 members:")
print(df[df["cluster"] == 1][["participant", "MBTI", "EI"]])

print("\nCluster 2 members:")
print(df[df["cluster"] == 2][["participant", "MBTI", "EI"]])