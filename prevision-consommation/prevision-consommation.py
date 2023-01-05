# https://www.edf.fr/groupe-edf/espaces-dedies/l-energie-de-a-a-z/tout-sur-l-energie/l-electricite-au-quotidien/la-consommation-d-electricite-en-chiffres
# https://www.rte-france.com/actualites/bilan-electrique-francais-2019-une-consommation-en-baisse-depuis-10-ans-une-production

# rte -> soit essayer de récupérer via l'API, soit extraire manuellement les données des PDFs

# https://bilan-electrique-2020.rte-france.com/#
# https://bilan-electrique-2021.rte-france.com/#

# https://bilan-electrique-2021.rte-france.com/consommation_evolution_de_la_consommation-2
# https://odre.opendatasoft.com/explore/dataset/consommation-annuelle-brute/table/?sort=-annee
# différence consommation brute / corrigée expliquée ici https://www.edf.fr/groupe-edf/espaces-dedies/l-energie-de-a-a-z/tout-sur-l-energie/l-electricite-au-quotidien/la-consommation-d-electricite-en-chiffres

import pandas

conso = pandas.read_csv("cleaneddata/consommation-anuelle-electricite-2001-2021.csv")
print(conso)


# brute : c'est la consommation totale d'électricité. 
# Elle comprend non seulement la consommation finale des consommateurs 
# mais également la consommation nécessaire à fournir l'électricité,
# les pertes dûes à la transformation et au transport et les écarts statistiques telles que la météorologie.

# corrigée : c'est la consommation corrigée des aléas climatiques 
# (les températures sont remplacées par des températures de référence) 
# et des effets calendaires (comme les années bissextiles).
# Elle permet d’observer plus finement les évolutions structurelles.
