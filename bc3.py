import networkx as nx
import random
import math
from matplotlib import pyplot as plt
import numpy as np

##############1Create a fully connected graph
nNodes = 100
NITER = 1000
epsilon = 0.5

G = nx.complete_graph(nNodes, create_using=None)

pos = nx.spring_layout(G)

#nx.draw_networkx(G,pos,node_size=10,alpha=0.5,with_labels=False)

##############2# Assign a random opinion at each agent and plot time=0
opinion =[random.uniform (0,1) for r in range(nNodes)]
#x =np.ones((nNodes), dtype=int)

#print opinion at time zero
#plt.scatter(x,opinion)
#plt.show()

##################3 plot next times. 

#print G.nodes()

#print random.choice (list(G.nodes()))

for i in range(NITER):
       n1=random.choice (list(G.nodes()))               # Select the first agent n1    
#       print n1
       n2=random.choice (list(G.neighbors(n1)))     # Select the second agent n2 in the neighbourhood of n1
#       print n2
#       Opinion dynamics between n1 and n2
       if np.fabs(opinion[n1] - opinion [n2] )<epsilon :
          print " conversation" 
#Update opinions
          av=0.5*(opinion[n1] + opinion [n2] )
          opinion [n1] =av
          opinion [n2] =av
          x =np.ones((nNodes), dtype=int)
          plt.scatter(i*x,opinion)

plt.show()


