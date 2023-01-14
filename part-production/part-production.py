import pandas as pd
import matplotlib.pyplot as plt

#lecture des fichiers
df_bioenergie = pd.read_csv('cleaneddata/production_electricite_bioenergie.csv')
df_prevision_bioenergie = pd.read_csv('prevision-production/bioenergie/prevision-bioenergie.csv')
df_eolien = pd.read_csv('cleaneddata/production_electricite_eolien.csv')
df_prevision_eolien = pd.read_csv('prevision-production/eolien/prevision-eolien.csv')
df_hydraulique = pd.read_csv('cleaneddata/production_electricite_hydrolique.csv')
df_prevision_hydraulique = pd.read_csv('prevision-production/hydrolique/prevision-hydrolique.csv')
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
df_part_hydraulique = pd.read_csv('part-production/hydrolique/part-production-hydrolique.csv')
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
df_part_bioenergie['annee'] = df_bioenergie_2020['annee']
df_part_bioenergie['part-production-MWh']= (df_bioenergie_2020['production'] / df_production_2020)*100
print(df_part_bioenergie)

df_part_eolien['annee'] = df_eolien_2020['annee']
df_part_eolien['part-production-MWh']= (df_eolien_2020['production'] / df_production_2020)*100
print(df_part_eolien)

df_part_hydraulique['annee'] = df_hydraulique_2020['annee']
df_part_hydraulique['part-production-MWh']= (df_hydraulique_2020['production'] / df_production_2020)*100
print(df_part_hydraulique)

df_part_nucleaire['annee'] = df_nucleaire_2020['annee']
df_part_nucleaire['part-production-MWh']= (df_nucleaire_2020['production'] / df_production_2020)*100
print(df_part_nucleaire)

df_part_solaire['annee'] = df_solaire_2020['annee']
df_part_solaire['part-production-MWh']= (df_solaire_2020['production'] / df_production_2020)*100
print(df_part_solaire)

df_part_charbon['annee'] = df_charbon_2020['annee']
df_part_charbon['part-production-MWh']= (df_charbon_2020['production'] / df_production_2020)*100
print(df_part_charbon)


df_part_gaz['annee'] = df_gaz_2020['annee']
df_part_gaz['part-production-MWh']= (df_gaz_2020['production'] / df_production_2020)*100



