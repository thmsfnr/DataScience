import pandas
import matplotlib.pyplot as plt
from prophet import Prophet

# from prophet.plot import plot_cross_validation_metric
from prophet.diagnostics import cross_validation

df = pandas.read_csv(
    "cleaneddata/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv"
)

# préparation des données

# on prend en compte que l'électricité
df = df[df["filiere"] == "Electricité"]
df = df.groupby("annee").sum(numeric_only=True).reset_index()

# conversion de l'année
df["annee"] = pandas.to_datetime(df["annee"], format="%Y")


conso_totale = df[
    [
        "annee",
        "conso_totale",
        # "conso_agriculture",
        # "conso_industrie",
        # "conso_tertiaire",
        # "conso_residentiel",
        # "conso_secteur_inconnu",
    ]
]
conso_agriculture = df[["annee", "conso_agriculture"]]
conso_industrie = df[["annee", "conso_industrie"]]
conso_tertiaire = df[["annee", "conso_tertiaire"]]
conso_residentiel = df[["annee", "conso_residentiel"]]
conso_secteur_inconnu = df[["annee", "conso_secteur_inconnu"]]


def columns_ds_y(data):
    data.columns = ["ds", "y"]


columns_ds_y(conso_totale)
columns_ds_y(conso_agriculture)
columns_ds_y(conso_industrie)
columns_ds_y(conso_tertiaire)
columns_ds_y(conso_residentiel)
columns_ds_y(conso_secteur_inconnu)

# graphique


def plot_data(df, xlabel, ylabel, title, filename):
    plt.figure(figsize=(17, 8))
    plt.plot(df["ds"], df["y"])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(False)
    plt.savefig(filename)


def plot_data_secteur(data, secteur):
    plot_data(
        data,
        annee_label,
        conso_electrique_label,
        "Consommation d'électricité (en MWh) en France, dans le secteur {}, en fonction des années".format(
            secteur
        ),
        "prevision-consommation/filieres/{}-consommation.png".format(secteur),
    )


annee_label = "Année"
conso_electrique_label = "Consommation d'électricité (en MWh)"

plot_data(
    conso_totale,
    annee_label,
    conso_electrique_label,
    "Consommation d'électricité (en MWh) en France, en fonction des années",
    "prevision-consommation/filieres/global-consommation.png",
)

plot_data_secteur(conso_agriculture, "agriculture")
plot_data_secteur(conso_industrie, "industrie")
plot_data_secteur(conso_tertiaire, "tertiaire")
plot_data_secteur(conso_residentiel, "residentiel")
plot_data_secteur(conso_secteur_inconnu, "secteur_inconnu")

### prédiction


def afficheGraphePrediction(df, forecast, title):
    plt.figure(figsize=(17, 8))
    plt.plot(forecast["ds"], forecast["yhat"], label="valeurs prédites")
    plt.plot(
        forecast["ds"], forecast["yhat_lower"], label="valeurs inférieures prédites"
    )
    plt.plot(
        forecast["ds"], forecast["yhat_upper"], label="valeurs supérieures prédites"
    )
    plt.plot(df["ds"], df["y"], label="valeurs réelles")
    plt.legend()
    plt.xlabel("Année")
    plt.ylabel("Consommation d'électricité (en MWh) en France")
    plt.title(title)
    plt.grid(False)


def predire_et_graphes(data, title, filename, title2, filename2):
    m = Prophet()
    m.fit(data)
    future = m.make_future_dataframe(periods=10, freq="Y")
    forecast = m.predict(future)
    fig = m.plot(forecast)
    plt.xlabel("Année")
    plt.ylabel("Consommation d'électricité (en MWh)")
    plt.title(title)
    plt.savefig(filename)

    # cross-validation
    # 5 ans -> 1825 jours
    df_cv = cross_validation(
        m, initial="1825 days", period="365 days", horizon="1825 days"
    )
    afficheGraphePrediction(
        df_cv,
        df_cv,
        title2,
    )
    plt.savefig(filename2)


def predire_et_graphes_secteur(data, secteur):
    predire_et_graphes(
        data,
        "Consommation d'électricité (en MWh) en France, dans le secteur {}, en fonction des années".format(
            secteur
        ),
        "prevision-consommation/filieres/{}-consommation-prevision.png".format(secteur),
        "Analyse de la cross-validation de la consommation d'électricité (en MWh) en France, dans le secteur {}, en fonction des années".format(
            secteur
        ),
        "prevision-consommation/filieres/{}-analyse-prediction.png".format(secteur),
    )


predire_et_graphes(
    conso_totale,
    "Consommation d'électricité (en MWh) en France, en fonction des années",
    "prevision-consommation/filieres/global-consommation-prevision.png",
    "Analyse de la cross-validation de la consommation d'électricité (en MWh) en France en fonction des années",
    "prevision-consommation/filieres/global-analyse-prediction.png",
)

predire_et_graphes_secteur(conso_agriculture, "agriculture")
predire_et_graphes_secteur(conso_industrie, "industrie")
predire_et_graphes_secteur(conso_tertiaire, "tertiaire")
predire_et_graphes_secteur(conso_residentiel, "residentiel")
predire_et_graphes_secteur(conso_secteur_inconnu, "secteur_inconnu")