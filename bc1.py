import networkx as nx
import random
import math
from matplotlib import pyplot as plt
import numpy as np

#1Create a fully connected graph
nNodes = 100

G = nx.complete_graph(nNodes, create_using=None)

pos = nx.spring_layout(G)

#nx.draw_networkx(G,pos,node_size=10,alpha=0.5,with_labels=False)

#2# Assign a random opinion at each agent and plot time=0
opinion =[random.uniform (0,1) for r in range(nNodes)]
x =np.ones((nNodes), dtype=int)

#print opinion at time zero
plt.scatter(x,opinion)
plt.show()
