import pandas as pd
import numpy as np
import networkx as nx
import community.community_louvain as community
from random import choice

"""# DBLP Network"""

dblpNet = nx.read_graphml("dblpNet.graphml")

dblpNet.number_of_nodes()

dblpNet.number_of_edges()

nx.density(dblpNet)

partition = community.best_partition(dblpNet)

from collections import defaultdict
communities = defaultdict(set)
for node, community_id in partition.items():
    communities[community_id].add(node)

community_list = list(communities.values())

modularity_score = nx.algorithms.community.modularity(dblpNet, community_list)

print(f"Modularity Score: {modularity_score}")

max_lcc = max(nx.connected_components(dblpNet), key=len)
max_wcc = dblpNet.subgraph(max_lcc)

clustering_coefficient = nx.average_clustering(max_wcc)
print("Clustering Coefficient:", clustering_coefficient)

total = 0
for i in range(10000):
  a = choice(list(max_wcc.nodes()))
  b = choice(list(max_wcc.nodes()))
  dist = nx.shortest_path_length(max_wcc, source=a, target=b, method='dijkstra')
  total += dist
average_shortest_path_length = total / 10000
print("Average Shortest Path Length:", average_shortest_path_length)

"""# Google Scholar Network"""

scholarNet = nx.read_graphml("scholarNet.graphml")

scholarNet.number_of_nodes()

scholarNet.number_of_edges()

nx.density(scholarNet)

partition = community.best_partition(scholarNet)

from collections import defaultdict
communities = defaultdict(set)
for node, community_id in partition.items():
    communities[community_id].add(node)

community_list = list(communities.values())

modularity_score = nx.algorithms.community.modularity(scholarNet, community_list)

print(f"Modularity Score: {modularity_score}")

max_lcc = max(nx.connected_components(scholarNet), key=len)
max_wcc = scholarNet.subgraph(max_lcc)

clustering_coefficient = nx.average_clustering(max_wcc)
print("Clustering Coefficient:", clustering_coefficient)

total = 0
for i in range(10000):
  a = choice(list(max_wcc.nodes()))
  b = choice(list(max_wcc.nodes()))
  dist = nx.shortest_path_length(max_wcc, source=a, target=b, method='dijkstra')
  total += dist
average_shortest_path_length = total / 10000
print("Average Shortest Path Length:", average_shortest_path_length)

"""# GPT-3.5 Network"""

gptNet = nx.read_graphml("gptNet.graphml")

gptNet.number_of_nodes()

gptNet.number_of_edges()

nx.density(gptNet)

partition = community.best_partition(gptNet)

from collections import defaultdict
communities = defaultdict(set)
for node, community_id in partition.items():
    communities[community_id].add(node)

community_list = list(communities.values())

modularity_score = nx.algorithms.community.modularity(gptNet, community_list)

print(f"Modularity Score: {modularity_score}")

max_lcc = max(nx.connected_components(gptNet), key=len)
max_wcc = gptNet.subgraph(max_lcc)

clustering_coefficient = nx.average_clustering(max_wcc)
print("Clustering Coefficient:", clustering_coefficient)

total = 0
for i in range(10000):
  a = choice(list(max_wcc.nodes()))
  b = choice(list(max_wcc.nodes()))
  dist = nx.shortest_path_length(max_wcc, source=a, target=b, method='dijkstra')
  total += dist
average_shortest_path_length = total / 10000
print("Average Shortest Path Length:", average_shortest_path_length)

"""# Mixtral Network"""

mixtralNet = nx.read_graphml("mixtralNet.graphml")

mixtralNet.number_of_nodes()

mixtralNet.number_of_edges()

nx.density(mixtralNet)

partition = community.best_partition(mixtralNet)

from collections import defaultdict
communities = defaultdict(set)
for node, community_id in partition.items():
    communities[community_id].add(node)

community_list = list(communities.values())

modularity_score = nx.algorithms.community.modularity(mixtralNet, community_list)

print(f"Modularity Score: {modularity_score}")

max_lcc = max(nx.connected_components(mixtralNet), key=len)
max_wcc = mixtralNet.subgraph(max_lcc)

clustering_coefficient = nx.average_clustering(max_wcc)
print("Clustering Coefficient:", clustering_coefficient)

total = 0
for i in range(10000):
  a = choice(list(max_wcc.nodes()))
  b = choice(list(max_wcc.nodes()))
  dist = nx.shortest_path_length(max_wcc, source=a, target=b, method='dijkstra')
  total += dist
average_shortest_path_length = total / 10000
print("Average Shortest Path Length:", average_shortest_path_length)