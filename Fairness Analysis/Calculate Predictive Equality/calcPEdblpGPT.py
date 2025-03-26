import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("matchDataDBLPgpt.csv")
df.columns

"""# Precision"""

df["Precision 50%"] = 0
df["Precision 60%"] = 0
df["Precision 70%"] = 0
df["Precision 80%"] = 0
df["Precision 90%"] = 0
df["Precision 100%"] = 0

for index, row in df.iterrows():
  numCoAuthors = len(row["Co-authors’ names (GPT 3.5 Turbo)"].split("/"))
  df.at[index, "Precision 50%"] = row["Match Count 50%"] / numCoAuthors
  df.at[index, "Precision 60%"] = row["Match Count 60%"] / numCoAuthors
  df.at[index, "Precision 70%"] = row["Match Count 70%"] / numCoAuthors
  df.at[index, "Precision 80%"] = row["Match Count 80%"] / numCoAuthors
  df.at[index, "Precision 90%"] = row["Match Count 90%"] / numCoAuthors
  df.at[index, "Precision 100%"] = row["Match Count 100%"] / numCoAuthors

"""# Completeness Analysis"""

std = np.std(df["Precision 50%"].to_list())
mean = np.mean(df["Precision 50%"].to_list())
print("Mean 50% =", mean, ", std =", std)

std = np.std(df["Precision 60%"].to_list())
mean = np.mean(df["Precision 60%"].to_list())
print("Mean 60% =", mean, ", std =", std)

std = np.std(df["Precision 70%"].to_list())
mean = np.mean(df["Precision 70%"].to_list())
print("Mean 70% =", mean, ", std =", std)

std = np.std(df["Precision 80%"].to_list())
mean = np.mean(df["Precision 80%"].to_list())
print("Mean 80% =", mean, ", std =", std)

std = np.std(df["Precision 90%"].to_list())
mean = np.mean(df["Precision 90%"].to_list())
print("Mean 90% =", mean, ", std =", std)

std = np.std(df["Precision 100%"].to_list())
mean = np.mean(df["Precision 100%"].to_list())
print("Mean 100% =", mean, ", std =", std)

"""# Gender Predictive Equality"""

print("Gender Predictive Equality 50% : ")
df[df["Gender"] == "Female"]["Precision 50%"].mean() / df[df["Gender"] == "Male"]["Precision 50%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Precision 50%"].to_list(), df[df["Gender"] == "Male"]["Precision 50%"].to_list())

print("Gender Predictive Equality 60% : ")
df[df["Gender"] == "Female"]["Precision 60%"].mean() / df[df["Gender"] == "Male"]["Precision 60%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Precision 60%"].to_list(), df[df["Gender"] == "Male"]["Precision 60%"].to_list())

print("Gender Predictive Equality 70% : ")
df[df["Gender"] == "Female"]["Precision 70%"].mean() / df[df["Gender"] == "Male"]["Precision 70%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Precision 70%"].to_list(), df[df["Gender"] == "Male"]["Precision 70%"].to_list())

print("Gender Predictive Equality 80% : ")
df[df["Gender"] == "Female"]["Precision 80%"].mean() / df[df["Gender"] == "Male"]["Precision 80%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Precision 80%"].to_list(), df[df["Gender"] == "Male"]["Precision 80%"].to_list())

print("Gender Predictive Equality 90% : ")
df[df["Gender"] == "Female"]["Precision 90%"].mean() / df[df["Gender"] == "Male"]["Precision 90%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Precision 90%"].to_list(), df[df["Gender"] == "Male"]["Precision 90%"].to_list())

print("Gender Predictive Equality 100% : ")
df[df["Gender"] == "Female"]["Precision 100%"].mean() / df[df["Gender"] == "Male"]["Precision 100%"].mean()

stats.ttest_ind(df[df["Gender"] == "Female"]["Precision 100%"].to_list(), df[df["Gender"] == "Male"]["Precision 100%"].to_list())

"""# Ethnicity Predictive Equality"""

minorities = ["Black", "Hispanic"]
majorities = ["White", "Asian"]

minority_precision_mean = df[df["Ethnicity"].isin(minorities)]["Precision 50%"].mean()
majority_precision_mean = df[df["Ethnicity"].isin(majorities)]["Precision 50%"].mean()

ethnicity_predictive_equality = minority_precision_mean / majority_precision_mean
print("Ethnicity Predictive Equality 50%:", ethnicity_predictive_equality)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Precision 50%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Precision 50%"].to_list())

minority_precision_mean = df[df["Ethnicity"].isin(minorities)]["Precision 60%"].mean()
majority_precision_mean = df[df["Ethnicity"].isin(majorities)]["Precision 60%"].mean()

ethnicity_predictive_equality = minority_precision_mean / majority_precision_mean
print("Ethnicity Predictive Equality 60%:", ethnicity_predictive_equality)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Precision 60%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Precision 60%"].to_list())

minority_precision_mean = df[df["Ethnicity"].isin(minorities)]["Precision 70%"].mean()
majority_precision_mean = df[df["Ethnicity"].isin(majorities)]["Precision 70%"].mean()

ethnicity_predictive_equality = minority_precision_mean / majority_precision_mean
print("Ethnicity Predictive Equality 70%:", ethnicity_predictive_equality)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Precision 70%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Precision 70%"].to_list())

minority_precision_mean = df[df["Ethnicity"].isin(minorities)]["Precision 80%"].mean()
majority_precision_mean = df[df["Ethnicity"].isin(majorities)]["Precision 80%"].mean()

ethnicity_predictive_equality = minority_precision_mean / majority_precision_mean
print("Ethnicity Predictive Equality 80%:", ethnicity_predictive_equality)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Precision 80%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Precision 80%"].to_list())

minority_precision_mean = df[df["Ethnicity"].isin(minorities)]["Precision 90%"].mean()
majority_precision_mean = df[df["Ethnicity"].isin(majorities)]["Precision 90%"].mean()

ethnicity_predictive_equality = minority_precision_mean / majority_precision_mean
print("Ethnicity Predictive Equality 90%:", ethnicity_predictive_equality)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Precision 90%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Precision 90%"].to_list())

minority_precision_mean = df[df["Ethnicity"].isin(minorities)]["Precision 100%"].mean()
majority_precision_mean = df[df["Ethnicity"].isin(majorities)]["Precision 100%"].mean()

ethnicity_predictive_equality = minority_precision_mean / majority_precision_mean
print("Ethnicity Predictive Equality 100%:", ethnicity_predictive_equality)

stats.ttest_ind(df[df["Ethnicity"].isin(minorities)]["Precision 100%"].to_list(), df[df["Ethnicity"].isin(majorities)]["Precision 100%"].to_list())