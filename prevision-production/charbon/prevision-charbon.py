import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import logging
logging.getLogger().setLevel(logging.ERROR)
from prophet.diagnostics import cross_validation
from prophet.plot import plot_cross_validation_metric
from prophet.diagnostics import performance_metrics
from sklearn.metrics import mean_absolute_error, confusion_matrix

##-----------------------------------------------Nettoyage des données-----------------------##
df = pd.read_csv('cleaneddata/production_electricite_charbon.csv')
# Formater les dates
#conversion TWh en MWh
df['production électricité TWh'] = df['production électricité TWh'] * 1000000
print(df.head())

df['annee'] = pd.to_datetime(df['annee'],format="%Y")
#Formater les noms des colonnes pour lancer Prophet
df.columns = ['ds', 'y']

##-----------------------------------------------Graphique-----------------------##
plt.figure(figsize=(17, 8))
plt.plot(df['ds'],df['y'])
plt.xlabel('Année')
plt.ylabel('Production d\'électricité en MWh')
plt.title('Production d\'électricité en MWh pour le charbon en fonction des années')
plt.grid(False)
plt.savefig('prevision-production/charbon/production-charbon.png')

##-----------------------------------------------prediction-----------------------##
#Creation objet prophet
m = Prophet()
#Entrainement du modèle
m.fit(df)
#prediction des 11 prochaines années par défault ça compare avec les données historiques
future = m.make_future_dataframe(periods=11, freq='Y')
forecast = m.predict(future)
fig = m.plot(forecast)
plt.xlabel('Année')
plt.ylabel("Production d'électricité en MWh")
plt.title("Prédiction de la production d'électricité en MWh pour le charbon en fonction des années")
plt.savefig('prevision-production/charbon/prediction-charbon.png')

##------------------graphe-----------------------##
def afficheGraphePrediction(df,forecast,title):
    plt.figure(figsize=(17, 8))
    plt.plot(forecast['ds'],forecast['yhat'],label='valeurs prédites')
    plt.plot(forecast['ds'],forecast['yhat_lower'],label='valeurs inférieures prédites')
    plt.plot(forecast['ds'],forecast['yhat_upper'],label='valeurs supérieures prédites')
    plt.plot(df['ds'],df['y'],label='valeurs réelles')
    plt.legend()
    plt.xlabel('Année')
    plt.ylabel("Production d'électricité en MWh")
    plt.title(title)
    plt.grid(False)

print(forecast)
afficheGraphePrediction(df,forecast,"Analyse de la prédiction de la production d'électricité en MWh pour le charbon en fonction des années")
#sauvegarde du graphe
plt.savefig('prevision-production/charbon/analyse-prevision-charbon.png')

##-----------------------------------------------Cross-validation-----------------------##

#cross validation -> entrainement sur les données et tests sur les données pour voir l'efficacité du modèle (s'il y a des erreurs de prévisions)
#initial : toutes les données ou on s'entraine 
# horizon : combien de données je veux prédire 
#period : le nombres de données à calculer à chaque itération (ici je compte par 1 donc 365 jours))
#90 % entrainement et 10 % test ( 365 * 60 ans = 7300 jours) (de 1950 à 2010) donc je veux tester sur les 10 ans restant soit 365*10= 3650 days
df_cv = cross_validation(m, initial = '21900 days', period='365 days', horizon = '3650 days')
print("CROSS VALIDATION")
print(df_cv)
afficheGraphePrediction(df_cv,df_cv,"Analyse de la cross validation de la production d'électricité en MWh pour charbon en fonction des années")
#sauvegarde du graphe
plt.savefig('prevision-production/charbon/analyse-cross-validation-charbon.png')

#pour calculer des indicateurs utiles par rapport à la prédiction
df_p = performance_metrics(df_cv)
print("INDICATEUR PERFORMANCE")
print(df_p)

####-------visualiser l'ensemble de la production par rapport au MAE-------####
'''
For example, if the range of nuclear electricity production is between 0 and 10,000 MWh,
then a MAE of 100 MWh would be considered quite good, while if the range is between 0 and 100 MWh, then a MAE of 100 MWh would be considered quite bad.
'''
print("Minimum production : "+ str(df["y"].min())) #minium de la production
print("Maximum production : " + str(df["y"].max())) #maximum de la production
print("Moyenne production : " + str(df["y"].mean())) #moyenne de la production
print("Ecart type production : " + str(df["y"].std())) #écart type de la production
print("Moyenne MAE : " + str(df_p["mae"].mean())) #moyenne de l'erreur absolue moyenne (MAE), mean absolute error (MAE)
print("MAE: ", mean_absolute_error(df_cv["y"], df_cv["yhat"])) # MAE avec une autre fonction

##----------Moyenne production prévision --------------##
moyennePrevision = forecast['yhat'].mean()
print("MOYENNE PRODUCTION BIOENERGIE PREVISION")
print(moyennePrevision)
##----------Minimum production prédite --------------##
minProductionPrevision = forecast['yhat'].min()
print("MINIMUM PRODUCTION BIOENERGIE PREVISION")
print(minProductionPrevision)
##----------Maximum production prédite --------------##
maxProductionPrevision = forecast['yhat'].max()
print("MAXIMUM PRODUCTION BIOENERGIE PREVISION")
print(maxProductionPrevision)
##----------Ecart type production prédite --------------##
ecartTypeProductionPrevision = forecast['yhat'].std()
print("ECART TYPE PRODUCTION BIOENERGIE PREVISION")
print(ecartTypeProductionPrevision)

#-----sauvegarde des données de prévision dans un fichier csv-----#
forecast.to_csv('prevision-production/charbon/prevision-charbon.csv', index=False)