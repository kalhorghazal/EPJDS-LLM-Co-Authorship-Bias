import pandas as pd
import numpy as np
import networkx as nx

df = pd.read_csv("inputData.csv")
df.columns

df.head()

df["DBLP ID"] = np.nan

for index, row in df.iterrows():
  dblpID = row["DBLP URL"].removeprefix("https://dblp.org/pid/")
  dblpID = dblpID.removesuffix(".html")
  df.at[index, "DBLP ID"] = dblpID


src = list()
dest = list()

for index, row in df.iterrows():
  author = row["DBLP ID"]
  coauthor_list = [s.strip() for s in row["Co-authors’ IDs (DBLP)"].split("$")]

  for coauthor in coauthor_list:
    src.append(author)
    dest.append(coauthor)

edges = pd.DataFrame({'Source':src, 'Target':dest})

edges = edges.drop_duplicates()

G = nx.from_pandas_edgelist(edges, source="Source", target="Target", create_using=nx.Graph())

G.number_of_nodes()

G.number_of_edges()

nx.density(G)

node_attrs = df[["DBLP ID", "Gender", "Ethnicity"]]

names = node_attrs["DBLP ID"].to_list()
genders = node_attrs["Gender"].to_list()
ethnicities = node_attrs["Ethnicity"].to_list()

for index, row in df.iterrows():
  coauthor_list = [s.strip() for s in row["Co-authors’ IDs (DBLP)"].split("$")]
  gender_list = row["Co-authors’ genders (DBLP)"].split('/')
  ethnicity_list = row["Co-authors’ ethnicities (DBLP)"].split('/')

  names.extend(coauthor_list)
  genders.extend(gender_list)
  ethnicities.extend(ethnicity_list)


attrs = pd.DataFrame({'DBLP ID':names, 'Gender':genders, 'Ethnicity':ethnicities})

attrs = attrs.drop_duplicates(subset='DBLP ID', keep="first")

node_attr = attrs.set_index('DBLP ID').to_dict('index')
nx.set_node_attributes(G, node_attr)

nx.write_graphml(G, "dblpNet.graphml")