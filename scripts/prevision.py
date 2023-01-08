import matplotlib.pyplot as plt


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
    plt.ylabel("Production d'électricité en MWh pour le nucléaire")
    plt.title(title)
    plt.grid(False)
    plt.show()
