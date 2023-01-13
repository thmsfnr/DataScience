import pandas
import matplotlib.pyplot as plt

bilanprevisionnel = pandas.read_csv(
    "cleaneddata/bilan-previsionel-electrique-2021-offre-de-production.csv"
)

bilanprevisionnel = bilanprevisionnel.drop(["total"], axis=1)
bilanprevisionnel.plot.bar(stacked=True, x="annee")

plt.xlabel("Année")
plt.ylabel("Production (en GW)")
plt.title("Prévision de production d'électricité (ORE)")
plt.savefig("prevision-consommation/bilan-previsionnel-ore.png")
