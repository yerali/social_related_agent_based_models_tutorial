import networkx as nx
from matplotlib import pyplot as plt
from random import randrange
import random
from random import randrange
# This program performs one update based on the Axelrod dynamics

 
F = 3
q = 4 #from 0 to 
n=9
G = nx.complete_graph(n, create_using=None)
pos = nx.spring_layout(G)
print(list(G.nodes))

 

for n in G.nodes:
#   G.add_node(n, vector=[1, 2, 3])
    G.add_node(n, vector=[randrange(q),randrange(q),randrange(q)])

 

print(list(G.nodes(data=True)))

 

n1=random.choice(list(G.nodes()))
n2=random.choice(list(G.neighbors(n1)))

 

print(G.nodes(data='vector')[n1],G.nodes(data='vector')[n2])

 

overlap=0
for i in range(F):
    if G.nodes(data='vector')[n1][i] == G.nodes(data='vector')[n2][i]:
        overlap = overlap + 1
print(overlap)

 

if (overlap>0 and overlap<F):
    prob = random.uniform (0,1)
    if prob<overlap:
        print('should change')
        j=0
        while j == 0:
            compontochange = randrange(F)
            print(compontochange)
            if G.nodes(data='vector')[n1][compontochange] != G.nodes(data='vector')[n2][compontochange]:
                G.nodes(data='vector')[n1][compontochange] = G.nodes(data='vector')[n2][compontochange]
                j=1
                print('doing the change')

 

print(G.nodes(data='vector')[n1],G.nodes(data='vector')[n2])
# Done by Julien Delages
