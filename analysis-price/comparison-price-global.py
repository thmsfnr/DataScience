
import pandas as pd
import matplotlib.pyplot as plt

# Open file with pandas
withoutNuclear = pd.read_csv("conclusion-without-nuclear.csv")
withNuclear = pd.read_csv("conclusion.csv")

# Analyse the dataset
print(withoutNuclear)
print(withNuclear)

# Calculate the electricity price
priceNuclear = 0
priceNotNuclear = 0
for i in range(0, len(withNuclear)):
    priceNuclear += withNuclear["prix_MWh"][i] * ((withNuclear["part_de_production"][i])/100)
for i in range(0, len(withoutNuclear)):
    priceNotNuclear += withoutNuclear["prix_MWh"][i] * ((withoutNuclear["part_de_production"][i])/100)
print("Price with nuclear : " + str(priceNuclear))
print("Price without nuclear : " + str(priceNotNuclear))

# Display on a graph the difference between part of production
plt.scatter(withoutNuclear["filiere"], withoutNuclear["part_de_production"], cmap="blue")
plt.scatter(withNuclear["filiere"], withNuclear["part_de_production"], cmap="red")
plt.title("Part of production difference between electricity production fields with and without nuclear")
plt.ylabel("share of production (%)")
plt.xlabel("fields of electricity production")
plt.legend(["Without nuclear", "With nuclear"])
plt.show()
