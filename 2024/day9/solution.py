"""day n"""

from itertools import batched
import re

with open("input") as f:
    inp = f.read().strip() + "0"


# part 1
def create_fs(inp):
    fs = []

    for fileid, (filesize, space) in enumerate(batched(inp, 2)):
        fs.extend([fileid] * int(filesize))
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
            fs.append(lblk)  # put it back
            break

        fs[lix] = lblk


def checksum(fs):
    return sum(bn * fid for (bn, fid) in enumerate(fs))


fs = create_fs(inp)
compact(fs)

print(f"part 1: {checksum(fs)}")


# part 2
def create_fs2(inp):
    fs = []  # tuple (file + fid) or int (space)

    for fileid, (filesize, space) in enumerate(batched(inp, 2)):
        fs.append((fileid, int(filesize)))
        fs.append(int(space))

    return fs


def compact2(fs2):
    fileix = len(fs2) - 1
    while fileix > 0:
        while isinstance(fs2[fileix], int):  # skip final blank spaces
            fileix -= 1

        # try to find a free space
        (fileid, filesize) = fs2[fileix]
        spaceix = 0
        while spaceix < fileix:
            spaceix += 1
            freespace = fs2[spaceix]
            if isinstance(freespace, int) and freespace >= filesize:
                break
        else:
            fileix -= 1
            continue  # could not find free space, try moving the next file

        # move file (horribly inefficient since we're moving lots of elements all the time)
        fs2[spaceix : spaceix + 1] = [0, (fileid, filesize), freespace - filesize]
        assert isinstance(fs2[fileix + 1], int) and isinstance(fs2[fileix + 3], int)
        fs2[fileix + 1 : fileix + 4] = [fs2[fileix + 1] + filesize + fs2[fileix + 3]]

        fileix += 1


def checksum2(fs2):
    blkix = chsum = 0
    for elt in fs2:
        if isinstance(elt, int):
            blkix += elt
            continue

        fileid, filesize = elt
        for _ in range(filesize):
            chsum += fileid * blkix
            blkix += 1

    return chsum


fs2 = create_fs2(inp)
compact2(fs2)
print(f"part 2: {checksum2(fs2)}")
