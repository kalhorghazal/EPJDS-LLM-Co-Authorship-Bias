!pip install groq

from groq import Groq
import pandas as pd
import numpy as np
import time

client = Groq(api_key=API_KEY)

def mixtral_api(messages: list):
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=messages,
        max_tokens=4096,
        stream=True
    )

    result = ""
    for chunk in completion:
        result += chunk.choices[0].delta.content or ""

    return result

df = pd.read_excel("prompts.xlsx")

df.head()

df["LLM response (Mixtral)"] = np.nan

for index, row in df.iterrows():
  if pd.isnull(row["LLM response (Mixtral)"]) == False:
    continue
  authorName = row["Name"]
  authorAffiliation = row["Affiliation"]
  numCoauthors = min(100, len(row["Co-authors’ names (DBLP)"].split("/")))
  query = f"Can you list the co-authors of {authorName}, who is affiliated with {authorAffiliation}? Please provide the names (first and last) of up to {numCoauthors} co-authors, separated by a forward slash ('/') with no extra whitespace."
  count += 1
  messages = [{'role': 'user','content': query},]
  df.at[index, "LLM response (Mixtral)"] = mixtral_api(messages)
  time.sleep(5)
  print(index)

df.to_excel("outputData.xlsx", index=False)