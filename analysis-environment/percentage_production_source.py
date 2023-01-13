#read the document and create the dataset of origine-de-lelectricite-fournie-par-edf-sa.csv

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv("origine-de-lelectricite-fournie-par-edf-sa.csv", sep=",")


#keep only the columns annee is 2021
df = df[df['annee'] == 2021]

#sort by valeur
df = df.sort_values(by=['valeur'], ascending=False)

#rename the column sous_categorie to filiere
df = df.rename(columns={'sous_categorie': 'filiere'})

#keep only the columns annee, filiere, valeur, unite
df = df[['annee', 'filiere', 'valeur', 'unite']]


print(df)


print('\n')


df2 = pd.read_csv("productions-consolidees-par-filiere-en-france.csv", sep=",")

#keep only the columns annee is 2021
df2 = df2[df2['annee'] == 2021]

#Change the unit of the column production_MWh from MWh to kWh
df2['production_MWh'] = df2['production_MWh'] * 1000

#rename the column production_MWh to production_kWh
df2 = df2.rename(columns={'production_MWh': 'production_kWh'})


print(df2)

# Save the dataset in a csv file
df2.to_csv("production-electrique-par-filiere.csv", index=False)

print('\n')


#Source : https://www.economiedenergie.fr/les-emissions-de-co2-par-energie/ ; Données de l'Ademe
#Creer un nouveau dataframe qui contient 2 colonnes: filiere et CO2 emissions
df3 = pd.DataFrame(columns=['filiere', 'CO2 emissions [gCO2/kWh]'])

#Ajouter les lignes dans le dataframe
df3 = df3.append({'filiere': 'Eolien', 'CO2 emissions [gCO2/kWh]': 9.5}, ignore_index=True)
df3 = df3.append({'filiere': 'Hydraulique', 'CO2 emissions [gCO2/kWh]': 10}, ignore_index=True)
df3 = df3.append({'filiere': 'Nucléaire', 'CO2 emissions [gCO2/kWh]': 6}, ignore_index=True)
df3 = df3.append({'filiere': 'Gaz', 'CO2 emissions [gCO2/kWh]': 443}, ignore_index=True)
df3 = df3.append({'filiere': 'Charbon', 'CO2 emissions [gCO2/kWh]': 1058}, ignore_index=True)
df3 = df3.append({'filiere': 'Fioul', 'CO2 emissions [gCO2/kWh]': 730}, ignore_index=True)
df3 = df3.append({'filiere': 'Géothermie', 'CO2 emissions [gCO2/kWh]': 38}, ignore_index=True)
df3 = df3.append({'filiere': 'Biomasse', 'CO2 emissions [gCO2/kWh]': 32}, ignore_index=True)

print(df3)

#Save the dataframe in a csv file
df3.to_csv('CO2_emissions_by_source.csv', index=False)
print('\n')

# melange les deux frame pour obtenir leur pollution en co2 puis ajoute tous dans un seul afin d'avoir chacun leur pollution
#Enfin faudra que je trouve où trouver des données pour générer de l'elec car plus de nucleaire, trou à combler, regarder les données d'Alexandre

#merge the two dataframes
df4 = pd.merge(df2, df3, on='filiere')

#add a new column to the dataframe
df4['CO2 emissions [gCO2]'] = df4['CO2 emissions [gCO2/kWh]'] * df4['production_kWh']

#Convert the unit of the column CO2 emissions [gCO2] from gCO2 to tCO2
df4['CO2 emissions [gCO2]'] = df4['CO2 emissions [gCO2]'] / 1000000
#rename the column CO2 emissions [gCO2] to CO2 emissions [tCO2]
df4 = df4.rename(columns={'CO2 emissions [gCO2]': 'CO2 emissions [tCO2]'})
#Convert the unit of the column production_kWh from kWh to MWh
df4['production_kWh'] = df4['production_kWh'] / 1000
#rename the column production_kWh to production_MWh
df4 = df4.rename(columns={'production_kWh': 'production_MWh'})

sumProduction = df4['production_MWh'].sum()
df4['percentage_energy_production'] = df4['production_MWh'] / sumProduction * 100

sumCO2 = df4['CO2 emissions [tCO2]'].sum()
df4['percentage_CO2_emissions'] = df4['CO2 emissions [tCO2]'] / sumCO2 * 100

#Remove the column annee
df4 = df4.drop(columns=['annee'])

#Sum where filiere has the same name for the column CO2 emissions [tCO2] and production_MWh
#Comme ça on a la production et les émissions de CO2 pour chaque filière hors chauffage et production electrique
df4 = df4.groupby(['filiere', 'CO2 emissions [gCO2/kWh]']).sum().reset_index()

print(df4)



#Save the dataframe to a csv file
df4.to_csv('CO2_emissions_source.csv', index=False)



#Trouver des études sans le nucléaire
#
#Weka pour des graphes/ pyplot Kmeans
#Regarder les pays qui ont arrêté le nucléaire
#Regarder les pays qui ont arrêté le nucléaire et qui ont des émissions de CO2 plus faibles que la France
#Dechet nucleaire recyclé, 

#Rename the column percentage_energy_production to part_production
df4 = df4.rename(columns={'percentage_energy_production': 'part_production'})

#Save the dataframe to a csv file with the columns filiere, part_production
df4.to_csv('dataset-part_production.csv', columns=['filiere', 'part_production'], index=False)


#Save the dataframe to a csv file with the columns filiere, CO2 emissions [tCO2]
df4.to_csv('dataset-CO2.csv', columns=['filiere', 'CO2 emissions [tCO2]'], index=False)