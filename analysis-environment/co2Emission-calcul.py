# we will use dataset-part-production-without-nuclear.csv and CO2_emissions_by_source.csv to calculate the global electricty price (with scale factor for each filiere) by MWh

import pandas as pd

# Open file with pandas
df = pd.read_csv("dataset-part-production-without-nuclear.csv")
df2 = pd.read_csv("CO2_emissions_by_source.csv")
df3 = pd.read_csv("production-electrique-par-filiere.csv", sep=",")

# Remove Nucléaire of df2
df2 = df2[df2["filiere"] != "Nucléaire"]

# Group by filiere in df
df = df.groupby("filiere").mean()

# Merge the two datasets
df = pd.merge(df, df2, on="filiere")

#Sum the production of energy
totalProduction = df3["production_kWh"].sum()

print(totalProduction)

# Add a column with the production in kWh for each filiere
for index, row in df.iterrows():
    df.loc[df['filiere'] == row["filiere"], 'production_kWh'] = totalProduction * (row["part_production"]/100)

print(df)

#add a new column to the dataframe
df['CO2 emissions [gCO2]'] = df['CO2 emissions [gCO2/kWh]'] * df['production_kWh']

print(df)

#Convert the unit of the column CO2 emissions [gCO2] from gCO2 to tCO2
df['CO2 emissions [gCO2]'] = df['CO2 emissions [gCO2]'] / 1000000

#rename the column CO2 emissions [gCO2] to CO2 emissions [tCO2]
df = df.rename(columns={'CO2 emissions [gCO2]': 'CO2 emissions [tCO2]'})

print(df)

#Save the dataset
df.to_csv("conclusion-without-nuclear.csv", index=False)