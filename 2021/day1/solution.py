"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1

ans = 0
for i in range(len(inp)-1):
    if int(inp[i+1]) > int(inp[i]):
        ans += 1


print(f"part 1: {ans}")

# part 2
ans = 0
for i in range(len(inp)-3):
    if int(inp[i+3]) > int(inp[i]):
        ans += 1

print(f"part 2: {ans}")