#selection production totale de 2021 à 2030 et production par annee des filieres
for annee in range(2021, 2031):
    df_prevision = pd.concat([df_prevision_bioenergie[['ds','yhat']][df_prevision_bioenergie['ds'] == str(annee) + '-12-31'],df_prevision_eolien[['ds','yhat']][df_prevision_eolien['ds'] == str(annee) + '-12-31'],df_prevision_charbon[['ds','yhat']][df_prevision_charbon['ds'] == str(annee) + '-12-31'],df_prevision_gaz[['ds','yhat']][df_prevision_gaz['ds'] == str(annee) + '-12-31'],df_prevision_hydraulique[['ds','yhat']][df_prevision_hydraulique['ds'] == str(annee) + '-12-31'],df_prevision_nucleaire[['ds','yhat']][df_prevision_nucleaire['ds'] == str(annee) + '-12-31'],df_prevision_solaire[['ds','yhat']][df_prevision_solaire['ds'] == str(annee) + '-12-31']])
    #print(df_prevision)
    df_prevision = df_prevision.rename(columns={'yhat': 'production_'+str(annee)})
    df_prevision = df_prevision['production_'+str(annee)].sum()
    #print(df_prevision)
    df_part_bioenergie['annee'] = df_prevision_bioenergie['ds'][df_prevision_bioenergie['ds'] == str(annee) + '-12-31']
    #print(df_part_bioenergie)
    df_part_bioenergie['part-production-MWh']= (df_prevision_bioenergie['yhat'][df_prevision_bioenergie['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    #print(df_part_bioenergie)
    '''
    df_part_eolien['annee'] = df_prevision_eolien['ds'][df_prevision_eolien['ds'] == str(annee) + '-12-31']
    df_part_eolien['part-production-MWh']= (df_prevision_eolien['yhat'][df_prevision_eolien['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    df_part_charbon['annee'] = df_prevision_charbon['ds'][df_prevision_charbon['ds'] == str(annee) + '-12-31']
    df_part_charbon['part-production-MWh']= (df_prevision_charbon['yhat'][df_prevision_charbon['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    df_part_gaz['annee'] = df_prevision_gaz['ds'][df_prevision_gaz['ds'] == str(annee) + '-12-31']
    df_part_gaz['part-production-MWh']= (df_prevision_gaz['yhat'][df_prevision_gaz['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    df_part_hydraulique['annee'] = df_prevision_hydraulique['ds'][df_prevision_hydraulique['ds'] == str(annee) + '-12-31']
    df_part_hydraulique['part-production-MWh']= (df_prevision_hydraulique['yhat'][df_prevision_hydraulique['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    df_part_nucleaire['annee'] = df_prevision_nucleaire['ds'][df_prevision_nucleaire['ds'] == str(annee) + '-12-31']
    df_part_nucleaire['part-production-MWh']= (df_prevision_nucleaire['yhat'][df_prevision_nucleaire['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    df_part_solaire['annee'] = df_prevision_solaire['ds'][df_prevision_solaire['ds'] == str(annee) + '-12-31']
    df_part_solaire['part-production-MWh']= (df_prevision_solaire['yhat'][df_prevision_solaire['ds'] == str(annee) + '-12-31'] / df_prevision)*100
    '''
print(df_part_bioenergie)
'''
#mise en forme colonne production
df_prevision_2021 = df_prevision_2021.rename(columns={'yhat': 'production_2021'})
df_prevision_2021.drop(['ds'], axis=1, inplace=True)
df_prevision_2021 = df_prevision_2021.sum()

df_prevision_2022 = df_prevision_2022.rename(columns={'yhat': 'production_2022'})
df_prevision_2022.drop(['ds'], axis=1, inplace=True)
df_prevision_2022 = df_prevision_2022.sum()

df_prevision_2023 = df_prevision_2023.rename(columns={'yhat': 'production_2023'})
df_prevision_2023.drop(['ds'], axis=1, inplace=True)
df_prevision_2023 = df_prevision_2023.sum()

df_prevision_2024 = df_prevision_2024.rename(columns={'yhat': 'production_2024'})
df_prevision_2024.drop(['ds'], axis=1, inplace=True)
df_prevision_2024 = df_prevision_2024.sum()

df_prevision_2025 = df_prevision_2025.rename(columns={'yhat': 'production_2025'})
df_prevision_2025.drop(['ds'], axis=1, inplace=True)
df_prevision_2025 = df_prevision_2025.sum()

df_prevision_2026 = df_prevision_2026.rename(columns={'yhat': 'production_2026'})
df_prevision_2026.drop(['ds'], axis=1, inplace=True)
df_prevision_2026 = df_prevision_2026.sum()

df_prevision_2027 = df_prevision_2027.rename(columns={'yhat': 'production_2027'})
df_prevision_2027.drop(['ds'], axis=1, inplace=True)
df_prevision_2027 = df_prevision_2027.sum()

df_prevision_2028 = df_prevision_2028.rename(columns={'yhat': 'production_2028'})
df_prevision_2028.drop(['ds'], axis=1, inplace=True)
df_prevision_2028 = df_prevision_2028.sum()

df_prevision_2029 = df_prevision_2029.rename(columns={'yhat': 'production_2029'})
df_prevision_2029.drop(['ds'], axis=1, inplace=True)
df_prevision_2029 = df_prevision_2029.sum()

df_prevision_2030 = df_prevision_2030.rename(columns={'yhat': 'production_2030'})
df_prevision_2030.drop(['ds'], axis=1, inplace=True)
df_prevision_2030 = df_prevision_2030.sum()




part_bioenergie_2022 = df_production_bioenergie_2022 / df_prevision_2022['production_2022'] *100
part_bioenergie_2023 = df_production_bioenergie_2023 / df_prevision_2023['production_2023'] *100
part_bioenergie_2024 = df_production_bioenergie_2024 / df_prevision_2024['production_2024'] *100
part_bioenergie_2025 = df_production_bioenergie_2025 / df_prevision_2025['production_2025'] *100
part_bioenergie_2026 = df_production_bioenergie_2026 / df_prevision_2026['production_2026'] *100
part_bioenergie_2027 = df_production_bioenergie_2027 / df_prevision_2027['production_2027'] *100
part_bioenergie_2028 = df_production_bioenergie_2028 / df_prevision_2028['production_2028'] *100
part_bioenergie_2029 = df_production_bioenergie_2029 / df_prevision_2029['production_2029'] *100
part_bioenergie_2030 = df_production_bioenergie_2030 / df_prevision_2030['production_2030'] *100

#calcul part de production eolien par année
part_eolien_2020 = df_eolien_2020['production'] / df_production_2020['production_2020'] *100
part_eolien_2021 = df_production_eolien_2021 / df_prevision_2021['production_2021'] *100
part_eolien_2022 = df_production_eolien_2022 / df_prevision_2022['production_2022'] *100
part_eolien_2023 = df_production_eolien_2023 / df_prevision_2023['production_2023'] *100
part_eolien_2024 = df_production_eolien_2024 / df_prevision_2024['production_2024'] *100
part_eolien_2025 = df_production_eolien_2025 / df_prevision_2025['production_2025'] *100
part_eolien_2026 = df_production_eolien_2026 / df_prevision_2026['production_2026'] *100
part_eolien_2027 = df_production_eolien_2027 / df_prevision_2027['production_2027'] *100
part_eolien_2028 = df_production_eolien_2028 / df_prevision_2028['production_2028'] *100
part_eolien_2029 = df_production_eolien_2029 / df_prevision_2029['production_2029'] *100
part_eolien_2030 = df_production_eolien_2030 / df_prevision_2030['production_2030'] *100

#calcul part de production solaire par année
part_solaire_2020 = df_solaire_2020['production'] / df_production_2020['production_2020'] *100 
part_solaire_2021 = df_production_solaire_2021 / df_prevision_2021['production_2021'] *100
part_solaire_2022 = df_production_solaire_2022 / df_prevision_2022['production_2022'] *100
part_solaire_2023 = df_production_solaire_2023 / df_prevision_2023['production_2023'] *100
part_solaire_2024 = df_production_solaire_2024 / df_prevision_2024['production_2024'] *100
part_solaire_2025 = df_production_solaire_2025 / df_prevision_2025['production_2025'] *100
part_solaire_2026 = df_production_solaire_2026 / df_prevision_2026['production_2026'] *100
part_solaire_2027 = df_production_solaire_2027 / df_prevision_2027['production_2027'] *100
part_solaire_2028 = df_production_solaire_2028 / df_prevision_2028['production_2028'] *100
part_solaire_2029 = df_production_solaire_2029 / df_prevision_2029['production_2029'] *100
part_solaire_2030 = df_production_solaire_2030 / df_prevision_2030['production_2030'] *100

#calcul part de production hydraulique par année
part_hydraulique_2020 = df_hydraulique_2020['production'] / df_production_2020['production_2020'] *100
part_hydraulique_2021 = df_production_hydraulique_2021 / df_prevision_2021['production_2021'] *100
part_hydraulique_2022 = df_production_hydraulique_2022 / df_prevision_2022['production_2022'] *100
part_hydraulique_2023 = df_production_hydraulique_2023 / df_prevision_2023['production_2023'] *100
part_hydraulique_2024 = df_production_hydraulique_2024 / df_prevision_2024['production_2024'] *100
part_hydraulique_2025 = df_production_hydraulique_2025 / df_prevision_2025['production_2025'] *100
part_hydraulique_2026 = df_production_hydraulique_2026 / df_prevision_2026['production_2026'] *100
part_hydraulique_2027 = df_production_hydraulique_2027 / df_prevision_2027['production_2027'] *100
part_hydraulique_2028 = df_production_hydraulique_2028 / df_prevision_2028['production_2028'] *100
part_hydraulique_2029 = df_production_hydraulique_2029 / df_prevision_2029['production_2029'] *100
part_hydraulique_2030 = df_production_hydraulique_2030 / df_prevision_2030['production_2030'] *100

#calcul part de production nucléaire par année
part_nucleaire_2020 = df_nucleaire_2020['production'] / df_production_2020['production_2020'] *100
part_nucleaire_2021 = df_production_nucleaire_2021 / df_prevision_2021['production_2021'] *100
part_nucleaire_2022 = df_production_nucleaire_2022 / df_prevision_2022['production_2022'] *100
part_nucleaire_2023 = df_production_nucleaire_2023 / df_prevision_2023['production_2023'] *100
part_nucleaire_2024 = df_production_nucleaire_2024 / df_prevision_2024['production_2024'] *100
part_nucleaire_2025 = df_production_nucleaire_2025 / df_prevision_2025['production_2025'] *100
part_nucleaire_2026 = df_production_nucleaire_2026 / df_prevision_2026['production_2026'] *100
part_nucleaire_2027 = df_production_nucleaire_2027 / df_prevision_2027['production_2027'] *100
part_nucleaire_2028 = df_production_nucleaire_2028 / df_prevision_2028['production_2028'] *100
part_nucleaire_2029 = df_production_nucleaire_2029 / df_prevision_2029['production_2029'] *100
part_nucleaire_2030 = df_production_nucleaire_2030 / df_prevision_2030['production_2030'] *100

#calcul part de production gaz par année
part_gaz_2020 = df_gaz_2020['production'] / df_production_2020['production_2020'] *100
part_gaz_2021 = df_production_gaz_2021 / df_prevision_2021['production_2021'] *100
part_gaz_2022 = df_production_gaz_2022 / df_prevision_2022['production_2022'] *100
part_gaz_2023 = df_production_gaz_2023 / df_prevision_2023['production_2023'] *100
part_gaz_2024 = df_production_gaz_2024 / df_prevision_2024['production_2024'] *100
part_gaz_2025 = df_production_gaz_2025 / df_prevision_2025['production_2025'] *100
part_gaz_2026 = df_production_gaz_2026 / df_prevision_2026['production_2026'] *100
part_gaz_2027 = df_production_gaz_2027 / df_prevision_2027['production_2027'] *100
part_gaz_2028 = df_production_gaz_2028 / df_prevision_2028['production_2028'] *100
part_gaz_2029 = df_production_gaz_2029 / df_prevision_2029['production_2029'] *100
part_gaz_2030 = df_production_gaz_2030 / df_prevision_2030['production_2030'] *100

#calcul part de production charbon par année
part_charbon_2020 = df_charbon_2020['production'] / df_production_2020['production_2020'] *100
part_charbon_2021 = df_production_charbon_2021 / df_prevision_2021['production_2021'] *100
part_charbon_2022 = df_production_charbon_2022 / df_prevision_2022['production_2022'] *100
part_charbon_2023 = df_production_charbon_2023 / df_prevision_2023['production_2023'] *100
part_charbon_2024 = df_production_charbon_2024 / df_prevision_2024['production_2024'] *100
part_charbon_2025 = df_production_charbon_2025 / df_prevision_2025['production_2025'] *100
part_charbon_2026 = df_production_charbon_2026 / df_prevision_2026['production_2026'] *100
part_charbon_2027 = df_production_charbon_2027 / df_prevision_2027['production_2027'] *100


'''



