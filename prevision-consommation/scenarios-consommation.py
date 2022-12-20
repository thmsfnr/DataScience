import pandas

scenarios = pandas.read_csv("cleaneddata/scenario-de-transition-energétique.csv")
scenarios = scenarios.groupby("annee").sum(numeric_only=True)

print(scenarios)

# c'est quoi l'unité ???? on a des trucs du genre 483.36, 516.86 donc je pense que c'est pas des GW
