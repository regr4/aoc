"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

numbers = [int(n) for n in inp[0].split(",")]

def parse_board(s):
    s = s.strip()
    r = []
    for line in s.splitlines():
        r.append([])
        for n in line.split():
            r[-1].append(int(n))
    return r

boards = [parse_board(s) for s in "\n".join(inp[1:]).split("\n\n")]

print(set(len(board) for board in boards))

def calc_winner(ns):
    def calc_score(ns, b):
        b2 = sum(sum(n for n in line if n not in ns) for line in b)
        return ns[-1]*b2

    for board in boards[:]:
        for i in range(5):
            if all(x in ns for x in board[i]):
                boards.remove(board)
                return calc_score(ns, board)
            if all(x in ns for x in [board[j][i] for j in range(5)]):
                boards.remove(board)
                return calc_score(ns, board)

        if (all(x in ns for x in [board[i][i] for i in range(5)])
                or all(x in ns for x in [board[i][4-i] for i in range(5)])):
                boards.remove(board)
                return calc_score(ns, board)
    return 0

winners = []
i = 1
while boards:
    if (r := calc_winner(numbers[:i])):
        winners.append(r)
    else:
        i += 1

print(f"part 1: {winners[0]}")
# part 2
print(f"part 2: {winners[-1]}")
