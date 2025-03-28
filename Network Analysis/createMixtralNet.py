import pandas as pd
import numpy as np
import networkx as nx

df = pd.read_csv("inputData.csv")
df.columns

seeds = df["Name"].to_list()

src = list()
dest = list()

for index, row in df.iterrows():
  if pd.isnull(row["Co-authors’ names (Mixtral)"]):
    continue
  author = row["Name"]
  coauthor_list = row["Co-authors’ names (Mixtral)"].split("/")

  for coauthor in coauthor_list:
    src.append(author)
    dest.append(coauthor)

edges = pd.DataFrame({'Source':src, 'Target':dest})

edges = edges.drop_duplicates()

G = nx.from_pandas_edgelist(edges, source="Source", target="Target", create_using=nx.Graph())

G.number_of_nodes()

allAuthors = set(df["Name"])
authorsWithCoauthors = set(src + dest)

isolatedAuthors = allAuthors - authorsWithCoauthors

G.add_nodes_from(isolatedAuthors)

G.number_of_nodes()

G.number_of_edges()

nx.density(G)

node_attrs = df[["Name", "Gender", "Ethnicity"]]

names = node_attrs["Name"].to_list()
genders = node_attrs["Gender"].to_list()
ethnicities = node_attrs["Ethnicity"].to_list()

for index, row in df.iterrows():
  if pd.isnull(row["Co-authors’ names (Mixtral)"]):
    continue
  coauthor_list = row["Co-authors’ names (Mixtral)"].split('/')
  gender_list = row["Co-authors’ genders (Mixtral)"].split('/')
  ethnicity_list = row["Co-authors’ ethnicities (Mixtral)"].split('/')

  names.extend(coauthor_list)
  genders.extend(gender_list)
  ethnicities.extend(ethnicity_list)

attrs = pd.DataFrame({'Name':names, 'Gender':genders, 'Ethnicity':ethnicities})

attrs = attrs.drop_duplicates(subset='Name', keep="first")

node_attr = attrs.set_index('Name').to_dict('index')
nx.set_node_attributes(G, node_attr)

nx.write_graphml(G, "mixtralNet.graphml")