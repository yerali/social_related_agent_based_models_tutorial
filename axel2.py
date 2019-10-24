import networkx as nx
from matplotlib import pyplot as plt
from random import randrange
import random
from random import randrange
# This program performs one update based on the Axelrod dynamics

F = 3
q = 4 #from 0 to 4
G = nx.complete_graph(9, create_using=None)
pos = nx.spring_layout(G)
#print list(G.nodes)

for n in G.nodes:
#   G.add_node(n, vector=[1, 2, 3])
    G.add_node(n, vector=[randrange(q),randrange(q),randrange(q)])

#print list(G.nodes(data=True))

n1=random.choice (list(G.nodes()))
n2=random.choice (list(G.neighbors(n1)))

print G.node(data='vector')[n1],G.node(data='vector')[n2]

overlap=0;
for i in range(F):
  if G.node(data='vector')[n1][i] == G.node(data='vector')[n2][i]:
     overlap = overlap + 1
print overlap

if (overlap>0 and overlap<F):
  prob = random.uniform (0,1)
  if prob<overlap:
     print 'should change'
     j=0
     while j == 0:
           compontochange = randrange(F)
           print compontochange  
           if G.node(data='vector')[n1][compontochange] != G.node(data='vector')[n2][compontochange]:
              G.node(data='vector')[n1][compontochange] = G.node(data='vector')[n2][compontochange]
              j=1
              print 'doing the change'

print G.node(data='vector')[n1],G.node(data='vector')[n2]
      
