"""day n"""

# common imports
import re

with open("input-instrs") as f:
    inp = f.read()

# part 1
import secret
initial = secret.initial.copy()

regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

def move(amt, fst, snd):
    for i in range(amt):
        initial[snd] += initial[fst][-1]
        initial[fst] = initial[fst][:-1]

for match in regex.findall(inp):
    match2 = [int(m) for m in match]
    move(*match2)

res = "".join([initial[i][-1] for i in range(1, 10)])
print(f"part 1: {res}")

#part 2

initial = secret.initial.copy()

def move2(amt, fst, snd):
    initial[snd] += initial[fst][-amt:]
    initial[fst] = initial[fst][:-amt]

for match in regex.findall(inp):
    match2 = [int(m) for m in match]
    move2(*match2)

res = "".join([initial[i][-1] for i in range(1, 10)])
print(f"part 2: {res}")
