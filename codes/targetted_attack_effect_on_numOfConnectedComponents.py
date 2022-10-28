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
num_connec_comp_bc = []
asp_bc = []
xaxis = []
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
	if(ind!='-1') and (ind in G.nodes()):
		G.remove_node(ind)
		num_connec_comp_bc.append(nx.number_connected_components(G))
		xaxis.append(i)

G.clear()

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
ffile.close()
num_connec_comp_deg = []
asp_deg = []
xaxis2 = []
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
		num_connec_comp_deg.append(nx.number_connected_components(G))
		xaxis2.append(i)
G.clear()

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
ffile.close()
num_connec_comp_cc = []
xaxis_cc = []
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
		num_connec_comp_cc.append(nx.number_connected_components(G))
		xaxis_cc.append(i)

G.clear()
				
plt.plot(xaxis,num_connec_comp_bc,'forestgreen',label = 'Betweenness Centrality')
plt.plot(xaxis2,num_connec_comp_deg,'deeppink',label = 'Degree Centrality')
plt.plot(xaxis_cc,num_connec_comp_cc,'darkviolet',label = 'Closeness Centrality')
plt.ylabel('Number of connected components')
plt.xlabel('Number of nodes removed')
plt.legend()
plt.savefig('targetted_all_ncc.svg')
plt.show()

