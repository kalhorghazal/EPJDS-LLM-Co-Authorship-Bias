"""# Import Libraries"""

import pandas as pd
import requests
import numpy as np
import json
import re

df = pd.read_csv("uniqueNames.csv")

len(df)

df.head()

len(df[pd.isnull(df["Name"])])

df = df[pd.isnull(df["Name"]) == False]

len(df)

"""## Set API values"""

API_KEY = 'YOUR_API_KEY'
API_URL = 'https://v2.namsor.com/NamSorAPIv2/api2/json/genderFullBatch'

"""# Detect Genders"""

def get_gender_from_namsor(full_name):
    headers = {
        'X-API-KEY': API_KEY,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    payload = {
      "personalNames": [
        {
          "name": full_name
        }
      ]
    }

    response = requests.request("POST", API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["personalNames"][0]['likelyGender']
    else:
        return None


"""## Get Authors' Genders"""

df["Gender"] = np.nan

for index, row in df.iterrows():
  if pd.isnull(row["Gender"]) == False:
    continue
  name = row["Name"]
  gender = get_gender_from_namsor(name)
  if gender:
    df.at[index, "Gender"] = gender
    print(index, "-", name, "**", gender)
  else:
    print("No gender detected!")
    break

df.head()

df.to_csv("uniqueNames.csv", index=False)