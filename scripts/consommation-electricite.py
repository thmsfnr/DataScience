import pandas

conso = pandas.read_csv("rawdata/consommation-annuelle-brute.csv", sep=";")

# conservation des attributs utiles
conso = conso[[
    "Année",
    "Consommation brute électricité (GWh) - RTE",
    "Consommation corrigée électricité (GWh) - RTE"
]]

# renommage des attributs
conso = conso.rename(
    columns={
        "Année": "annee",
        "Consommation brute électricité (GWh) - RTE": "conso_brute",
        "Consommation corrigée électricité (GWh) - RTE": "conso_corrigee"
    }
)

conso.to_csv("cleaneddata/consommation-anuelle-electricite-2001-2021.csv", index=False)
