import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
    
clus_coeff = nx.clustering(G)

xmax = 0
xmin = 100
for val in clus_coeff:
	b = clus_coeff[val]
	if(b>xmax):
		xmax = b
	if(b<xmin):
		xmin = b

print(xmax,xmin)
binw = 0.05
maxbins = int((xmax-xmin)/binw)+ 1

i=0
xhist = []
while (i<maxbins):
	xhist.append(xmin + (2*i+1)*binw/2)
	i+=1
	
hist = [0]*maxbins
count = 0
for val in clus_coeff:
	b = clus_coeff[val]
	binIndex = int((b-xmin)/binw)
	hist[binIndex]+=1
	count+=1

hist[:]= [val/count for val in hist]   
plt.plot(xhist,hist,'r')
plt.xlabel('Clustering coefficient')
plt.ylabel('Fraction')
plt.savefig('clus_hist.svg')
plt.show()
