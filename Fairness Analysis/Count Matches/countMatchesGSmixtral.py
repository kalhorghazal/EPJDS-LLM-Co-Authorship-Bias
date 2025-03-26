!pip install fuzzywuzzy

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd

def extractLastNames(names):
    lastNames = []
    for name in names:
      parts = name.strip().lower().split()
      lastNames.append(parts[-1].strip())
    return lastNames

thresholds = [50, 60, 70, 80, 90, 100]

df = pd.read_csv("inputData.csv")
df.columns

df = df[df["Co-authors’ names (Google Scholar)"].notna()]
df = df[df["Co-authors’ names (Mixtral)"].notna()]

len(df)

df.head()

df["Match Count 50%"] = 0
df["Match Count 60%"] = 0
df["Match Count 70%"] = 0
df["Match Count 80%"] = 0
df["Match Count 90%"] = 0
df["Match Count 100%"] = 0

for index, row in df.iterrows():
    llmNames = row["Co-authors’ names (Mixtral)"].split('/')
    refNames = row["Co-authors’ names (Google Scholar)"].split('/')

    llmNames = extractLastNames(llmNames)
    refNames = extractLastNames(refNames)

    for threshold in thresholds:
        count = 0
        refNamesCopy = refNames.copy()

        for name in llmNames:
            if not refNamesCopy:
                break

            bestRatio = 0
            bestIndex = -1
            for i, candidate in enumerate(refNamesCopy):
                currentRatio = fuzz.ratio(name, candidate)
                if currentRatio >= threshold and currentRatio > bestRatio:
                    bestRatio = currentRatio
                    bestIndex = i

            if bestIndex != -1:
                count += 1
                del refNamesCopy[bestIndex]

        colName = "Match Count " + str(threshold) + "%"
        df.at[index, colName] = count

df = df[["Scholar ID", "Name", "Country", "Ethnicity", "Gender", "h-index", "Co-authors’ names (Google Scholar)", "Co-authors’ names (Mixtral)", "Match Count 50%", "Match Count 60%", "Match Count 70%", "Match Count 80%", "Match Count 90%", "Match Count 100%"]]
df.head()

df.to_csv("matchDataGSmixtral.csv", index = False)