import pandas as pd
import matplotlib.pyplot as plt

#lecture des fichiers
df_bioenergie = pd.read_csv('cleaneddata/production_electricite_bioenergie.csv')
df_prevision_bioenergie = pd.read_csv('prevision-production/bioenergie/prevision-bioenergie.csv')
df_eolien = pd.read_csv('cleaneddata/production_electricite_eolien.csv')
df_prevision_eolien = pd.read_csv('prevision-production/eolien/prevision-eolien.csv')
df_hydraulique = pd.read_csv('cleaneddata/production_electricite_hydraulique.csv')
df_prevision_hydraulique = pd.read_csv('prevision-production/hydraulique/prevision-hydraulique.csv')
df_nucleaire = pd.read_csv('cleaneddata/production_electricite_nucleaire.csv')
df_prevision_nucleaire = pd.read_csv('prevision-production/nucleaire/prevision-nucleaire.csv')
df_solaire = pd.read_csv('cleaneddata/production_electricite_solaire.csv')
df_prevision_solaire = pd.read_csv('prevision-production/solaire/prevision-solaire.csv')
df_charbon = pd.read_csv('cleaneddata/production_electricite_charbon.csv')
df_prevision_charbon = pd.read_csv('prevision-production/charbon/prevision-charbon.csv')
df_gaz = pd.read_csv('cleaneddata/production_electricite_gaz.csv')
df_prevision_gaz = pd.read_csv('prevision-production/gaz/prevision-gaz.csv')
#les parts de production
df_part_bioenergie = pd.read_csv('part-production/bioenergie/part-production-bioenergie.csv')
df_part_charbon = pd.read_csv('part-production/charbon/part-production-charbon.csv')
df_part_eolien = pd.read_csv('part-production/eolien/part-production-eolien.csv')
df_part_gaz = pd.read_csv('part-production/gaz/part-production-gaz.csv')
df_part_hydraulique = pd.read_csv('part-production/hydraulique/part-production-hydraulique.csv')
df_part_nucleaire = pd.read_csv('part-production/nucleaire/part-production-nucleaire.csv')
df_part_solaire = pd.read_csv('part-production/solaire/part-production-solaire.csv')

# production 2020
df_bioenergie_2020 = df_bioenergie[df_bioenergie['annee'] == 2020]
df_eolien_2020 = df_eolien[df_eolien['annee'] == 2020]
df_hydraulique_2020 = df_hydraulique[df_hydraulique['annee'] == 2020]
df_nucleaire_2020 = df_nucleaire[df_nucleaire['annee'] == 2020]
df_solaire_2020 = df_solaire[df_solaire['annee'] == 2020]
df_charbon_2020 = df_charbon[df_charbon['annee'] == 2020]
df_gaz_2020 = df_gaz[df_gaz['annee'] == 2020]

# normalisation nom colonne de production & unité en MWh
df_bioenergie_2020 = df_bioenergie_2020.rename(columns={'production électricité MWh': 'production'})
df_eolien_2020 = df_eolien_2020.rename(columns={'production électricité TWh': 'production'})
df_eolien_2020['production'] = df_eolien_2020['production'] * 1000000
df_hydraulique_2020 = df_hydraulique_2020.rename(columns={'production électricité TWh': 'production'})
df_hydraulique_2020['production'] = df_hydraulique_2020['production'] * 1000000
df_nucleaire_2020 = df_nucleaire_2020.rename(columns={'production électricité TWh': 'production'})
df_nucleaire_2020['production'] = df_nucleaire_2020['production'] * 1000000
df_solaire_2020 = df_solaire_2020.rename(columns={'production électricité TWh': 'production'})
df_solaire_2020['production'] = df_solaire_2020['production'] * 1000000
df_charbon_2020 = df_charbon_2020.rename(columns={'production électricité TWh': 'production'})
df_charbon_2020['production'] = df_charbon_2020['production'] * 1000000
df_gaz_2020 = df_gaz_2020.rename(columns={'production électricité TWh': 'production'})
df_gaz_2020['production'] = df_gaz_2020['production'] * 1000000

# production totale 2020
df_production_2020 = pd.concat([df_bioenergie_2020, df_eolien_2020, df_hydraulique_2020, df_nucleaire_2020, df_solaire_2020, df_charbon_2020, df_gaz_2020])
df_production_2020 = df_production_2020['production'].sum()

#ajout part 2020
df_stock_2020 = df_bioenergie_2020['production']  #df_stock_2020 est une série
df_part_bioenergie.loc[len(df_part_bioenergie)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]
df_stock_2020 = df_eolien_2020['production']
df_part_eolien.loc[len(df_part_eolien)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]
df_stock_2020 = df_hydraulique_2020['production']
df_part_hydraulique.loc[len(df_part_hydraulique)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]
df_stock_2020 = df_nucleaire_2020['production']
df_part_nucleaire.loc[len(df_part_nucleaire)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]
df_stock_2020 = df_solaire_2020['production']
df_part_solaire.loc[len(df_part_solaire)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]
df_stock_2020 = df_charbon_2020['production']
df_part_charbon.loc[len(df_part_charbon)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]
df_stock_2020 = df_gaz_2020['production']
df_part_gaz.loc[len(df_part_gaz)] = [str(2020),(df_stock_2020.values[0] / df_production_2020)*100]

