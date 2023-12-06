"""day n"""

# common imports
from copy import deepcopy
from dataclasses import dataclass
from typing import List

with open("input") as f:
    inp = f.read().strip()

lines = [int(x) for x in inp.split()]

# print(len(lines))


# @dataclass
class CircularList:
    def __init__(self, clist):
        self.clist = clist
        self.positions = list(range(len(clist)))
        # positions[i] is the current position of the original i'th element
        self.inv_positions = list(range(len(clist)))
        # inv_positions[i] is the original position of the current i'th element.

    def __str__(self):
        return '\n'.join((str(self.positions), str(self.clist), str(self.inv_positions)))

    def move(self, idx, amt):
        inv_pos_old = deepcopy(self.inv_positions)
        new_pos = (idx + amt) % len(self.clist)

        # update list and inv_positions
        if new_pos > idx:
            old_val = self.clist[idx]
            old_val_inv_pos = self.inv_positions[idx]
            for i in range(idx, new_pos):
                self.clist[i] = self.clist[i + 1]
                self.inv_positions[i] = self.inv_positions[i+1]
            self.clist[new_pos] = old_val
            self.inv_positions[new_pos] = old_val_inv_pos

        elif new_pos < idx:
            old_val = self.clist[idx]
            old_val_inv_pos = self.inv_positions[idx]
            for i in reversed(range(new_pos, idx)):
                self.clist[i + 1] = self.clist[i]
                self.inv_positions[i+1] = self.inv_positions[i]
            self.clist[new_pos] = old_val
            self.inv_positions[new_pos] = old_val_inv_pos

        # update positions
        self.positions[inv_pos_old[idx]] = new_pos
        if new_pos > idx:
            for i in range(idx+1, new_pos+1):
                self.positions[inv_pos_old[i]] -= 1
        elif new_pos < idx:
            for i in range(new_pos, idx):
                self.positions[inv_pos_old[i]] += 1

# lines_l = CircularList([4, -2, 5, 6, 7, 8, 9])
lines_l = CircularList(list(range(10)))

# import random

# for i in range(50):
#     # lines_l2 = deepcopy(lines_l)
#     amt = random.randint(-5, 5)
#     idx = random.randint(0, 9)
#     print(idx, amt)
#     lines_l.move(idx, amt)
#     # print(i)
#     print(lines_l, end='\n\n')

lines_l = CircularList(lines)

for i in range(len(lines_l.clist)):
    idx = lines_l.positions[i]
    amt = lines_l.clist[idx]
    lines_l.move(idx, amt)

# calculate result
clist = lines_l.clist
zero_idx = clist.index(0)
res = sum(clist[(zero_idx + i) % len(clist)] for i in [1000, 2000, 3000])

# part 1
print(f"part 1: {res}")

# part 2
print(f"part 2: {None}")
