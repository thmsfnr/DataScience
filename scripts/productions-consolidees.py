
import pandas as pd

# Open file with pandas
df = pd.read_csv("rawdata/productions-consolidees-par-pays-du-groupe-edf.csv", sep=";")

# Keep only the columns we need
df = df[["annee", "filiere", "production","perimetre_spatial"]]

# Rename columns
df = df.rename(columns={"production": "production_MWh"})

# Keep only the rows we need
df = df[df["filiere"] != "Chaleur"]
df = df[df["perimetre_spatial"].str.contains("France", na=False)]

# Keep only the columns we need
df = df[["annee", "filiere", "production_MWh"]]

# Save the file
df.to_csv("cleaneddata/productions-consolidees-par-filiere-en-france.csv", index=False)
