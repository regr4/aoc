"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read()

# part 1

res = 0
nrs = []
for line in inp.splitlines():
	[_, n] = line.split(": ")
	l,r = n.split("|")
	ln = set(int(x) for x in l.split())
	lr = set(int(x) for x in r.split())
	n = len(ln & lr)
	nrs.append(n)
	if n:
		res += 2 ** (n-1)

print(f"part 1: {res}")

#part 2

copies = [1 for x in nrs]

for ix, k in enumerate(nrs):
	for i in range(ix+1, ix+1+k):
		copies[i] += copies[ix]



print(f"part 2: {sum(copies)}")
