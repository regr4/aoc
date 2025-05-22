"""day n"""

# common imports
import re
import networkx as nwx

with open("input") as f:
    inp = f.read().splitlines()


def ib(x, y):
    return 0 <= x < len(inp[0]) and 0 <= y < len(inp)


def accessible(x, y):
    if not ib(x, y):
        return False
    return inp[y][x] != "#"


def ix(x, y):
    if not ib(x, y):
        return None
    return inp[y][x]


G1 = nwx.DiGraph()
G2 = nwx.Graph()
for y, l in enumerate(inp):
    for x, c in enumerate(l):
        if c == "#":
            continue
        
        for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if accessible(nx, ny):
                G2.add_edge((x,y),(nx,ny), weight= 1)

        if c == "^":
            ny = y - 1
            if accessible(x, ny):
                G1.add_edge((x, y), (x, ny))
            continue
        if c == "v":
            ny = y + 1
            if accessible(x, ny):
                G1.add_edge((x, y), (x, ny))
            continue
        if c == "<":
            nx = x - 1
            if accessible(nx, y):
                G1.add_edge((x, y), (nx, y))
            continue
        if c == ">":
            nx = x + 1
            if accessible(nx, y):
                G1.add_edge((x, y), (nx, y))
            continue
        if c == ".":
            # left?
            nx, ny = x - 1, y
            if ix(nx, ny) in list(".<^v"):
                G1.add_edge((x, y), (nx, ny))
            # right?
            nx, ny = x + 1, y
            if ix(nx, ny) in list(".>^v"):
                G1.add_edge((x, y), (nx, ny))
            # up?
            nx, ny = x, y - 1
            if ix(nx, ny) in list(".<>^"):
                G1.add_edge((x, y), (nx, ny))
            # down?
            nx, ny = x, y + 1
            if ix(nx, ny) in list(".<>v"):
                G1.add_edge((x, y), (nx, ny))

start = (1, 0)
end = (139, 140)

pathlens1 = map(len, nwx.all_simple_paths(G1, start, end))

for node in G2.nodes():
    if G2.degree(node) == 2:
        e1, e2 = G2.edges(node)
        w1 = G2.edges[e1]["weight"]
        w2 = G2.edges[e2]["weight"]

        _, n1 = e1
        _,n2 = e2
        assert n1 != node
        assert n2 != node
        G2.remove_edge(node, n1)
        G2.remove_edge(node, n2)
        G2.add_edge(n1, n2, weight = w1+w2)

G2.remove_nodes_from(tuple(n for n in G2.nodes() if G2.degree(n) == 0))

# terribly inefficient but it works
wts = []
for p in nwx.all_simple_paths(G2, start, end):
    wts.append(nwx.path_weight(G2, p, 'weight'))


# part 1
print(f"part 1: {max(pathlens1) - 1}")

# part 2
print(f"part 2: {max(wts)}")
