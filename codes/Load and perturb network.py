import networkx as nx
from random import choice

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

#Random node removal

random_node_removed = nx.Graph()
random_node_removed.add_edges_from(edge_list)

percent_removed = 50

for i in range(round(percent_removed*len(G.nodes)/100)):
    random_node = choice(list(random_node_removed.nodes))
    random_node_removed.remove_node(random_node)
    
#nx.draw(random_node_removed)


#Highest degree node removal

degree_values = dict(nx.degree(G))
sorted_degrees_values = sorted(degree_values.values(), reverse=True)
sorted_degrees_nodes = []

for val in sorted_degrees_values:
    for key in degree_values:
        if degree_values[key] == val and key not in sorted_degrees_nodes:
            sorted_degrees_nodes.append(key)
            
highest_degree_node_removed = nx.Graph()
highest_degree_node_removed.add_edges_from(edge_list)

percent_removed_degree = 25
for i in range(round(percent_removed_degree*len(G.nodes)/100)):
    removed_node = sorted_degrees_nodes[i]
    highest_degree_node_removed.remove_node(removed_node)
    
nx.draw_spring(highest_degree_node_removed)


#Highest betweenness centrality node removal

centrality_values = dict(nx.betweenness_centrality(G))
sorted_centrality_values = sorted(centrality_values.values(), reverse=True)
sorted_centrality_nodes = []

for val in sorted_centrality_values:
    for key in centrality_values:
        if centrality_values[key] == val and key not in sorted_centrality_nodes:
            sorted_centrality_nodes.append(key)
            
highest_centrality_node_removed = nx.Graph()
highest_centrality_node_removed.add_edges_from(edge_list)

percent_removed_centrality = 30
for i in range(round(percent_removed_centrality*len(G.nodes)/100)):
    removed_node = sorted_centrality_nodes[i]
    highest_centrality_node_removed.remove_node(removed_node)
    
#nx.draw_kamada_kawai(highest_centrality_node_removed)




            

    


    