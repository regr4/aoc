"""day n"""

# common imports
from typing import List

with open("input") as f:
    inp = f.read()

# def contains_duplicates(l: List[str]):
#     l.sort()
#     prevCh = ""
#     for c in l:
#         if c == prevCh:
#             return True
#         prevCh = c
#     return False


def contains_duplicates(l: List[str]):
    return len(set(l)) < len(l)


# part 1
for (i, ch) in enumerate(inp):
    if not i >= 3:
        continue

    lastFour = [inp[j] for j in range(i - 3, i + 1)]
    if contains_duplicates(lastFour):
        continue
    print(f"part 1: {i+1}")
    break

# part 2
for (i, ch) in enumerate(inp):
    if not i >= 13:
        continue

    lastFourteen = [inp[j] for j in range(i - 13, i + 1)]
    if contains_duplicates(lastFourteen):
        continue
    print(f"part 2: {i+1}")
    break
