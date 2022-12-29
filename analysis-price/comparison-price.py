
# We will compare dataset-price-without-nuclear.csv and dataset-price-with-nuclear.csv

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Open file with pandas
withoutNuclear = pd.read_csv("dataset-price-without-nuclear.csv")
withNuclear = pd.read_csv("dataset-price-with-nuclear.csv")

# Analyse the dataset
print(withoutNuclear)
print(withNuclear)

# Compare the two datasets
withoutNuclear = withoutNuclear.sort_values(by=["prix_MWh"])
withNuclear = withNuclear.sort_values(by=["prix_MWh"])
plt.scatter(withoutNuclear["filiere"], withoutNuclear["prix_MWh"], marker='^',c=withoutNuclear["cluster"], cmap="rainbow")
plt.scatter(withNuclear["filiere"], withNuclear["prix_MWh"], c=withNuclear["cluster"], cmap="rainbow")
plt.title("Price difference between electricity production fields with and without nuclear")
plt.ylabel("price/MWh (in €)")
plt.xlabel("fields of electricity production")
plt.legend(["Without nuclear", "With nuclear"])
plt.show()

# Compare the cluster of the two datasets
clusterNotNuclear = withoutNuclear.groupby("cluster").mean()
clusterNuclear = withNuclear.groupby("cluster").mean()

# Reorder the cluster
clusterNotNuclear = clusterNotNuclear.sort_values(by=["prix_MWh"])
clusterNuclear = clusterNuclear.sort_values(by=["prix_MWh"])

# Reorder the index
clusterNotNuclear = clusterNotNuclear.reset_index()
clusterNuclear = clusterNuclear.reset_index()

# Represent on a graph the mean price of electricity between clusters
clusterNotNuclear = clusterNotNuclear.sort_values(by=["prix_MWh"])
clusterNuclear = clusterNuclear.sort_values(by=["prix_MWh"])
plt.scatter(clusterNotNuclear.index, clusterNotNuclear["prix_MWh"], cmap="red")
plt.scatter(clusterNuclear.index, clusterNuclear["prix_MWh"], cmap="blue")
plt.title("Price difference between electricity production clusters with and without nuclear")
plt.ylabel("price/MWh (in €)")
plt.xlabel("fields of electricity production")
plt.legend(["Without nuclear", "With nuclear"])
plt.show()

# Compare the mean price of electricity between clusters
print(clusterNotNuclear)
print(clusterNuclear)

# Compare the mean price of electricity between clusters
print(clusterNotNuclear["prix_MWh"].mean())
print(clusterNuclear["prix_MWh"].mean())
