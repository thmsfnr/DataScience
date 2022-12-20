import pandas as pd

# Open file with pandas
df = pd.read_csv("scenarios-de-consommation-de-gaz-de-production-de-gaz-vert-et-de-mobilite-gaz-a-.csv", sep=";")


# Sort by annee
df = df.sort_values(by="annee")

# Save the file
df.to_csv("cleaneddata/les-sites-dinjection-de-biomethane-en-france2.csv", index=False)
