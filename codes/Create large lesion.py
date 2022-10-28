#Create large lesion by removing node with largest degree - 29

import networkx as nx
from random import choice, sample

f = open("bn-macaque-rhesus_cerebral-cortex_1.edges", "r")
lines = f.readlines()
lines_modified = [x.split(' ') for x in lines]

f.close()

edge_list = []
for x in lines_modified:
    edge_list.append((int(x[0]), int(x[1])))
    
G = nx.Graph()
G.add_edges_from(edge_list)
#nx.draw(G)

#Store shortest path lengths for all pairs
distance_matrix = dict(nx.all_pairs_shortest_path_length(G))



#Create lesion - remove highest degree node (29)
           
lesioned_graph = nx.Graph()
lesioned_graph.add_edges_from(edge_list)

affected_nodes = set()
affected_nodes.add(29)

removed_node = 29
removed_node_neighbours = sample([x for x in nx.neighbors(G, removed_node)], 43)

for x in removed_node_neighbours:
    lesioned_graph.remove_edge(29, x)
    affected_nodes.add(x)

for x in removed_node_neighbours:
    second_layer_neighbours = list(nx.neighbors(lesioned_graph, x))
    second_layer_sample = sample(second_layer_neighbours, round(0.25*len(second_layer_neighbours)))
    
    for y in second_layer_sample:
        lesioned_graph.remove_edge(x, y)
        affected_nodes.add(y)