import pandas as pd
import numpy as np
import networkx as nx

df = pd.read_csv("inputData.csv")
df.columns

df.head()

seeds = df["Scholar ID"].to_list()

src = list()
dest = list()

for index, row in df.iterrows():
  if pd.isnull(row["Co-authors’ IDs (Google Scholar)"]):
    continue
  author = row["Scholar ID"]
  coauthor_list = [s.strip() for s in row["Co-authors’ IDs (Google Scholar)"].split("$")]

  for coauthor in coauthor_list:
    src.append(author)
    dest.append(coauthor)

edges = pd.DataFrame({'Source':src, 'Target':dest})

edges = edges.drop_duplicates()

len(edges)

G = nx.from_pandas_edgelist(edges, source="Source", target="Target", create_using=nx.Graph())

G.number_of_nodes()

allAuthors = set(df["Scholar ID"])
authorsWithCoauthors = set(src + dest)

isolatedAuthors = allAuthors - authorsWithCoauthors

G.add_nodes_from(isolatedAuthors)

G.number_of_nodes()

G.number_of_edges()

nx.density(G)

node_attrs = df[["Scholar ID", "Gender", "Ethnicity"]]

names = node_attrs["Scholar ID"].to_list()
genders = node_attrs["Gender"].to_list()
ethnicities = node_attrs["Ethnicity"].to_list()

for index, row in df.iterrows():
  if pd.isnull(row["Co-authors’ IDs (Google Scholar)"]):
    continue
  coauthor_list = [s.strip() for s in row["Co-authors’ IDs (Google Scholar)"].split("$")]
  gender_list = row["Co-authors’ genders (Google Scholar)"].split('/')
  ethnicity_list = row["Co-authors’ ethnicities (Google Scholar)"].split('/')

  names.extend(coauthor_list)
  genders.extend(gender_list)
  ethnicities.extend(ethnicity_list)

attrs = pd.DataFrame({'Scholar ID':names, 'Gender':genders, 'Ethnicity':ethnicities})

attrs = attrs.drop_duplicates(subset='Scholar ID', keep="first")

node_attr = attrs.set_index('Scholar ID').to_dict('index')
nx.set_node_attributes(G, node_attr)

nx.write_graphml(G, "scholarNet.graphml")