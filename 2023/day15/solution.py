"""day n"""

# common imports
import collections
import re

with open("input") as f:
    inp = f.read().strip().split(",")


# part 1
def hash(s):
    r = 0
    for c in s:
        r += ord(c)
        r *= 17
        r %= 256
    return r


print(f"part 1: {sum(map(hash, inp))}")

# part 2
boxes = [[] for _ in range(256)]

for ins in inp:
    if m := re.match(r"(\w+)=(\d)", ins):
        label = m.group(1)
        box = hash(label)
        flen = int(m.group(2))
        for i in range(len(boxes[box])):
            if label == boxes[box][i][0]:
                boxes[box][i] = (label, flen)
                break
        else:
            boxes[box].append((label, flen))
    elif m := re.match(r"(\w+)-", ins):
        label = m.group(1)
        box = hash(label)
        boxes[box] = [item for item in boxes[box] if item[0] != label]
    else:
        assert False

ans = 0
for bn, box in enumerate(boxes, start=1):
    for ln, (_, fl) in enumerate(box, start=1):
        ans += bn * ln * fl

print(f"part 2: {ans}")
