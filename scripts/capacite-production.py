
import pandas as pd

# Open file with pandas
df = pd.read_csv("rawdata/capacites-de-production-par-pays-du-groupe-edf.csv", sep=";")

# Keep only the columns we need
df = df[["annee", "filiere", "capacite_maximale_de_production",'perimetre_spatial']]

# Rename columns
df = df.rename(columns={"capacite_maximale_de_production": "capacite_maximale_de_production_MWe"})


# Keep only the rows we need
df = df[df["filiere"] != "Chaleur"]
df = df[df["perimetre_spatial"].str.contains("France", na=False)]

# Keep only the columns we need
df = df[["annee", "filiere", "capacite_maximale_de_production_MWe"]]


# Save the file
df.to_csv("cleaneddata/capacites-de-production-par-filiere-en-france.csv", index=False)
