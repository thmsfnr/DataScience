import pandas as pd

# Open file with pandas
df = pd.read_csv("dataset-part_production.csv")

# Calculate the sum of production part
sum = 0
for index, row in df.iterrows():
    sum += row["part_production"]

# Remove nuclear
df = df[df["filiere"] != "Nucléaire"]

print(df)

nuclearPart = 82.14059933338557


# Simulate whithout nuclear (part of ther increase proportionally the ols shares)
newPartProduction = {"Charbon": (0.7215875460898845*sum)/(sum-nuclearPart), 
"Gaz": (5.655051224851311*sum)/(sum-nuclearPart), 
"Hydraulique": (10.043101729307685*sum)/(sum-nuclearPart), 
"Fioul": (1.2608412677114138*sum)/(sum-nuclearPart), 
"Biomasse": (0.17795067723511726*sum)/(sum-nuclearPart),
"Géothermie": (0.0008682214190120616*sum)/(sum-nuclearPart)}

print(newPartProduction)

# Replace old part production by new part production
for index, row in df.iterrows():
    df.loc[df['filiere'] == row["filiere"], 'part_production'] = newPartProduction[row["filiere"]]



print(df)

# Save the dataset
df.to_csv("dataset-part-production-without-nuclear.csv", index=False)
