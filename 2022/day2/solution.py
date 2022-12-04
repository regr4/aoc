"""day 2"""

with open("input2") as f:
    strategy = f.read()

strategy_lines = [line.split() for line in strategy.split("\n")]

def isWinning(l):
    if l in [['A', 'Y'], ['B', 'Z'], ['C', 'X']]:
        return True
    return False

def isDraw(l):
    if l in [['A', 'X'], ['B', 'Y'], ['C', 'Z']]:
        return True
    return False

def getScore(ch):
    return {'X' : 1, 'Y': 2, 'Z': 3}[ch]

# part 1
score = 0
for line in strategy_lines:
    if not line:
        continue

    if isWinning(line):
        score += 6
    elif isDraw(line):
        score += 3

    score += getScore(line[1])

print(f"score for part 1: {score}")

# part 2
def value(line):
    if line == ['A', 'X']:
        return 0 + 3
    elif line == ['A', 'Y']:
        return 3 + 1
    elif line == ['A', 'Z']:
        return 6 + 2
    elif line == ['B', 'X']:
        return 0 + 1
    elif line == ['B', 'Y']:
        return 3 + 2
    elif line == ['B', 'Z']:
        return 6 + 3
    elif line == ['C', 'X']:
        return 0 + 2
    elif line == ['C', 'Y']:
        return 3 + 3
    elif line == ['C', 'Z']:
        return 6 + 1

score = 0
for line in strategy_lines:
    if not line:
        continue

    # print(line, value(line))
    if line == ['A', 'X']:
        score += value(line)
    elif line == ['A', 'Y']:
        score += value(line)
    elif line == ['A', 'Z']:
        score += value(line)
    elif line == ['B', 'X']:
        score += value(line)
    elif line == ['B', 'Y']:
        score += value(line)
    elif line == ['B', 'Z']:
        score += value(line)
    elif line == ['C', 'X']:
        score += value(line)
    elif line == ['C', 'Y']:
        score += value(line)
    elif line == ['C', 'Z']:
        score += value(line)

print(f"score for part 2: {score}")
