
import pandas as pd

# Open file with pandas
df = pd.read_csv("conclusion.csv")

# Remove nuclear
df = df[df["filiere"] != "Nucléaire"]

# Simulate whithout nuclear (part of ther increase proportionally the ols shares)
newPartProduction = {"Charbon": (0.81*100)/(100-76.88), "Gaz": (7.0*100)/(100-76.88), "Hydraulique": (8.56*100)/(100-76.88), "Eolien": (0.7647861595767812*100)/(100-76.88), "Solaire": (0.0787807345745655*100)/(100-76.88), "Fioul": (0.8*100)/(100-76.88)}

# Calculate a factor for each filiere using newPartProduction variable
for index, row in df.iterrows():
    ratio = (row["part_de_production"] / (newPartProduction[row["filiere"]]))
    ratio = ratio - (ratio - 1) * 0.9
    df.loc[df['filiere'] == row["filiere"], 'factor'] = ratio
    
# Add the new production part
for index, row in df.iterrows():
    df.loc[df['filiere'] == row["filiere"], 'part_de_production'] = newPartProduction[row["filiere"]]

# Replace the old price by the new price
for index, row in df.iterrows():
    price = row["prix_MWh"] * row["factor"]
    df.loc[df['filiere'] == row["filiere"], 'prix_MWh'] = price

# Save the dataset
df.to_csv("conclusion-without-nuclear.csv", index=False)
