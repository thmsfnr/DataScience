
# Analysis of dataset-price.csv to determine the dependency between the price and the filiere

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Open file with pandas
df = pd.read_csv("dataset-price.csv")

# Analyse the dataset
print(df)

# Analyse the dataset
print(df.describe())

# Analyse the dataset
print(df.groupby("filiere").describe())

# Analyse the dataset
scatter_matrix(df.groupby("filiere").mean())
plt.title("Representation of mean price for each electricity production field ")
plt.ylabel("population")
plt.xlabel("price/MWh (in €)")
plt.show()

# Analyse the dataset
scatter_matrix(df)
plt.title("Representation of extremum prices for each electricity production field ")
plt.ylabel("population")
plt.xlabel("price/MWh (in €)")
plt.show()

# add column range to the filiere
df["filiere"] = (df["filiere"]).str[0:4] + " " + df["range"]

# remove range column
df = df.drop("range", axis=1)

# Analyse the dataset
print(df)

# Do a clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df[["prix_MWh"]])

# Add the cluster to the dataset
df["cluster"] = kmeans.labels_

# Group Filiere by cluster and create a new column with each filiere name
df["filiere_group"] = df.groupby("cluster")["filiere"].transform(lambda x: ', '.join(x))

# group by filiere_group
print(df.groupby("filiere_group").mean())

# Display in a graph the dependency between the price and the filiere
df = df.sort_values(by=["prix_MWh"])
plt.scatter(df["filiere"], df["prix_MWh"], c=df["cluster"], cmap="rainbow")
plt.title("Similitude between electricity production fields regarding their price")
plt.ylabel("price/MWh (in €)")
plt.xlabel("fields of electricity production")
plt.show()

# save the dataset
df.to_csv("dataset-price-v2.csv", index=False)
