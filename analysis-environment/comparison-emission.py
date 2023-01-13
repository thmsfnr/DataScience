
# We will compare dataset-CO2-v2.csv and conclusion-without-nuclear.csv

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Open file with pandas
withoutNuclear = pd.read_csv("conclusion-without-nuclear.csv")
withNuclear = pd.read_csv("dataset-CO2-v2.csv")
partProdWithNuclear = pd.read_csv("dataset-part_production.csv")

# Merge the two datasets
withNuclear = pd.merge(withNuclear, partProdWithNuclear, on="filiere")

# Rename the column "CO2 emissions [tCO2]" to "CO2 emissions (in Tonne)"
withoutNuclear = withoutNuclear.rename(columns={"CO2 emissions [tCO2]": "CO2 emissions (in Tonne)"})

# Keep filiere and part_de_production and CO2 emissions (in Tonne)
withoutNuclear = withoutNuclear[["filiere", "part_production", "CO2 emissions (in Tonne)"]]
withNuclear = withNuclear[["filiere", "part_production", "CO2 emissions (in Tonne)"]]

# Sort the dataset by filiere
withoutNuclear = withoutNuclear.sort_values(by=["filiere"])
withNuclear = withNuclear.sort_values(by=["filiere"])

# Analyse the dataset and the sum of CO2 emissions (in Tonne)
print(withoutNuclear)
sumWithoutNuclear = withoutNuclear["CO2 emissions (in Tonne)"].sum()
print(withoutNuclear["CO2 emissions (in Tonne)"].sum(), "Tonne de CO2 produite par an")
print(withNuclear)
sumWithNuclear = withNuclear["CO2 emissions (in Tonne)"].sum()
print(withNuclear["CO2 emissions (in Tonne)"].sum() , "Tonne de CO2 produite par an")

# Compare the two datasets
plt.scatter(withoutNuclear["filiere"], withoutNuclear["part_production"], cmap="blue")
plt.scatter(withNuclear["filiere"], withNuclear["part_production"], cmap="red")
plt.title("Part of production difference between electricity production fields with and without nuclear")
plt.ylabel("part of production")
plt.xlabel("fields of electricity production")
plt.legend(["Without nuclear", "With nuclear"])
plt.show()

# Difference between the sum of CO2 emissions (in Tonne) with and without nuclear
difference = sumWithNuclear - sumWithoutNuclear
print("Différence entre la production de CO2 (Avec - Sans) : ", difference, "Tonne de CO2")

# Compare the two datasets
plt.scatter(withoutNuclear["filiere"], withoutNuclear["CO2 emissions (in Tonne)"], cmap="blue")
plt.scatter(withNuclear["filiere"], withNuclear["CO2 emissions (in Tonne)"], cmap="red")
plt.title("CO2 emissions difference between electricity production fields with and without nuclear")
plt.ylabel("CO2 emissions (in Tonne)")
plt.xlabel("fields of electricity production")
plt.legend(["Without nuclear", "With nuclear"])
plt.show()
