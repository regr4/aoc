"""day n"""

# common imports
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from typing import Dict, List, Set
import itertools
import re

with open("input_test") as f:
    inp = f.read().strip()

regex = re.compile(
    r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (\w+(?:, \w+)*)$"
)


@dataclass
class Room:
    # label: str
    flow_rate: int
    neighbours: Dict[str, int]


Graph = Dict[str, Room]

graph: Graph = {}

for l in inp.split("\n"):
    match = regex.match(l)
    if match is None:
        # print(l)
        raise Exception("oh no")

    name, flow_rate, neighbours = match.groups()

    graph[name] = Room(int(flow_rate), {n: 1 for n in neighbours.split(", ")})

orig_graph = deepcopy(graph)


def remove_zero(g: Graph, lbl: str):
    assert g[lbl].flow_rate == 0
    assert lbl != "AA"

    for neighbour1, weight1 in g[lbl].neighbours.items():
        for neighbour2, weight2 in g[lbl].neighbours.items():
            if neighbour1 == neighbour2:
                continue
            if (
                neighbour2 not in g[neighbour1].neighbours
                or weight1 + weight2 < g[neighbour1].neighbours[neighbour2]
            ):
                g[neighbour1].neighbours[neighbour2] = weight1 + weight2
                g[neighbour2].neighbours[neighbour1] = weight1 + weight2

    del g[lbl]
    for v in g.values():
        if lbl in v.neighbours:
            del v.neighbours[lbl]


g2 = graph.copy()

for lbl, r in graph.items():
    if r.flow_rate == 0 and lbl != "AA":
        remove_zero(g2, lbl)

graph = g2
# print(graph)


from queue import SimpleQueue


def min_dist(g, n1, n2) -> int:
    # bfs because it's simpler
    def reconstruct_path(v: str) -> List[str]:
        path = [v]
        if v == n1:
            return []
        while (v := parent[v]) != n1:
            # print(v)
            path.append(v)
        return path

    explored = set([n1])
    q = SimpleQueue()
    q.put(n1)
    parent: Dict[str, str] = {}

    while not q.empty():
        v = q.get()
        if v == n2:
            return len(reconstruct_path(v))

        for w in g[v].neighbours:
            if w in explored:
                continue
            explored.add(w)
            parent[w] = v
            q.put(w)

    raise Exception("could not find path to goal")


distance_matrix = {
    (a, b): min_dist(orig_graph, a, b) for a, b in itertools.product(graph, graph)
}

heuristic_matrix = {
    (a, b): graph[b].flow_rate / (distance_matrix[(a, b)] + 1)
    for a, b in itertools.product(graph, graph)
}


print(distance_matrix)
print(heuristic_matrix)


# greedy solution (probably won't work)
# curr_node = "AA"
# curr_time = 0
# curr_opened = 0
# curr_score = 0

# while True:
#     candidates = [b for a, b in heuristic_matrix if a == curr_node]
#     candidates_h = [(heuristic_matrix[(curr_node, c)], c) for c in candidates]
#     if not candidates_h:
#         curr_score += (30 - curr_time) * curr_opened
#         break
#     _, best_candidate = max(candidates_h)

#     time_to_go_there = distance_matrix[(curr_node, best_candidate)] + 1
#     if curr_time + time_to_go_there >= 30:
#         curr_score += (30 - curr_time) * curr_opened
#         break

#     print(best_candidate)

#     curr_time += time_to_go_there
#     curr_score += time_to_go_there * curr_opened
#     curr_node = best_candidate
#     curr_opened += graph[best_candidate].flow_rate

#     heuristic_matrix = {k: v for k, v in heuristic_matrix.items() if k[0] != curr_node}

#     # print(max(candidates_h))

# print(curr_score)

# brute force?
# def bruteforce():
    # ...


# def print_graph(g: Graph):
    # print("graph data {")
    # seen: Set[str] = set()
    # for n, r in g.items():
        # seen.add(n)
        # print(f"{n} -- {{{' '.join(p for p in r.neighbours if p not in seen)}}};")

    # print("}")


# print_graph(graph)

# now what?
# try just brute-force traversing it?


# print(data)

# part 1
# print(f"part 1: {None}")

# part 2
# print(f"part 2: {None}")
