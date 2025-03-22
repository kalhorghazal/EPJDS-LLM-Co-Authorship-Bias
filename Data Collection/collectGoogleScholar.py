!pip install scholarly

import pandas as pd
import numpy as np
from scholarly import scholarly

author = scholarly.search_author_id("B-otGqYAAAAJ")
scholarly.fill(author, sections=["coauthors"])
co_authors = [coauthor['name'] for coauthor in author.get('coauthors', [])]
co_authors_ids = [coauthor['scholar_id'] for coauthor in author.get('coauthors', [])]
print(" $ ".join(co_authors_ids))
print("/".join(co_authors))

df = pd.read_csv('newSeeds.csv')
df.head()

del df["Citation Count"]

df["h-index"] = np.nan
df["Citation count"] = np.nan
df["Co-authors’ IDs (Google Scholar)"] = np.nan
df["Co-authors’ names (Google Scholar)"] = np.nan

for index, row in df.iterrows():
  name = row["Name"]
  try:
    author = scholarly.search_author_id(row["Scholar ID"])
    scholarly.fill(author, sections=["basics", "indices", "coauthors"])
    df.at[index, "h-index"] = author.get('hindex', 'N/A')
    df.at[index, "Citation count"] = author.get('citedby', 'N/A')

    co_authors = [coauthor['name'] for coauthor in author.get('coauthors', [])]
    co_authors_ids = [coauthor['scholar_id'] for coauthor in author.get('coauthors', [])]
    df.at[index, "Co-authors’ names (Google Scholar)"] = " $ ".join(co_authors)
    df.at[index, "Co-authors’ IDs (Google Scholar)"] = " $ ".join(co_authors_ids)
    print(index)
  except Exception as e:
    print(f"Failed to fetch data for Author: {name}. Error: {e}")

df.head()

df.to_csv('newSeeds.csv', index=False)