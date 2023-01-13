# https://www.edf.fr/groupe-edf/espaces-dedies/l-energie-de-a-a-z/tout-sur-l-energie/l-electricite-au-quotidien/la-consommation-d-electricite-en-chiffres
# https://www.rte-france.com/actualites/bilan-electrique-francais-2019-une-consommation-en-baisse-depuis-10-ans-une-production

# rte -> soit essayer de récupérer via l'API, soit extraire manuellement les données des PDFs

# https://bilan-electrique-2020.rte-france.com/#
# https://bilan-electrique-2021.rte-france.com/#

# https://bilan-electrique-2021.rte-france.com/consommation_evolution_de_la_consommation-2
# https://odre.opendatasoft.com/explore/dataset/consommation-annuelle-brute/table/?sort=-annee
# différence consommation brute / corrigée expliquée ici https://www.edf.fr/groupe-edf/espaces-dedies/l-energie-de-a-a-z/tout-sur-l-energie/l-electricite-au-quotidien/la-consommation-d-electricite-en-chiffres

import pandas
import matplotlib.pyplot as plt
from prophet import Prophet
from prophet.plot import plot_cross_validation_metric
from prophet.diagnostics import performance_metrics
from prophet.diagnostics import cross_validation
import time

df = pandas.read_csv("cleaneddata/consommation-anuelle-electricite-2001-2021.csv")

# brute : c'est la consommation totale d'électricité.
# Elle comprend non seulement la consommation finale des consommateurs
# mais également la consommation nécessaire à fournir l'électricité,
# les pertes dûes à la transformation et au transport et les écarts statistiques telles que la météorologie.

# corrigée : c'est la consommation corrigée des aléas climatiques
# (les températures sont remplacées par des températures de référence)
# et des effets calendaires (comme les années bissextiles).
# Elle permet d’observer plus finement les évolutions structurelles.

### nettoyage des données

df = df.drop("conso_brute", axis=1)

# conversion GWh en MWh
df["conso_corrigee"] = df["conso_corrigee"] * 1000

df["annee"] = pandas.to_datetime(df["annee"], format="%Y")

df.columns = ["ds", "y"]
print(df)

### graphique
plt.figure(figsize=(17, 8))
plt.plot(df["ds"], df["y"])
plt.xlabel("Année")
plt.ylabel("Consommation d'électricité (en MWh)")
plt.title("Consommation d'électricité (en MWh) en France, en fonction des années")
plt.grid(False)
# plt.show()
plt.savefig("prevision-consommation/consommation-2001-2021-france.png")


### prédiction

# Creation objet prophet
m = Prophet()
# Entrainement du modèle
m.fit(df)
# prediction des 10 prochaines années par défault ça compare avec les données historiques
future = m.make_future_dataframe(periods=10, freq="Y")
forecast = m.predict(future)
fig = m.plot(forecast)
plt.xlabel("Année")
plt.ylabel("Consommation d'électricité (en MWh)")
plt.title("Consommation d'électricité (en MWh) en France, en fonction des années")
# plt.show()
plt.savefig("prevision-consommation/prediction-consommation.png")


## tendance

m.plot_components(forecast)
plt.xlabel("Année")
plt.ylabel("Consommation d'électricité (en MWh) en France")
plt.show()

### cross-validation
# 2021-2001 = 20 ans -> 10 ans test
df_cv = cross_validation(m, initial="3650 days", period="365 days", horizon="3650 days")
print("CROSS VALIDATION")
print(df_cv)

def afficheGraphePrediction(df,forecast,title):
    plt.figure(figsize=(17, 8))
    plt.plot(forecast['ds'],forecast['yhat'],label='valeurs prédites')
    plt.plot(forecast['ds'],forecast['yhat_lower'],label='valeurs inférieures prédites')
    plt.plot(forecast['ds'],forecast['yhat_upper'],label='valeurs supérieures prédites')
    plt.plot(df['ds'],df['y'],label='valeurs réelles')
    plt.legend()
    plt.xlabel('Année')
    plt.ylabel("Consommation d'électricité (en MWh) en France")
    plt.title(title)
    plt.grid(False)
    plt.show()


afficheGraphePrediction(
    df_cv,
    df_cv,
    "Analyse de la cross-validation de la consommation d'électricité (en MWh) en France en fonction des années",
)

df_p = performance_metrics(df_cv)
print("INDICATEUR PERFORMANCE")
print(df_p)

fig = plot_cross_validation_metric(df_cv, metric='mape')
plt.show()
plot_cross_validation_metric(df_cv, metric='rmse')
plt.show()
