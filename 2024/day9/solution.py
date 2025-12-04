"""day n"""

from itertools import batched
import re

with open("input") as f:
    inp = f.read().strip() + '0'

def create_fs(inp):
    fs = []

    for (blkid, (blk, space)) in enumerate(batched(inp, 2)):
        fs.extend([blkid] * int(blk))
        fs.extend([None] * int(space))

    return fs

def compact(fs):
    lix = 0

    while True:
        lblk = None
        while lblk is None:
            lblk = fs.pop()
            
        while lix < len(fs) and fs[lix] is not None:
            lix += 1

        if lix == len(fs):
            fs.append(lblk) # put it back
            break

        fs[lix] = lblk

def checksum(fs):
    return sum(bn*fid for (bn, fid) in enumerate(fs))

fs = create_fs(inp)
compact(fs)

# part 1
print(f"part 1: {checksum(fs)}")

# part 2
print(f"part 2: {None}")
