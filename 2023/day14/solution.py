"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1
def transpose(board):
    return [
        "".join(board[i][j] for i in range(len(board))) for j in range(len(board[0]))
    ]


def slide_rocks(tinp):
    temp = tinp
    while True:
        n = [x.replace(".O", "O.") for x in temp]
        if n == temp:
            break
        temp = n
    return temp


def calc_load(board):
    return sum(
        sum(i for i, c in enumerate(reversed(r), start=1) if c == "O") for r in board
    )


print(f"part 1: {calc_load(slide_rocks(transpose(inp)))}")


# part 2
# Since we transposed it, we need to rotate counterclockwise.
def rotate(board):
    return transpose(board)[::-1]


def spin_cycle(r):
    temp = r
    for i in range(4):
        temp = slide_rocks(temp)
        temp = rotate(temp)
    return temp


# detect cycles using the tortoise and hare algorithm
# https://en.wikipedia.org/wiki/Cycle_detection
tortoise = hare = transpose(inp)

tortoise = spin_cycle(tortoise)
hare = spin_cycle(spin_cycle(hare))
i = 1
while tortoise != hare:
    tortoise = spin_cycle(tortoise)
    hare = spin_cycle(spin_cycle(hare))
    i += 1

assert i < 1000000000

# number of times we still need to move the tortoise: 1000000000 - i
# but since there's a cycle of length dividing i, this is the same as doing it (1000000000 - i) % i = 1000000000 % i times.
for k in range(1000000000 % i):
    tortoise = spin_cycle(tortoise)

print(f"part 2: {calc_load(tortoise)}")
