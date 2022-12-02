import pandas as pd

# Open file with pandas
df = pd.read_csv("les-sites-dinjection-de-biomethane-en-france.csv", sep=";")


# Keep only the columns we need
df = df[["code_reg", "capacite_de_production_gwh_an", "augmentation_prevue"]]


# Sort by code_reg
df = df.sort_values(by="code_reg")


# Save the file
df.to_csv("cleaneddata/les-sites-dinjection-de-biomethane-en-france.csv", index=False)