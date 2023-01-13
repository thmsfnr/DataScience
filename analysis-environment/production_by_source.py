#read the document and create the dataset

import pandas as pd



df = pd.read_csv("productions-consolidees-par-filiere-en-france.csv", sep=",")

#keep only the columns annee is 2021
df = df[df['annee'] == 2021]

print(df)