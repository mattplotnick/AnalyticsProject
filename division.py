from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv("NFL.csv")
df = data[["team_name", "lat", "long"]]

# Teams that must be in the same group
team_groups = [["Baltimore Ravens", "Pittsburgh Steelers"], ["Chicago Bears", "Green Bay Packers"], ["San Francisco 49ers", "Seattle Seahawks"]]

# Create an empty list to store clusters
clusters = [[] for _ in range(8)]

# Assign teams to clusters based on pre-defined groups
for group in team_groups:
    group_indices = df[df["team_name"].isin(group)].index.tolist()
    for idx in group_indices:
        assigned = False
        for cluster_idx, cluster in enumerate(clusters):
            if len(cluster) < 4:
                clusters[cluster_idx].append(idx)
                assigned = True
                break
        if not assigned:
            break

# Assign remaining teams to clusters based on location
remaining_indices = df[~df["team_name"].isin([team for group in team_groups for team in group])].index.tolist()

# Use KMeans clustering on remaining teams based on their proximity to grouped teams
initial_centers = np.array([df.iloc[idx][["lat", "long"]].values for cluster in clusters for idx in cluster])
kmeans = KMeans(n_clusters=len(clusters), random_state=0, init=initial_centers).fit(df.iloc[remaining_indices][["lat", "long"]])

# Assign remaining teams to clusters
for i, label in enumerate(kmeans.labels_):
    clusters[label].append(remaining_indices[i])

# Add cluster labels to the dataframe
df["cluster"] = -1
for i, cluster in enumerate(clusters):
    df.loc[cluster, "cluster"] = i

# Display the clusters
plt.figure(figsize=(15, 10))
for i in range(len(clusters)):
    cluster_df = df[df["cluster"] == i]
    plt.scatter(cluster_df["long"], cluster_df["lat"], label=f"Cluster {i+1}")

# Annotate each point with team name
for i, row in df.iterrows():
    plt.annotate(row["team_name"], (row["long"], row["lat"]), fontsize=9)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("NFL Teams Locations")
plt.legend()
plt.show()
