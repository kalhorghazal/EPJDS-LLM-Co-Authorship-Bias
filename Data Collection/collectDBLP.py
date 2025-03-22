import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import re

def get_co_authors(author_name):
    base_url = "https://dblp.org/search/author/api?q="
    query_url = f"{base_url}{author_name.replace(' ', '+')}&format=json"

    try:
        response = requests.get(query_url)
        response.raise_for_status()
        data = response.json()

        if not data.get("result") or not data["result"].get("hits"):
            print(f"No results found for author: {author_name}")
            return []

        authors = data["result"]["hits"]["hit"]
        dblp_url = authors[0]["info"]["url"]

        dblp_response = requests.get(dblp_url)
        dblp_response.raise_for_status()

        soup = BeautifulSoup(dblp_response.text, "html.parser")
        co_authors = list()

        index_div = soup.find("div", class_="index hide-body hidden")
        if not index_div:
            print("No co-author index found on the page.")
            return []

        for person_div in index_div.find_all("div", class_="person"):
            co_author_link = person_div.find("a")
            if co_author_link:
                co_authors.append(co_author_link.get_text(strip=True))

        return co_authors

    except requests.RequestException as e:
        print(f"An error occurred while accessing DBLP: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def get_dblp_url(author_name):
    base_url = "https://dblp.org/search/author/api?q="
    query_url = f"{base_url}{author_name.replace(' ', '+')}&format=json"

    try:
        response = requests.get(query_url)
        response.raise_for_status()
        data = response.json()

        if not data.get("result") or not data["result"].get("hits"):
            print(f"No results found for author: {author_name}")
            return []

        authors = data["result"]["hits"]["hit"]
        dblp_url = authors[0]["info"]["url"]
        return dblp_url

    except requests.RequestException as e:
        print(f"An error occurred while accessing DBLP: {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""

df = pd.read_csv("newSeeds.csv")
df.head()

df["Co-authors’ names (DBLP)"] = np.nan
df["DBLP URL"] = np.nan

for index, row in df.iterrows():
    if pd.notna(row["DBLP URL"]):
        continue
    print(index)
    author_name = row["Name"]
    url = get_dblp_url(author_name)
    if url:
        df.at[index, "DBLP URL"] = url
    time.sleep(5)

for index, row in df.iterrows():
    if pd.notna(row["Co-authors’ names (DBLP)"]):
        continue
    print(index)
    author_name = row["Name"]
    co_authors = get_co_authors(author_name)
    if co_authors:
        df.at[index, "Co-authors’ names (DBLP)"] = "/".join(co_authors)
    time.sleep(5)

df.to_csv("outputData.csv", index=False)