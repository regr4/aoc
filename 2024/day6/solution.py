"""day n"""

# common imports
import re

with open("input") as f:
    inp = [l for l in f.read().splitlines()]

WIDTH = len(inp[0])
HEIGHT = len(inp)

def ix(inp: list[str], c: complex):
    if not (0 <= c.real < HEIGHT and 0 <= c.imag < WIDTH):
        raise IndexError()

    return inp[int(c.real)][int(c.imag)]

class InfiniteLoopDetected(Exception):
    pass

def run_setup(inp):
    for row, line in enumerate(inp):
        for col, char in enumerate(line):
            if char == "^":
                pos = row + col * 1j
                break

    dir = -1 + 0j
    visited = set()
    
    try:
        while True:
            if (pos, dir) in visited:
                raise InfiniteLoopDetected()
            visited.add((pos, dir))
            # if this throws, then we've walked off the map!
            if ix(inp, pos + dir) == "#":
                dir *= -1j # turn clockwise (real axis points down, imaginary right)
            else:
                pos += dir
    except IndexError:
        pass

    return len(set(pos for pos, dir in visited))

# part 1
print(f"part 1: {run_setup(inp)}")


# slow but works
# more convenient to mutate, still works the same
inp2 = [[c for c in l] for l in inp]
ans = 0
for i in range(HEIGHT):
    print(i)
    for j in range(WIDTH):
        if inp2[i][j] != ".":
            continue
        inp2[i][j] = "#"
        try:
            run_setup(inp2)
        except InfiniteLoopDetected:
            ans += 1
        inp2[i][j] = "."


# part 2
print(f"part 2: {ans}")
