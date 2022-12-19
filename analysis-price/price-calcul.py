
# we will use shares-of-filiere.csv and dataset-price.csv to calculate the global electricty price (with scale factor for each filiere) by MWh

import pandas as pd

# Open file with pandas
df = pd.read_csv("dataset-price.csv")
df2 = pd.read_csv("shares-of-filiere.csv")

# Remove Autres Renouvelables of df2
df2 = df2[df2["filiere"] != "Autres Renouvelables"]

# Group by filiere in df
df = df.groupby("filiere").mean()

# Rename Éolien to Eolien
df = df.rename(index={"Éolien": "Eolien"})

# Rename Photovoltaïque to Solaire
df = df.rename(index={"Photovoltaïque": "Solaire"})

# Merge the two datasets
df = pd.merge(df, df2, on="filiere")

# To simulate a new repartition of production, we will use this variable
newPartProduction = {"Charbon": 10.8, "Gaz": 7.0, "Nucléaire": 66.8, "Hydraulique": 8.6, "Eolien": 0.7, "Solaire": 0.078, "Fioul": 0.8}

# Calculate a factor for each filiere using newPartProduction variable
for index, row in df.iterrows():
    ratio = (row["part_de_production"] / (newPartProduction[row["filiere"]]))
    ratio = ratio - (ratio - 1) * 0.9
    df.loc[df['filiere'] == row["filiere"], 'factor'] = ratio

# Save the dataset
df.to_csv("conclusion.csv", index=False)

# Calculate the price
price = 0
for index, row in df.iterrows():
    price += row["prix_MWh"] * (row["part_de_production"]/100) * row["factor"]
    print(row["filiere"] + " : " + str(row["prix_MWh"] * row["factor"]) + " €/MWh")
print("The global electricity price is " + str(price) + " €/MWh")
