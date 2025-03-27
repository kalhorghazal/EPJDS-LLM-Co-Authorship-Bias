import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("matchDataDBLPmixtral.csv")
df.columns

"""# Recall"""

df["Recall 50%"] = 0
df["Recall 60%"] = 0
df["Recall 70%"] = 0
df["Recall 80%"] = 0
df["Recall 90%"] = 0
df["Recall 100%"] = 0

for index, row in df.iterrows():
  numCoAuthors = len(row["Co-authors’ names (DBLP)"].split("/"))
  df.at[index, "Recall 50%"] = row["Match Count 50%"] / numCoAuthors
  df.at[index, "Recall 60%"] = row["Match Count 60%"] / numCoAuthors
  df.at[index, "Recall 70%"] = row["Match Count 70%"] / numCoAuthors
  df.at[index, "Recall 80%"] = row["Match Count 80%"] / numCoAuthors
  df.at[index, "Recall 90%"] = row["Match Count 90%"] / numCoAuthors
  df.at[index, "Recall 100%"] = row["Match Count 100%"] / numCoAuthors

"""# Completeness Analysis"""

std = np.std(df["Recall 50%"].to_list())
mean = np.mean(df["Recall 50%"].to_list())
print("Mean 50% =", mean, ", std =", std)

std = np.std(df["Recall 60%"].to_list())
mean = np.mean(df["Recall 60%"].to_list())
print("Mean 60% =", mean, ", std =", std)

std = np.std(df["Recall 70%"].to_list())
mean = np.mean(df["Recall 70%"].to_list())
print("Mean 70% =", mean, ", std =", std)

std = np.std(df["Recall 80%"].to_list())
mean = np.mean(df["Recall 80%"].to_list())
print("Mean 80% =", mean, ", std =", std)

std = np.std(df["Recall 90%"].to_list())
mean = np.mean(df["Recall 90%"].to_list())
print("Mean 90% =", mean, ", std =", std)

std = np.std(df["Recall 100%"].to_list())
mean = np.mean(df["Recall 100%"].to_list())
print("Mean 100% =", mean, ", std =", std)

"""# Gender Demographic Parity"""

print("Gender Demographic Parity 50% : ")
df[df["Gender"] == "Female"]["Recall 50%"].mean() / df[df["Gender"] == "Male"]["Recall 50%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Recall 50%"].to_list(), df[df["Gender"] == "Male"]["Recall 50%"].to_list())

print("Gender Demographic Parity 60% : ")
df[df["Gender"] == "Female"]["Recall 60%"].mean() / df[df["Gender"] == "Male"]["Recall 60%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Recall 60%"].to_list(), df[df["Gender"] == "Male"]["Recall 60%"].to_list())

print("Gender Demographic Parity 70% : ")
df[df["Gender"] == "Female"]["Recall 70%"].mean() / df[df["Gender"] == "Male"]["Recall 70%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Recall 70%"].to_list(), df[df["Gender"] == "Male"]["Recall 70%"].to_list())

print("Gender Demographic Parity 80% : ")
df[df["Gender"] == "Female"]["Recall 80%"].mean() / df[df["Gender"] == "Male"]["Recall 80%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Recall 80%"].to_list(), df[df["Gender"] == "Male"]["Recall 80%"].to_list())

print("Gender Demographic Parity 90% : ")
df[df["Gender"] == "Female"]["Recall 90%"].mean() / df[df["Gender"] == "Male"]["Recall 90%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Recall 90%"].to_list(), df[df["Gender"] == "Male"]["Recall 90%"].to_list())

print("Gender Demographic Parity 100% : ")
df[df["Gender"] == "Female"]["Recall 100%"].mean() / df[df["Gender"] == "Male"]["Recall 100%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Recall 100%"].to_list(), df[df["Gender"] == "Male"]["Recall 100%"].to_list())

"""# Ethnicity Demographic Parity"""

minorities = ["Black", "Hispanic"]
majorities = ["White", "Asian"]

minority_recall_mean = df[df["Ethnicity"].isin(minorities)]["Recall 50%"].mean()
majority_recall_mean = df[df["Ethnicity"].isin(majorities)]["Recall 50%"].mean()

ethnicity_demographic_parity = minority_recall_mean / majority_recall_mean
print("Ethnicity Demographic Parity 50%:", ethnicity_demographic_parity)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Recall 50%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Recall 50%"].to_list())

minority_recall_mean = df[df["Ethnicity"].isin(minorities)]["Recall 60%"].mean()
majority_recall_mean = df[df["Ethnicity"].isin(majorities)]["Recall 60%"].mean()

ethnicity_demographic_parity = minority_recall_mean / majority_recall_mean
print("Ethnicity Demographic Parity 60%:", ethnicity_demographic_parity)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Recall 60%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Recall 60%"].to_list())

minority_recall_mean = df[df["Ethnicity"].isin(minorities)]["Recall 70%"].mean()
majority_recall_mean = df[df["Ethnicity"].isin(majorities)]["Recall 70%"].mean()

ethnicity_demographic_parity = minority_recall_mean / majority_recall_mean
print("Ethnicity Demographic Parity 70%:", ethnicity_demographic_parity)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Recall 70%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Recall 70%"].to_list())

minority_recall_mean = df[df["Ethnicity"].isin(minorities)]["Recall 80%"].mean()
majority_recall_mean = df[df["Ethnicity"].isin(majorities)]["Recall 80%"].mean()

ethnicity_demographic_parity = minority_recall_mean / majority_recall_mean
print("Ethnicity Demographic Parity 80%:", ethnicity_demographic_parity)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Recall 80%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Recall 80%"].to_list())

minority_recall_mean = df[df["Ethnicity"].isin(minorities)]["Recall 90%"].mean()
majority_recall_mean = df[df["Ethnicity"].isin(majorities)]["Recall 90%"].mean()

ethnicity_demographic_parity = minority_recall_mean / majority_recall_mean
print("Ethnicity Demographic Parity 90%:", ethnicity_demographic_parity)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Recall 90%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Recall 90%"].to_list())

minority_recall_mean = df[df["Ethnicity"].isin(minorities)]["Recall 100%"].mean()
majority_recall_mean = df[df["Ethnicity"].isin(majorities)]["Recall 100%"].mean()

ethnicity_demographic_parity = minority_recall_mean / majority_recall_mean
print("Ethnicity Demographic Parity 100%:", ethnicity_demographic_parity)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Recall 100%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Recall 100%"].to_list())