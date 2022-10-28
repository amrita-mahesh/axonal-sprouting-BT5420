#Create small lesion by removing node with median degree - 24

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
affected_nodes.add(24)

removed_node = 24
removed_node_neighbours = sample([x for x in nx.neighbors(G, removed_node)], 10)

for x in removed_node_neighbours:
    lesioned_graph.remove_edge(24, x)
    affected_nodes.add(x)

for x in removed_node_neighbours:
    second_layer_neighbours = list(nx.neighbors(lesioned_graph, x))
    second_layer_sample = sample(second_layer_neighbours, round(0.25*len(second_layer_neighbours)))
    
    for y in second_layer_sample:
        lesioned_graph.remove_edge(x, y)
        affected_nodes.add(y)
        
        
#Unbounded axonal sprouting - no bounds, more extensive

reconnected_nodes = sample(list(G.nodes), round(len(list(G.nodes))))

for node in reconnected_nodes:
    reconnected = False
    
    while not reconnected:
        random_node = choice(list(G.nodes))
        if not lesioned_graph.has_edge(random_node, node):
            lesioned_graph.add_edge(node, random_node)
            reconnected = True
            

import numpy as np
import networkx as nx
import math, random

def erdos_renyi(V,E):
	adj_mat = np.zeros((V,V))
	p = E/(V*(V-1)/2)
	i = 0
	while i<V:
		j = i+1
		while j<V:
		    x = random.random()
		    adj_graph = nx.from_numpy_matrix(adj_mat)
		    E1 = adj_graph.number_of_edges()
		    if(x<p) & (E-E1>0):
		        adj_mat[i][j] = 1
		        adj_mat[j][i] = 1
		    j = j+1
		i = i+1
	return adj_mat
	
def reglattice(N,k):
	adj_mat1 = np.zeros((N,N))
	for i1 in range(0,N):
		j1 = -k
		while (i1+j1<0) & (j1<=k):
		    adj_mat1[i1][i1+j1+N]=1
		    adj_mat1[i1+j1+N][i1]=1
		    j1 = j1+1
		while (j1<=k) & (i1+j1<N):
		    adj_mat1[i1][i1+j1]=1
		    adj_mat1[i1+j1][i1]=1
		    j1 = j1+1
		while (j1<=k) & (i1+j1>=N):
		    adj_mat1[i1][i1+j1-N]=1
		    adj_mat1[i1+j1-N][i1]=1
		    j1 = j1+1
	for i1 in range(0,N):
		adj_mat1[i1][i1]=0
	return adj_mat1

num_nodes = lesioned_graph.number_of_nodes()
num_edges = lesioned_graph.number_of_edges()    

L = nx.average_shortest_path_length(lesioned_graph)
C = nx.average_clustering(lesioned_graph)

avg_deg = 0
for val in lesioned_graph.degree():
	(a,b) = val
	avg_deg+= b
	
avg_deg = math.floor(avg_deg/num_nodes)
reglat_adjmat = reglattice(num_nodes,avg_deg)
reglat_graph = nx.from_numpy_matrix(reglat_adjmat)
C_L = nx.average_clustering(reglat_graph)

i = 1
grand_avg_sp = 0
while i<=10:
    er_adjmat = erdos_renyi(num_nodes,num_edges)
    er_graph = nx.from_numpy_matrix(er_adjmat)
    grand_avg_sp += nx.average_shortest_path_length(er_graph)
    i = i+1

Lr = grand_avg_sp/10;
omega = (Lr/L) - (C/C_L)



print('Nodes:', len(lesioned_graph.nodes), 'Edges:', len(lesioned_graph.edges))
print('Characteristic path length:', nx.average_shortest_path_length(lesioned_graph))
print('Average degree:', avg_deg)
print('Omega:', omega)