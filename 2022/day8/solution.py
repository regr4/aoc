"""day n"""

# common imports
import re
from itertools import count

with open("input") as f:
    inp = f.read()

# part 1
inp = inp.split()
inp = [[int(x) for x in r] for r in inp]
w = len(inp[0])
h = len(inp)

seen = [[False for _ in inp[i]] for i in range(h)]

# from left
for i, row in enumerate(inp):
    prev = float("-inf")
    for j, tree in enumerate(row):
        if tree > prev:
            seen[i][j] = True
            prev = tree

# from right
for i, row in enumerate(inp):
    prev = float("-inf")
    for j, tree in enumerate(reversed(row)):
        if tree > prev:
            seen[i][w - j - 1] = True
            prev = tree

# from top
for j in range(h):
    prev = float("-inf")
    for i in range(w):
        tree = inp[i][j]
        if tree > prev:
            seen[i][j] = True
            prev = tree

# from bottom
for j in range(h):
    prev = float("-inf")
    for i in reversed(range(w)):
        tree = inp[i][j]
        if tree > prev:
            seen[i][j] = True
            prev = tree

res = 0
for row in seen:
    for b in row:
        if b:
            res += 1

print(f"part 1: {res}")

# part 2
def get_score(x, y):
    own_height = inp[y][x]
    up = 1
    for j in count(y - 1, -1):
        if j < 0:
            up -= 1
            break
        if (inp[j][x]) < own_height:
            up += 1
        else:
            break

    down = 1
    for j in count(y + 1, 1):
        if j > h - 1:
            down -= 1
            break
        if (tree := inp[j][x]) < own_height:
            down += 1
        else:
            break

    left = 1
    for j in count(x - 1, -1):
        if j < 0:
            left -= 1
            break
        if (inp[y][j]) < own_height:
            left += 1
        else:
            break

    right = 1
    for j in count(x + 1, 1):
        if j > w - 1:
            right -= 1
            break
        if (inp[y][j]) < own_height:
            right += 1
        else:
            break

    return up * down * left * right


max_score = float("-inf")
for i in range(w):
    for j in range(h):
        max_score = max(max_score, get_score(i, j))

print(f"part 2: {max_score}")
