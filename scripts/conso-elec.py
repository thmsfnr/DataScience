import pandas

consoelec = pandas.read_csv(
    "../rawdata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv",
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


consoelec['libelle_departement'].str.replace('-',' ')
consoelec['libelle_region'].str.replace('-',' ')
print(consoelec['libelle_departement'])

consoelec.to_csv(
    "../cleaneddata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement-TEST.csv",
    index=False,
)


