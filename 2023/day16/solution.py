"""day n"""

# common imports
import re
from queue import Queue

with open("input") as f:
    inp = f.read().splitlines()

# part 1
Tile = tuple[int, int]
Direction = int
Beam = tuple[Tile, Direction]

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3


def march(t: Tile, d: Direction) -> Tile:
    x, y = t
    if d == RIGHT:
        x += 1
    elif d == LEFT:
        x -= 1
    elif d == UP:
        y -= 1
    elif d == DOWN:
        y += 1
    return (x, y)


def get(b, t: Tile) -> str:
    x, y = t
    return b[y][x]


def ib(b, t: Tile) -> bool:
    x, y = t
    return 0 <= x < len(b[0]) and 0 <= y < len(b)


def solve(board, initpos: Tile, initd: Direction) -> int:
    board = inp
    curr: Queue[Beam] = Queue()
    curr.put((initpos, initd))
    energised: set[tuple[Tile, Direction]] = set()

    while curr.qsize():
        t, d = curr.get()
        if (t, d) in energised:
            continue

        energised.add((t, d))
        c = get(board, t)
        match c:
            case ".":
                t2 = march(t, d)
                if ib(board, t2):
                    curr.put((t2, d))
            case "/":
                d2 = {RIGHT: UP, LEFT: DOWN, UP: RIGHT, DOWN: LEFT}[d]
                t2 = march(t, d2)
                if ib(board, t2):
                    curr.put((t2, d2))
            case "\\":
                d2 = {RIGHT: DOWN, LEFT: UP, UP: LEFT, DOWN: RIGHT}[d]
                t2 = march(t, d2)
                if ib(board, t2):
                    curr.put((t2, d2))
            case "|":
                if d in (LEFT, RIGHT):
                    cds = (UP, DOWN)
                else:
                    cds = (d,)
                for cd in cds:
                    t2 = march(t, cd)
                    if ib(board, t2):
                        curr.put((t2, cd))
            case "-":
                if d in (UP, DOWN):
                    cds = (LEFT, RIGHT)
                else:
                    cds = (d,)
                for cd in cds:
                    t2 = march(t, cd)
                    if ib(board, t2):
                        curr.put((t2, cd))

    return len({t for (t, d) in energised})


print(f"part 1: {solve(inp, (0, 0), RIGHT)}")

# part 2
initials = []
for i in range(len(inp)):
    initials.append(((0, i), RIGHT))
    end = len(inp[i]) - 1
    initials.append(((end, i), LEFT))
for i in range(len(inp[0])):
    initials.append(((i, 0), DOWN))
    end = len(inp) - 1
    initials.append(((i, end), UP))

print(f"part 2: {max(solve(inp, *ini) for ini in initials)}")
