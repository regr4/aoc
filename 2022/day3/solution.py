"""day 3"""

with open("input2") as f:
    input = f.read()

def priority(chr):
    if ord("a") <= ord(chr) <= ord("z"):
        return ord(chr) - ord("a") + 1
    elif ord("A") <= ord(chr) <= ord("Z"):
        return ord(chr) - ord("A") + 27
    raise Exception(f"invalid char {chr}")


res = 0
for line in input.split():
    if not line:
        continue

    split_point = int(len(line)/2)
    first_part = line[:split_point]
    second_part = line[split_point:]

    for ch in first_part:
        if ch in second_part:
            res += priority(ch)
            break # otherwise we're double counting sometimes

print(f"part 1: {res}")

import re

res = 0
regex = re.compile(r"\w+\s\w+\s\w+")
for x in regex.findall(input):
    (fst, snd, thr) = x.split()
    for ch in fst:
        if ch in snd and ch in thr:
            res += priority(ch)
            break

print(f"part 2: {res}")
