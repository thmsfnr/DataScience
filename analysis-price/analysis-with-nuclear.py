
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Open file with pandas
withNuclear = pd.read_csv("dataset-price.csv")

# Rename solar and wind
withNuclear["filiere"] = withNuclear["filiere"].replace("Photovoltaïque", "Solaire")
withNuclear["filiere"] = withNuclear["filiere"].replace("Éolien", "Eolien")

# Group withNuclear by filiere
withNuclear = withNuclear.groupby("filiere").mean()

# Do a clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(withNuclear[["prix_MWh"]])

# Add the cluster to the dataset
withNuclear["cluster"] = kmeans.labels_

# Add index to withNuclear
withNuclear = withNuclear.reset_index()

# Group Filiere by cluster and create a new column with each filiere name
withNuclear["filiere_group"] = withNuclear.groupby("cluster")["filiere"].transform(lambda x: ', '.join(x))

# Save the dataset
withNuclear.to_csv("dataset-price-with-nuclear.csv", index=False)

# Display in a graph the dependency between the price and the filiere
withNuclear = withNuclear.sort_values(by=["prix_MWh"])
plt.scatter(withNuclear["filiere"], withNuclear["prix_MWh"], c=withNuclear["cluster"], cmap="rainbow")
plt.title("Similitude between electricity production fields regarding their price")
plt.ylabel("price/MWh (in €)")
plt.xlabel("fields of electricity production")
plt.show()
