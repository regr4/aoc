"""day n"""

with open("input") as f:
    inp = f.read().strip()

instrs = [l.split() for l in inp.split("\n")]


def dif(v1, v2):
    return [c1 - c2 for (c1, c2) in zip(v1, v2)]


def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num


def move_head(direction, head_pos):
    if direction == "U":
        head_pos[1] += 1
    elif direction == "D":
        head_pos[1] -= 1
    elif direction == "R":
        head_pos[0] += 1
    elif direction == "L":
        head_pos[0] -= 1


def move_tail(head_pos, tail_pos):
    # H.T -> HT
    if sorted([abs(a) for a in dif(head_pos, tail_pos)]) == [0, 2]:
        for i in range(2):
            tail_pos[i] = tail_pos[i] / 2 + head_pos[i] / 2

    # H..
    # ..T
    # -> HT
    elif sorted([abs(a) for a in dif(head_pos, tail_pos)]) == [1, 2]:
        for i in range(2):
            tail_pos[i] += clamp(head_pos[i] - tail_pos[i], -1, 1)

    # H..
    # ...
    # ..T
    # ->
    # H.
    # .T
    # only applies in the longer rope case, as the previous node may move diagonally.
    elif sorted([abs(a) for a in dif(head_pos, tail_pos)]) == [2, 2]:
        for i in range(2):
            tail_pos[i] += clamp(head_pos[i] - tail_pos[i], -1, 1)


# part 1
head_pos = [0, 0]
tail_pos = [0, 0]

tail_seen = set()
for direction, amt in instrs:
    for _ in range(int(amt)):
        move_head(direction, head_pos)
        move_tail(head_pos, tail_pos)
        tail_seen.add(tuple(tail_pos))


print(f"part 1: {len(tail_seen)}")


# part 2
rope = [[0, 0] for i in range(10)]
tail_seen = set()


for direction, amt in instrs:
    for _ in range(int(amt)):
        move_head(direction, rope[0])
        for i in range(len(rope) - 1):
            move_tail(rope[i], rope[i + 1])
            tail_seen.add(tuple(rope[-1]))

print(f"part 2: {len(tail_seen)}")
