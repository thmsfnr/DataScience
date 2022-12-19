
# We will merge origine-de-lelectricite-fournie-par-edf-sa.csv and productions-consolidees-par-filiere-en-france.csv to dtermine shares of each filiere in the total production of EDF

import pandas as pd

# Open file with pandas
df = pd.read_csv("../cleaneddata/origine-de-lelectricite-fournie-par-edf-sa.csv", sep=",")
df2 = pd.read_csv("../cleaneddata/productions-consolidees-par-filiere-en-france.csv", sep=",")

# Where annee is 2021 and categorie is Source d'énergie d'électricité fournie for df
df = df[df["annee"] == 2021]
df = df[df["categorie"] == "Source d'énergie d'électricité fournie"]

# Where anne = 2021 for df2
df2 = df2[df2["annee"] == 2021]

# Keep only the columns we need
df = df[["sous_categorie","valeur","unite"]]
df2 = df2[["filiere","production_MWh"]]

# Rename columns
df = df.rename(columns={"sous_categorie": "filiere"})

# Add the missing filiere in df
df_new_row = pd.DataFrame({'filiere': ['Eolien', 'Solaire'], 'valeur': [0, 0], 'unite': ['%', '%']})
df = pd.concat([df, df_new_row], ignore_index=True)

# Sum of production_MWh
sum_production_MWh = df2["production_MWh"].sum()

# Quantity of production_MWh for eolien
eolien_production_MWh = df2[df2["filiere"] == "Eolienne"]["production_MWh"].sum()

# Share of eolien in sum
eolien_share = eolien_production_MWh / sum_production_MWh

# Quantity of production_MWh for solaire
solaire_production_MWh = df2[df2["filiere"] == "Solaire"]["production_MWh"].sum()

# Share of solaire in sum
solaire_share = solaire_production_MWh / sum_production_MWh

# Update line Eolien in df
df.loc[df['filiere'] == 'Eolien', 'valeur'] = eolien_share * 100

# Update line Solaire in df
df.loc[df['filiere'] == 'Solaire', 'valeur'] = solaire_share * 100

# Autres Renouvelables valeur - Eolien + Solaire in df
df.loc[df['filiere'] == 'Autres Renouvelables', 'valeur'] = df.loc[df['filiere'] == 'Autres Renouvelables', 'valeur'] - eolien_share * 100 - solaire_share * 100

# Keep only the columns we need
df = df[["filiere","valeur"]]

# Rename columns
df = df.rename(columns={"valeur": "part_de_production"})

# Save the file
df.to_csv("shares-of-filiere.csv", index=False)
