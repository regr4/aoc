"""day n"""

# common imports
from math import prod
import networkx as nx
import re

with open("input") as f:
    inp = f.read().splitlines()

G = nx.Graph()
for line in inp:
    s, ts = line.split(": ")
    for t in ts.split():
        G.add_edge(s, t)

l = list(nx.k_edge_components(G, 4))
print(len(l))
cs = prod(map(len,l))

# part 1
print(f"part 1: {cs}")

# part 2
print(f"part 2: {None}")
