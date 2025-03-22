
!pip install --upgrade openai

from openai import OpenAI
import pandas as pd
import numpy as np
import time


client = OpenAI(
    api_key=API_KEY,
)

def gpt_3_5_api(messages: list):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=4096
    )
    return completion.choices[0].message.content

df = pd.read_excel("inputData.xlsx")

df.head()

df["LLM response (GPT 3.5 Turbo)"] = np.nan

for index, row in df.iterrows():
  if pd.isnull(row["LLM response (GPT 3.5 Turbo)"]) == False:
    continue
  authorName = row["Name"]
  authorAffiliation = row["Affiliation"]
  numCoauthors = min(100, len(row["Co-authors’ names (DBLP)"].split("/")))
  query = f"Can you list the co-authors of {authorName}, who is affiliated with {authorAffiliation}? Please provide the names (first and last) of up to {numCoauthors} co-authors, separated by a forward slash ('/') with no extra whitespace."
  count += 1
  messages = [{'role': 'user','content': query},]
  df.at[index, "LLM response (GPT 3.5 Turbo)"] = gpt_3_5_api(messages)
  time.sleep(5)
  print(index, count)

df.to_excel("outputData.xlsx", index=False)