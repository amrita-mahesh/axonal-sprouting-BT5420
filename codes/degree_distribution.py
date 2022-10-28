import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

ffile=open("bn-cat-mixed-species_brain_1.edges",'r')
G = nx.Graph()
for line in ffile:
    a = line.split()
    G.add_edge(a[0],a[1])
    
degree = nx.degree(G)
xmax = 0
xmin = 100
for val in degree:
	(a,b) = val 
	if(b>xmax):
		xmax = b
	if(b<xmin):
		xmin = b

print(xmax,xmin)
binw = 5
maxbins = int((xmax-xmin)/binw)+ 1

i=0
xhist = []
while (i<maxbins):
	xhist.append(xmin + (2*i+1)*binw/2)
	i+=1
	
hist = [0]*maxbins
count = 0
for val in degree:
	(a,b) = val
	binIndex = int((b-xmin)/binw)
	hist[binIndex]+=1
	count+=1

hist[:]= [val/count for val in hist]   
degree_dist = nx.degree_histogram(G)
xaxis = range(len(degree_dist))

plt.plot(xhist,hist,'b')
plt.xlabel('Degree')
plt.ylabel('Fraction')
plt.savefig('degree_hist.svg')
plt.show()