#selection production totale de 2021 à 2030 et production par annee des filieres & prevision production
for annee in range(2021, 2031):
    #bioenergie
    df_prevision = pd.concat([df_prevision_bioenergie[['ds','yhat']][df_prevision_bioenergie['ds'] == str(annee) + '-12-31'],df_prevision_eolien[['ds','yhat']][df_prevision_eolien['ds'] == str(annee) + '-12-31'],df_prevision_charbon[['ds','yhat']][df_prevision_charbon['ds'] == str(annee) + '-12-31'],df_prevision_gaz[['ds','yhat']][df_prevision_gaz['ds'] == str(annee) + '-12-31'],df_prevision_hydraulique[['ds','yhat']][df_prevision_hydraulique['ds'] == str(annee) + '-12-31'],df_prevision_nucleaire[['ds','yhat']][df_prevision_nucleaire['ds'] == str(annee) + '-12-31'],df_prevision_solaire[['ds','yhat']][df_prevision_solaire['ds'] == str(annee) + '-12-31']])
    df_prevision = df_prevision.rename(columns={'yhat': 'production_'+str(annee)})
    df_prevision = df_prevision['production_'+str(annee)].sum()
    df_stock_bioenergie = df_prevision_bioenergie['yhat'][df_prevision_bioenergie['ds'] == str(annee) + '-12-31'] #df_stock est une série
    df_stock_eolien = df_prevision_eolien['yhat'][df_prevision_eolien['ds'] == str(annee) + '-12-31']
    df_stock_hydraulique = df_prevision_hydraulique['yhat'][df_prevision_hydraulique['ds'] == str(annee) + '-12-31']
    df_stock_nucleaire = df_prevision_nucleaire['yhat'][df_prevision_nucleaire['ds'] == str(annee) + '-12-31']
    df_stock_solaire = df_prevision_solaire['yhat'][df_prevision_solaire['ds'] == str(annee) + '-12-31']
    df_stock_charbon = df_prevision_charbon['yhat'][df_prevision_charbon['ds'] == str(annee) + '-12-31']
    df_stock_gaz = df_prevision_gaz['yhat'][df_prevision_gaz['ds'] == str(annee) + '-12-31']
   
    for production_actuelle in df_stock_bioenergie.values:
        df_part_bioenergie.loc[len(df_part_bioenergie)] = [str(annee), (production_actuelle / df_prevision)*100]

    for production_actuelle in df_stock_eolien.values:
        df_part_eolien.loc[len(df_part_eolien)] = [str(annee), (production_actuelle / df_prevision)*100]
    
    for production_actuelle in df_stock_hydraulique.values:
        df_part_hydraulique.loc[len(df_part_hydraulique)] = [str(annee), (production_actuelle / df_prevision)*100]

    for production_actuelle in df_stock_nucleaire.values:
        df_part_nucleaire.loc[len(df_part_nucleaire)] = [str(annee), (production_actuelle / df_prevision)*100]

    for production_actuelle in df_stock_solaire.values:
        df_part_solaire.loc[len(df_part_solaire)] = [str(annee), (production_actuelle / df_prevision)*100]

    for production_actuelle in df_stock_charbon.values:
        df_part_charbon.loc[len(df_part_charbon)] = [str(annee), (production_actuelle / df_prevision)*100]

    for production_actuelle in df_stock_gaz.values:
        df_part_gaz.loc[len(df_part_gaz)] = [str(annee), (production_actuelle / df_prevision)*100]

  
print(df_part_bioenergie)
print(df_part_eolien)
print(df_part_hydraulique)
print(df_part_nucleaire)
print(df_part_solaire)
print(df_part_charbon)
print(df_part_gaz)

#sauvagegarde des données
df_part_bioenergie.to_csv('part-production/bioenergie/part_production_bioenergie.csv', index=False)
df_part_eolien.to_csv('part-production/eolien/part_production_eolien.csv', index=False)
df_part_hydraulique.to_csv('part-production/hydraulique/part_production_hydraulique.csv', index=False)
df_part_nucleaire.to_csv('part-production/nucleaire/part_production_nucleaire.csv', index=False)
df_part_solaire.to_csv('part-production/solaire/part_production_solaire.csv', index=False)
df_part_charbon.to_csv('part-production/charbon/part_production_charbon.csv', index=False)
df_part_gaz.to_csv('part-production/gaz/part_production_gaz.csv', index=False)





