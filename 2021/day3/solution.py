"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1

gamma = []
eps = []

nlines = len(inp)
for i in range(len(inp[0])):
    if sum(int(line[i]) for line in inp) * 2 > nlines:
        gamma.append('1')
        eps.append('0')
    else:
        gamma.append('0')
        eps.append('1')


tg = int("".join(gamma), base=2)
te = int("".join(eps), base=2)

print(f"part 1: {tg * te}")

# part 2

lox = [[int(c) for c in line] for line in inp]
lco = lox[:]

for i in range(len(inp[0])):
    if sum(line[i] for line in lox) * 2 >= len(lox):
        c = 1
    else:
        c = 0
    
    if sum(line[i] for line in lco) * 2 >= len(lco):
        cc = 0
    else:
        cc = 1

    if len(lox) > 1:
        lox = [line for line in lox if line[i] == c]

    if len(lco) > 1:
        lco = [line for line in lco if line[i] == cc]

lox = "".join(str(c) for c in lox[0])
lco = "".join(str(c) for c in lco[0])

print(f"part 2: {int(lox, base=2) * int(lco, base=2)}")











