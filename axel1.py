import networkx as nx
from matplotlib import pyplot as plt
from random import randrange
import random

G = nx.complete_graph(9, create_using=None)
pos = nx.spring_layout(G)
#print list(G.nodes)
#print list(G.nodes(data=True))

#G.add_node(1, vector=[1, 2, 3])
#G.add_node(1, vector=[randrange(4),randrange(4),randrange(4)])

for n in G.nodes:
#   G.add_node(n, vector=[1, 2, 3])
    G.add_node(n, vector=[randrange(4),randrange(4),randrange(4)])

print list(G.nodes(data=True))
