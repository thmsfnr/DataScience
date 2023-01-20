import pandas as pd

#-----------Lecture dataframe--------------------------------------------------------------   
df_bioenergie_prevision = pd.read_csv('prevision-production/bioenergie/prevision-bioenergie.csv', sep=',')
df_bioenergie_actuelle = pd.read_csv('cleaneddata/production_electricite_bioenergie.csv', sep=',')
df_charbon_prevision = pd.read_csv('prevision-production/charbon/prevision-charbon.csv', sep=',')
df_charbon_actuelle = pd.read_csv('cleaneddata/production_electricite_charbon.csv', sep=',')
df_eolien_prevision = pd.read_csv('prevision-production/eolien/prevision-eolien.csv', sep=',')
df_eolien_actuelle = pd.read_csv('cleaneddata/production_electricite_eolien.csv', sep=',')
df_gaz_prevision = pd.read_csv('prevision-production/gaz/prevision-gaz.csv', sep=',')
df_gaz_actuelle = pd.read_csv('cleaneddata/production_electricite_gaz.csv', sep=',')
df_hydro_prevision = pd.read_csv('prevision-production/hydraulique/prevision-hydraulique.csv', sep=',')
df_hydro_actuelle = pd.read_csv('cleaneddata/production_electricite_hydraulique.csv', sep=',')
df_nucleaire_prevision = pd.read_csv('prevision-production/nucleaire/prevision-nucleaire.csv', sep=',')
df_nucleaire_actuelle = pd.read_csv('cleaneddata/production_electricite_nucleaire.csv', sep=',')
df_solaire_prevision = pd.read_csv('prevision-production/solaire/prevision-solaire.csv', sep=',')
df_solaire_actuelle = pd.read_csv('cleaneddata/production_electricite_solaire.csv', sep=',')

#-----------Nettoyage dataframe------------------------------------------------------------
#bioenergie
df_bioenergie_prevision = df_bioenergie_prevision[df_bioenergie_prevision['ds'] > '2020-12-31']
df_bioenergie_prevision = df_bioenergie_prevision[['ds','yhat']]
df_bioenergie_prevision = df_bioenergie_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_bioenergie = pd.concat([df_bioenergie_actuelle,df_bioenergie_prevision], axis=0)
df_bioenergie['filiere'] = "bioénergie"

#charbon
df_charbon_prevision = df_charbon_prevision[df_charbon_prevision['ds'] > '2020-12-31']
df_charbon_prevision = df_charbon_prevision[['ds','yhat']]
df_charbon_prevision = df_charbon_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_charbon_actuelle['production électricité TWh'] = df_charbon_actuelle['production électricité TWh'] * 1000000
df_charbon_actuelle = df_charbon_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_charbon = pd.concat([df_charbon_actuelle,df_charbon_prevision], axis=0)
df_charbon['filiere'] = "charbon"

#eolien
df_eolien_prevision = df_eolien_prevision[df_eolien_prevision['ds'] > '2020-12-31']
df_eolien_prevision = df_eolien_prevision[['ds','yhat']]
df_eolien_prevision = df_eolien_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_eolien_actuelle['production électricité TWh'] = df_eolien_actuelle['production électricité TWh'] * 1000000
df_eolien_actuelle = df_eolien_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_eolien = pd.concat([df_eolien_actuelle,df_eolien_prevision], axis=0)
df_eolien['filiere'] = "éolien"

#gaz
df_gaz_prevision = df_gaz_prevision[df_gaz_prevision['ds'] > '2020-12-31']
df_gaz_prevision = df_gaz_prevision[['ds','yhat']]
df_gaz_prevision = df_gaz_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_gaz_actuelle['production électricité TWh'] = df_gaz_actuelle['production électricité TWh'] * 1000000
df_gaz_actuelle = df_gaz_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_gaz = pd.concat([df_gaz_actuelle,df_gaz_prevision], axis=0)
df_gaz['filiere'] = "gaz"

#hydraulique
df_hydro_prevision = df_hydro_prevision[df_hydro_prevision['ds'] > '2020-12-31']
df_hydro_prevision = df_hydro_prevision[['ds','yhat']]
df_hydro_prevision = df_hydro_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_hydro_actuelle['production électricité TWh'] = df_hydro_actuelle['production électricité TWh'] * 1000000
df_hydro_actuelle = df_hydro_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_hydro = pd.concat([df_hydro_actuelle,df_hydro_prevision], axis=0)
df_hydro['filiere'] = "hydraulique"

#nucleaire
df_nucleaire_prevision = df_nucleaire_prevision[df_nucleaire_prevision['ds'] > '2020-12-31']
df_nucleaire_prevision = df_nucleaire_prevision[['ds','yhat']]
df_nucleaire_prevision = df_nucleaire_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_nucleaire_actuelle["production électricité TWh"] = df_nucleaire_actuelle["production électricité TWh"] * 1000000
df_nucleaire_actuelle = df_nucleaire_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_nucleaire = pd.concat([df_nucleaire_actuelle,df_nucleaire_prevision], axis=0)
df_nucleaire['filiere'] = "nucléaire"

#solaire
df_solaire_prevision = df_solaire_prevision[df_solaire_prevision['ds'] > '2020-12-31']
df_solaire_prevision = df_solaire_prevision[['ds','yhat']]
df_solaire_prevision = df_solaire_prevision.rename(columns={'ds':'annee','yhat':'production électricité MWh'})
df_solaire_actuelle['production électricité TWh'] = df_solaire_actuelle['production électricité TWh'] * 1000000
df_solaire_actuelle = df_solaire_actuelle.rename(columns={'production électricité TWh':'production électricité MWh'})
df_solaire = pd.concat([df_solaire_actuelle,df_solaire_prevision], axis=0)
df_solaire['filiere'] = "solaire"

#fusion de tous les dataframes
df_production = pd.concat([df_bioenergie,df_charbon,df_eolien,df_gaz,df_hydro,df_nucleaire,df_solaire], axis=0)
df_production['annee']= df_production['annee'].replace(regex="-12-31",value="")
df_production = df_production.rename(columns={'production électricité MWh':'production_electricite_MWh'})


#sauvegarde du dataframe
df_production.to_csv('cleaneddata/df_production.csv', index=False)




