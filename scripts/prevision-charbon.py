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

'''
Choix de prophet :
Utile pour faire des prédictions sur les séries temporelles. C'est un modèle additif qui permet de faire des prédictions sur des données saisonnières et tendancielles.
Il décompose une série temporelle comme cela : y(t) = g(t) + s(t) + h(t) + e(t)
g(t) : tendance
s(t) : saisonnalité
h(t) : effet de vacances
e(t) : erreur

Grande capacité à l'interprétation des données. Utile ici car la production du nucléaire est très saisonnière et tendancielle.

'''


##-----------------------------------------------Nettoyage des données-----------------------##
df = pd.read_csv('../cleaneddata/production_electricite_charbon.csv')
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
plt.ylabel('Production d\'électricité en MWh pour le charbon')
plt.title('Production d\'électricité en MWh pour le charbon en fonction des années')
plt.grid(False)
plt.show()

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
plt.ylabel('Production d\'électricité en MWh pour le charbon')
plt.title('Prédiction de la production d\'électricité en MWh pour le charbon en fonction des années')
plt.show()

##----------tendance-----------------------##


m.plot_components(forecast)
plt.xlabel('Année')
plt.ylabel('Production d\'électricité en MWh pour le charbon')
plt.show()
# trend = tendance
# yearly = saisonnalité hebdomadaire


##------------------graphe-----------------------##
def afficheGraphePrediction(df,forecast,title):
    plt.figure(figsize=(17, 8))
    plt.plot(forecast['ds'],forecast['yhat'],label='valeurs prédites')
    plt.plot(forecast['ds'],forecast['yhat_lower'],label='valeurs inférieures prédites')
    plt.plot(forecast['ds'],forecast['yhat_upper'],label='valeurs supérieures prédites')
    plt.plot(df['ds'],df['y'],label='valeurs réelles')
    plt.legend()
    plt.xlabel('Année')
    plt.ylabel('Production d\'électricité en MWh pour le charbon')
    plt.title(title)
    plt.grid(False)
    plt.show()

print(forecast)
afficheGraphePrediction(df,forecast,'Analyse de la prédiction de la production d\'électricité en MWh pour le charbon en fonction des années')



##-----------------------------------------------Cross-validation-----------------------##

#cross validation -> entrainement sur les données et tests sur les données pour voir l'efficacité du modèle (s'il y a des erreurs de prévisions)
#initial : toutes les données ou on s'entraine 
# horizon : combien de données je veux prédire 
#period : le nombres de données à calculer à chaque itération (ici je compte par 1 donc 365 jours))
#90 % entrainement et 10 % test ( 365 * 60 ans = 7300 jours) (de 1950 à 2010) donc je veux tester sur les 10 ans restant soit 365*10= 3650 days
df_cv = cross_validation(m, initial = '21900 days', period='365 days', horizon = '3650 days')
print("CROSS VALIDATION")
print(df_cv)
afficheGraphePrediction(df_cv,df_cv,'Analyse de la cross validation de la production d\'électricité en MWh pour charbon en fonction des années')

#pour calculer des indicateurs utiles par rapport à la prédiction
df_p = performance_metrics(df_cv)
print("INDICATEUR PERFORMANCE")
print(df_p)
# l'erreur quadratique moyenne (MSE) mean squared error (MSE)
#  l'erreur quadratique moyenne (RMSE), (root mean squared error (RMSE))
#  l'erreur absolue moyenne (MAE), mean absolute error (MAE)
# l'erreur absolue moyenne en pourcentage (MAPE), mean absolute percent error (MAPE)
# l'erreur absolue médiane en pourcentage (MDAPE) ,median absolute percent error (MDAPE) 
# la couverture des estimations yhat_lower et yhat_upper.
#  Ils sont calculés sur une fenêtre glissante des prédictions dans df_cv après un tri par horizon (ds moins cutoff).
#  Par défaut, 10% des prédictions seront incluses dans chaque fenêtre, mais cela peut être modifié avec l'argument rolling_window.


'''
RMSE : 
Un avantage de l'utilisation de la RMSE est que la mesure qu'elle produit est à la même échelle que l'unité prédite. 
Par exemple, le calcul de l'EQM pour un modèle de prédiction du prix des maisons donne l'erreur en termes de prix des maisons, 

 Le RMSE peut être relié à la variance du modèle
'''

#pour calculer des indicateurs utiles par rapport au cross validation
#Les points montrent le pourcentage d'erreur absolue pour chaque prédiction dans df_cv.

fig = plot_cross_validation_metric(df_cv, metric='mape')
plt.show()
plot_cross_validation_metric(df_cv, metric='rmse')
plt.show()

mean_squared_error =(df_cv["y"], df_cv["yhat"])
print("MEAN SQUARED ERROR")
print(mean_squared_error)