import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
ffile.close()	    
nnode = 64
asp_bc = []
xnew = []
for i in range(0,nnode):   
	xmax = 0
	ind = -1 
	bc = nx.betweenness_centrality(G)
	for val in bc:
		b = bc[val] 
		a = val
		if(b>xmax):
			xmax = b
			ind = a
	if(ind!='-1')and (ind in G.nodes()):
		G.remove_node(ind)
		if(nx.number_connected_components(G)==1):
			asp_bc.append(nx.average_shortest_path_length(G))
			xnew.append(i)

G.clear()

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
ffile.close()
asp_deg = []
xnew2 = []
for i in range(0,nnode):   
	xmax = 0
	ind = -1 
	degree = nx.degree_centrality(G)
	for val in degree:
		b = degree[val]
		a = val 
		if(b>xmax):
			xmax = b
			ind = a
	if(ind!='-1')and (ind in G.nodes()):
		G.remove_node(ind)
		if(nx.number_connected_components(G)==1):
			asp_deg.append(nx.average_shortest_path_length(G))
			xnew2.append(i)
G.clear()

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
ffile.close()
asp_cc = []
xnew_cc = []
for i in range(0,nnode):   
	xmax = 0
	ind = -1 
	cc = nx.closeness_centrality(G)
	for val in cc:
		b = cc[val]
		a = val 
		if(b>xmax):
			xmax = b
			ind = a
	if(ind!='-1')and (ind in G.nodes()):
		G.remove_node(ind)
		if(nx.number_connected_components(G)==1):
			asp_cc.append(nx.average_shortest_path_length(G))
			xnew_cc.append(i)

G.clear()
				
plt.plot(xnew,asp_bc,'forestgreen',label = 'Betweenness Centrality')
plt.plot(xnew2,asp_deg,'deeppink',label = 'Degree Centrality')
plt.plot(xnew_cc,asp_cc,'darkviolet',label = 'Closeness Centrality')
plt.ylabel('Average Shortest Path length')
plt.xlabel('Number of nodes removed')
plt.legend()
plt.savefig('targetted_all_asp.svg')
plt.show()

