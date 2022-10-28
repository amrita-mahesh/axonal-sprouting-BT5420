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

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
ffile.close()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()    

L = nx.average_shortest_path_length(G)
C = nx.average_clustering(G)

avg_deg = 0
for val in G.degree():
	(a,b) = val
	avg_deg+= b
	
avg_deg = math.floor(avg_deg/num_nodes)
print(avg_deg)
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
print(Lr, L, C, C_L, omega)
