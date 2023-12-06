"""day n"""

# common imports
from collections import defaultdict
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1


res = 0
gears = defaultdict(set)
for ix, row in enumerate(inp):
	for m in re.finditer("\d+", row):
		good = False
		s = m.start()
		e = m.end()
		neighbours = [(ix, s-1), (ix, e)]
		for i in range(s-1, e+1):
			neighbours.append((ix+1, i))
			neighbours.append((ix-1, i))

		for (y,x) in neighbours:
			try:
				c = inp[y][x]
				if not c.isdigit() and c != ".":
					good = True
				if c == "*":
					gears[(y,x)].add(m)

			except IndexError: pass

		if good:
			res += int(m.group())


print(f"part 1: {res}")

#part 2

res = 0
for neighbours in gears.values():
	if len(neighbours) == 2:
		n=list(neighbours)
		res += int(n[0].group())*int(n[1].group())

print(f"part 2: {res}")
