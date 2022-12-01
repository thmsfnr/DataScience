#pip pandas
import pandas as pd

donnees = pd.read_csv('../rawdata/origine-de-lelectricite-fournie-par-edf-sa.csv',sep=';')


# on conserve que les colonnes utiles
donneesOrigineElectricite = donnees[[
    'annee',
    'categorie',
    'sous_categorie',
    'valeur',
    'unite',
]]
donneesOrigineElectricite.to_csv('../cleaneddata/origine-de-lelectricite-fournie-par-edf-sa.csv', index=False)


# valeur ? c'est quoi ? combien on fournie d'électricité par catégorie ?

#peut etre renommer "catégorie" mais je ne sais pas quoi dire à la place ?
#idem pour sous_categorie
#est-ce qu'on garde que les années 2021 ? 2020 ? voir avec les autres donneés
#on peut regrouper par années aussi 