"""day n"""

# common imports
import re

with open("input") as f:
    inp = f.read().splitlines()

# part 1

cx = 0
cy = 0
for line in inp:
    num = int(re.findall('\d+', line)[0])
    match line[0]:
        case 'f':
            cx += num
        case 'd':
            cy += num
        case 'u':
            cy -= num


print(f"part 1: {cx*cy}")

# part 2
cx = 0
cy = 0
aim = 0
for line in inp:
    num = int(re.findall('\d+', line)[0])
    match line[0]:
        case 'f':
            cx += num
            cy += aim * num
        case 'd':
            aim += num
        case 'u':
            aim -= num


print(f"part 2: {cx*cy}")
