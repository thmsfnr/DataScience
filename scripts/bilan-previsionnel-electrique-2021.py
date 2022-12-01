import pandas

bilanprevisionnel = pandas.read_csv(
    "rawdata/bilan-previsionnel-electrique-2021-offre-de-production.csv", sep=";"
)

# on conserve que les attributs utiles
bilanprevisionnel = bilanprevisionnel[
    [
        "annee",
        "nucleaire_gw",
        "cycles_combines_au_gaz_gw",
        "turbines_a_combustion_gw",
        "hydraulique_gw",
        "eolien_gw",
        "photovoltaique_gw",
    ]
]

# pas besoin de renommer, c'est clair dès quand on sait que gw = gigawatt
bilanprevisionnel.to_csv(
    "cleaneddata/bilan-previsionel-electrique-2021-offre-de-production.csv", index=False
)
