"""day n"""

# common imports
import functools
import re

with open("input") as f:
    inp = [tuple(int(c) for c in l) for l in f.read().split()]

@functools.cache
def maxjoltage(ndigits: int, bank: tuple[int]) -> int:
    assert 1 <= ndigits <= len(bank)
    if ndigits == 1:
        return max(bank)

    skip_fst = -1 if ndigits == len(bank) else maxjoltage(ndigits, bank[1:])
    dont_skip_fst = 10**(ndigits - 1) * bank[0] + maxjoltage(ndigits-1, bank[1:])
    return max(skip_fst, dont_skip_fst)
    
ans1 = ans2 = 0
for bank in inp:
    ans1 += maxjoltage(2, bank)
    ans2 += maxjoltage(12, bank)

# part 1
print(f"part 1: {ans1}")

# part 2
print(f"part 2: {ans2}")

