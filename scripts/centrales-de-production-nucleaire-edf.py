#pip pandas
import pandas as pd

donnees = pd.read_csv('../rawdata/centrales-de-production-nucleaire-edf.csv',sep=';')

# on conserve que les colonnes utiles
donneesCentrales = donnees[[
    'centrale',
    'filiere',
    'sous_filiere',
    'combustible',
    'code_insee_region',
    'region',
    'departement',
    'code_insee_departement',
    'date_de_mise_en_service_industrielle',
    'puissance_installee',
    'unite'
]]
donneesCentrales.to_csv('../cleaneddata/centrales-de-production-nucleaire-edf.csv', index=False)

#on peut regrouper par date de mise en service ?
