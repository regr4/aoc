"""day n"""

# common imports
from functools import reduce
import typing
from typing import Callable, Dict, List, Set, Tuple

with open("input") as f:
    inp = f.read().strip()

Coord = Tuple[int, int, int]
BBox = Tuple[Coord, Coord]


def neighbours(c: Coord) -> List[Coord]:
    (x, y, z) = c
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]


occupied: Set[Coord] = typing.cast(
    Set[Coord], set(tuple(int(i) for i in x.split(",")) for x in inp.split("\n"))
)

# part 1
res = 0
for n in occupied:
    for c in neighbours(n):
        if c not in occupied:
            res += 1

print(f"part 1: {res}")

# part 2
def lift_tuple(f: Callable[[int, int], int]) -> Callable[[Coord, Coord], Coord]:
    return lambda t1, t2: typing.cast(Coord, tuple(f(*v) for v in zip(t1, t2)))


# such pythonic. much wow
bbox = tuple(reduce(lift_tuple(f), list(occupied)) for f in [min, max])


def inside(box, c):
    return all(box[0][i] <= c[i] <= box[1][i] for i in range(len(c)))


# cache is preserved across function calls because python is evil
# would have used @functools.cache but i'm stuck on 3.8
def is_outside(box, c: Coord, cache={}):
    def set_cache(res):
        for x in visited:
            cache[x] = res
        return res

    # flood fill
    candidates = [c]
    visited: Set[Coord] = set()
    while candidates:
        n = candidates.pop()

        if n in cache:
            return set_cache(cache[n])

        if n in visited:
            continue

        if not inside(box, n):
            return set_cache(True)

        visited.add(n)
        candidates.extend(filter(lambda x: x not in occupied, neighbours(n)))

    return set_cache(False)


res = 0
for n in occupied:
    for c in neighbours(n):
        if c not in occupied and is_outside(bbox, c):
            res += 1

print(f"part 2: {res}")
