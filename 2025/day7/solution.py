"""day n"""

# common imports
import functools

with open("input") as f:
    inp = f.read().splitlines()

# part 1
state = [c == "S" for c in inp[0]]

split_count = 0
for r in inp[1:]:
    new_state = [False] * len(state)

    for i in range(len(state)):
        if state[i] and r[i] == ".":
            new_state[i] = True
        elif state[i] and r[i] == "^":
            split_count += 1
            new_state[i - 1] = True  # bounds checking not necessary with given input
            new_state[i + 1] = True

    state = new_state

print(f"part 1: {split_count}")


# part 2
@functools.cache
def num_worlds(row, col):
    if row == len(inp):
        return 1
    if inp[row][col] == ".":
        return num_worlds(row + 1, col)
    if inp[row][col] == "^":
        return num_worlds(row + 1, col - 1) + num_worlds(row + 1, col + 1)


ans = num_worlds(1, inp[0].index("S"))

print(f"part 2: {ans}")
