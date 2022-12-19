#Build a csv dataset with :
#Nucléaire - 59.8€/MWh à 109€/MWh
#Éolien - 90€/MWh à 200€/MWh
#Hydraulique - 15€/MWh à 20€/MWh
#Photovoltaïque - 142€/MWh
#Gaz - 70€/MWh à 100€/MWh
#Charbon - 40€/MWh
#Fioul - 70€/MWh à 100€/MWh

import pandas as pd

# BUold the dataset
df = pd.DataFrame(columns=["range","filiere", "prix_MWh"])

# Add the rows
df = df.append({"range": "low", "filiere": "Nucléaire", "prix_MWh": 59.8}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Nucléaire", "prix_MWh": 109}, ignore_index=True)
df = df.append({"range": "low", "filiere": "Éolien", "prix_MWh": 90}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Éolien", "prix_MWh": 200}, ignore_index=True)
df = df.append({"range": "low", "filiere": "Hydraulique", "prix_MWh": 15}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Hydraulique", "prix_MWh": 20}, ignore_index=True)
df = df.append({"range": "low", "filiere": "Photovoltaïque", "prix_MWh": 142}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Photovoltaïque", "prix_MWh": 142}, ignore_index=True)
df = df.append({"range": "low", "filiere": "Gaz", "prix_MWh": 70}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Gaz", "prix_MWh": 100}, ignore_index=True)
df = df.append({"range": "low", "filiere": "Charbon", "prix_MWh": 40}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Charbon", "prix_MWh": 40}, ignore_index=True)
df = df.append({"range": "low", "filiere": "Fioul", "prix_MWh": 70}, ignore_index=True)
df = df.append({"range": "high", "filiere": "Fioul", "prix_MWh": 100}, ignore_index=True)

# Save the file
df.to_csv("dataset-price.csv", index=False)
