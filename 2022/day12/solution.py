"""day n"""

from typing import Callable, Dict, List, Set, Tuple, Union
from collections import defaultdict

with open("input") as f:
    inp = f.read()


Node = Tuple[int, int]
Graph = Dict[Node, Set[Node]]
Path = List[Node]


def get_height(c: str) -> int:
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - ord("a")


heights: List[List[int]] = []
start: Node
end: Node

for i, r in enumerate(inp.split()):
    heights.append([])
    for j, c in enumerate(r):
        heights[-1].append(get_height(c))

        if c == "S":
            start = (i, j)
        elif c == "E":
            end = (i, j)


# I tried to implement A*, but it gave me the wrong answer. Not sure what I did wrong, the heuristic seems to be fine. Maybe priorityqueue is not doing what i think it is?
"""
from queue import PriorityQueue

# translated from wikipedia pseudocode
def a_star(g: Graph) -> Path:
    def heuristic(n: Node) -> float:
        (xn, yn) = n
        (xe, ye) = end
        return abs(xn - xe) + abs(yn - ye)
        # return min(abs(xn - xe), abs(yn - ye))

    def reconstructPath(n: Node) -> Path:
        path = [n]
        prev = n
        while (prev := came_from[prev]) != start:
            path.append(prev)
        return list(reversed(path))

    q: PriorityQueue = PriorityQueue()
    q.put(start)

    came_from: Dict[Node, Node] = {}

    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    f_score = defaultdict(lambda: float("inf"))
    f_score[start] = heuristic(start)

    while not q.empty():
        current = q.get()
        if current == end:
            return reconstructPath(current)

        for neighbour in g[current]:
            # print(f"{neighbour = }")
            tentative_g_score = g_score[current] + 1  # weights are all 1
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour)
                if neighbour not in q.queue:
                    q.put(neighbour)

    OhNo()


def showPath():
    output = defaultdict(lambda: ".")
    output[start] = "S"
    output[end] = "E"
    for i in range(len(res) - 1):
        (px, py) = res[i]
        (nx, ny) = res[i + 1]
        output[res[i]] = {(-1, 0): "v", (1, 0): "^", (0, -1): ">", (0, 1): "<"}[
            (px - nx, py - ny)
        ]

    for i in range(len(heights)):
        for j in range(len(heights[0])):
            print(output[(i, j)], end="")
        print()

res = a_star(graph)
"""


def dijkstra(g: Graph, start: Node, end: Union[Node, Callable[[Node], bool]]) -> float:
    if not callable(end):
        endp = lambda x: x == end
    else:
        endp = end

    unvisited = set(g.keys())
    tentative_distance: Dict[Node, float] = defaultdict(lambda: float("inf"))
    tentative_distance[start] = 0
    curr_node = start
    while not endp(curr_node):
        for n in g[curr_node]:
            if n in unvisited:
                tentative_distance[n] = min(
                    tentative_distance[n], tentative_distance[curr_node] + 1
                )
        unvisited.remove(curr_node)

        curr_node = next(iter(unvisited))
        for n in unvisited:
            if tentative_distance[n] <= tentative_distance[curr_node]:
                curr_node = n

    return tentative_distance[curr_node]


def init_graph(pred: Callable[[int, int], bool]) -> Graph:
    graph = defaultdict(set)
    for i, row in enumerate(heights):
        for j, num in enumerate(row):
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < len(heights) and 0 <= y < len(row):
                    if pred(num, heights[x][y]):
                        graph[(i, j)].add((x, y))

    return graph


# part 1
graph = init_graph(lambda self_height, other_height: other_height <= self_height + 1)
res = dijkstra(graph, start, end)
print(f"part 1: {res}")

# part 2
graph = init_graph(lambda self_height, other_height: self_height <= other_height + 1)
res = dijkstra(graph, end, lambda pos: heights[pos[0]][pos[1]] == 0)
print(f"part 2: {res}")
