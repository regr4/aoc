"""day n"""

# common imports
import re, itertools, math

with open("input") as f:
    inp = f.read()

directions, rest = inp.split("\n\n")

nodes = {}
for line in rest.splitlines():
    fro, tol, tor = re.findall(r"\w{3}", line)
    nodes[fro] = (tol, tor)


# part 1
res = 0
currNode = "AAA"
for d in itertools.cycle(directions):
    if currNode == "ZZZ":
        break
    if d == "L":
        currNode = nodes[currNode][0]
    elif d == "R":
        currNode = nodes[currNode][1]
    else:
        assert False
    res += 1


print(f"part 1: {res}")

# part 2
res = 1
for c in nodes.keys():
    if not c.endswith("A"):
        continue

    n = 0
    curr = c
    for d in itertools.cycle(directions):
        if curr.endswith("Z"):
            break
        if d == "L":
            curr = nodes[curr][0]
        if d == "R":
            curr = nodes[curr][1]
        n += 1
    res = math.lcm(res, n)


print(f"part 2: {res}")
