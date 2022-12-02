import pandas

bilanprevisionnel = pandas.read_csv(
    "rawdata/bilan-previsionnel-electrique-2021-offre-de-production.csv", sep=";"
)


total = bilanprevisionnel.sum(axis=1)
bilanprevisionnel["total"] = total

bilanprevisionnel.to_csv(
    "cleaneddata/bilan-previsionel-electrique-2021-offre-de-production.csv", index=False
)
