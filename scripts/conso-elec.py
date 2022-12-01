import pandas

consoelec = pandas.read_csv(
    "rawdata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv",
    sep=";",
)

# on conserve que les colonnes utiles
consoelec = consoelec[
    [
        "annee",
        "filiere",
        "code_departement",
        "code_region",
        "consototale",
        "consoa",
        "consoi",
        "consot",
        "consor",
        "consona",
        "libelle_departement",
        "libelle_region",
    ]
]

# renommage des attributs
consoelec = consoelec.rename(
    columns={
        "consoa": "conso_agriculture",
        "consototale": "conso_totale",
        "consoi": "conso_industrie",
        "consot": "conso_tertiaire",
        "consor": "conso_residentiel",
        "consona": "conso_secteur_inconnu",
    }
)

# sauvegarde
consoelec.to_csv(
    "cleaneddata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv",
    index=False,
)

# question : indice qualité : Pourcentage de la consommation annuelle 
# qui est mesurée du 1er janvier au 31 décembre. Il est compris entre 0 et 1
# donc la vraie conso c'est conso + (1-indqual) * conso non ???
