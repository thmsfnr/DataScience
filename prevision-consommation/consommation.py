import pandas
import matplotlib.pyplot as plt

consommation = pandas.read_csv("cleaneddata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv")

consommation = consommation[consommation["filiere"] == "Electricité"]
consommation = consommation.groupby("annee").sum(numeric_only=True).reset_index()

print(consommation)
print(type(consommation))

consommation.plot(x="annee", y="conso_totale")
# unité mwh, il faut convertir en GW ??
plt.show()

# ensuite extrapoler linéairement
