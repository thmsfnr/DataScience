
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


# Open file with pandas
df = pd.read_csv("conclusion-without-nuclear.csv")

#Rename the column CO2 emissions [tCO2] to CO2 emissions (in Tonne)
df = df.rename(columns={"CO2 emissions [tCO2]": "CO2 emissions (in Tonne)"})

# Analyse the dataset
print(df)

# Analyse the dataset
print(df.describe())

# Keep only the filiere and the CO2 emissions (in Tonne)
df = df[["filiere", "CO2 emissions (in Tonne)"]]

# Analyse the dataset
print(df.groupby("filiere").describe())

# Analyse the dataset
scatter_matrix(df.groupby("filiere").mean())
plt.title("Representation of mean CO2 for each electricity production field ")
plt.ylabel("population")
plt.xlabel("CO2 emissions (in Tonne)")
plt.show()


# Analyse the dataset
print(df)

# Do a clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df[["CO2 emissions (in Tonne)"]])

# Add the cluster to the dataset
df["cluster"] = kmeans.labels_

# Group Filiere by cluster and create a new column with each filiere name
df["filiere_group"] = df.groupby("cluster")["filiere"].transform(lambda x: ', '.join(x))

# group by filiere_group
print(df.groupby("filiere_group").mean())

# Display in a graph the dependency between the CO2 and the filiere
df = df.sort_values(by=["CO2 emissions (in Tonne)"])
plt.scatter(df["filiere"], df["CO2 emissions (in Tonne)"], c=df["cluster"], cmap="rainbow")
plt.title("Representation of CO2 for each electricity production field ")
plt.ylabel("CO2 emissions (in Tonne)")
plt.xlabel("filiere")
plt.show()


# Save the dataset
df.to_csv("dataset-CO2-v2.csv", index=False)

#Loris, prends les photos, et écrire sur le rapport.