"""day 4"""

with open("input") as f:
    input = f.read()

import re
regex = re.compile(r"(?P<f0>\d+)-(?P<f1>\d+),(?P<s0>\d+)-(?P<s1>\d+)")

res = 0
for (f0, f1, s0, s1) in regex.findall(input):
    f0, f1, s0, s1 = int(f0), int(f1), int(s0), int(s1)
    if f0 <= s0 <= s1 <= f1 or s0 <= f0 <= f1 <= s1:
        res += 1

print(f"part 1: {res}")

res = 0
for (f0, f1, s0, s1) in regex.findall(input):
    f0, f1, s0, s1 = int(f0), int(f1), int(s0), int(s1)
    r1 = range(f0, f1 + 1)
    r2 = range(s0, s1 + 1)

    for x in r1:
        if x in r2:
            res +=1
            break
    for x in r2:
        if x in r1:
            res += 1
            break

res /= 2
print(f"part 2: {res}")
