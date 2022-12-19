
# Analysis of dataset-price.csv to determine the dependency between the price and the filiere

import pandas as pd

# Open file with pandas
df = pd.read_csv("dataset-price.csv")

# Analyse the dataset
print(df)

# Analyse the dataset
print(df.describe())

# Analyse the dataset
print(df.groupby("filiere").describe())

# Build group of filieres very similar
df["filiere_group"] = df["filiere"].replace(["Nucléaire", "Gaz", "Fioul"], "Cout moyen - Nucléaire, Gaz, Fioul")
df["filiere_group"] = df["filiere_group"].replace(["Éolien", "Photovoltaïque"], "Cout élevé - Eolien, Photovoltaïque")
df["filiere_group"] = df["filiere_group"].replace(["Hydraulique", "Charbon"], "Cout faible - Hydraulique, Charbon")

# Analyse the dataset
print(df.groupby(["filiere_group"]).describe())

