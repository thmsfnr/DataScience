
# We will compare dataset-price-without-nuclear.csv and dataset-price-v2.csv

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Open file with pandas
df = pd.read_csv("dataset-price-without-nuclear.csv")
df2 = pd.read_csv("dataset-price.csv")

# Rename solar and wind
df2["filiere"] = df2["filiere"].replace("Photovoltaïque", "Solaire")
df2["filiere"] = df2["filiere"].replace("Éolien", "Eolien")

# Group df2 by filiere
df2 = df2.groupby("filiere").mean()

# Do a clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df2[["prix_MWh"]])

# Add the cluster to the dataset
df2["cluster"] = kmeans.labels_

# Add index to df2
df2 = df2.reset_index()

# Group Filiere by cluster and create a new column with each filiere name
df2["filiere_group"] = df2.groupby("cluster")["filiere"].transform(lambda x: ', '.join(x))

# Analyse the dataset
print(df)
print(df2)

# Compare the two datasets
df = df.sort_values(by=["prix_MWh"])
df2 = df2.sort_values(by=["prix_MWh"])
plt.scatter(df["filiere"], df["prix_MWh"], c=df["cluster"], cmap="rainbow")
plt.scatter(df2["filiere"], df2["prix_MWh"], c=df2["cluster"], cmap="rainbow")
plt.title("Similitude between electricity production fields regarding their price")
plt.ylabel("price/MWh (in €)")
plt.xlabel("fields of electricity production")
plt.show()

# Compare the cluster of the two datasets
dfc = df.groupby("cluster").mean()
dfc2 = df2.groupby("cluster").mean()

# Reorder the cluster
dfc = dfc.sort_values(by=["prix_MWh"])
dfc2 = dfc2.sort_values(by=["prix_MWh"])

# Reorder the index
dfc = dfc.reset_index()
dfc2 = dfc2.reset_index()

# Represent on a graph the mean price of electricity between clusters
dfc = dfc.sort_values(by=["prix_MWh"])
dfc2 = dfc2.sort_values(by=["prix_MWh"])
plt.scatter(dfc.index, dfc["prix_MWh"], cmap="red")
plt.scatter(dfc2.index, dfc2["prix_MWh"], cmap="blue")
plt.title("Similitude between electricity production fields regarding their price")
plt.ylabel("price/MWh (in €)")
plt.xlabel("fields of electricity production")
plt.show()

# Compare the mean price of electricity between clusters
print(dfc)
print(dfc2)

# Compare the mean price of electricity between clusters
print(dfc["prix_MWh"].mean())
print(dfc2["prix_MWh"].mean())
