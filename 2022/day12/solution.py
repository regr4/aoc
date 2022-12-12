"""day n"""

from typing import Callable, Dict, List, Set, Tuple, Union
from collections import defaultdict
from queue import PriorityQueue


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


# translated from wikipedia pseudocode
def a_star(g: Graph, start: Node, end: Union[Node, Callable[[Node], bool]]) -> Path:
    endp = end if callable(end) else lambda x: x == end

    def heuristic(n: Node) -> float:
        # can't really find a useful heuristic if we don't know what the end is going to be
        # so just revert to dijkstra's (which is essentially A* with the heuristic always zero)
        if callable(end):
            return 0

        (xn, yn) = n
        (xe, ye) = end
        # taxicab metric.
        # admissible (always underestimates), so we're guaranteed an optimal solution.
        return abs(xn - xe) + abs(yn - ye)

    def reconstructPath(n: Node) -> Path:
        path = [n]
        prev = n
        while (prev := came_from[prev]) != start:
            path.append(prev)
        path.append(start)
        return list(reversed(path))

    # priority queue of nodes. stores tuples (f-score, node) to get the order right
    q: PriorityQueue = PriorityQueue()
    q.put((heuristic(start), start))

    came_from: Dict[Node, Node] = {}

    g_score: Dict[Node, float] = defaultdict(lambda: float("inf"))
    g_score[start] = 0
    f_score: Dict[Node, float] = defaultdict(lambda: float("inf"))
    f_score[start] = heuristic(start)

    while not q.empty():
        _, current = q.get()
        if endp(current):
            return reconstructPath(current)

        for neighbour in g[current]:
            tentative_g_score = g_score[current] + 1  # weights are all 1
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour)
                if neighbour not in q.queue:
                    q.put((f_score[neighbour], neighbour))

    raise Exception("Did not find a path.")


def showPath(path: Path, start: Node, end: Node):
    output = defaultdict(lambda: ".")
    for i in range(len(path) - 1):
        (px, py) = path[i]
        (nx, ny) = path[i + 1]
        output[path[i]] = {(-1, 0): "v", (1, 0): "^", (0, -1): ">", (0, 1): "<"}[
            (px - nx, py - ny)
        ]

    output[start] = "S"
    output[end] = "E"

    for i in range(len(heights)):
        for j in range(len(heights[0])):
            print(output[(i, j)], end="")
        print()


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
res = a_star(
    init_graph(lambda self_height, other_height: other_height <= self_height + 1),
    start,
    end,
)
print(f"part 1: {len(res)-1}")
# showPath(res, start, end)


# part 2
res = a_star(
    init_graph(lambda self_height, other_height: self_height <= other_height + 1),
    end,
    lambda pos: heights[pos[0]][pos[1]] == 0,
)
print(f"part 2: {len(res)-1}")
# showPath(res, end, res[-1])
