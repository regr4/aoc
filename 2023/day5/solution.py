"""day n"""

# common imports
import re
from itertools import chain
from typing import List, Tuple

with open("input") as f:
    inp = f.read().splitlines()

seeds = [int(x) for x in re.findall("\\d+", inp[0])]

assignments = list(map(lambda x: [tuple(map(lambda x: int(m.group(x)),
                                       range(1,4))) for l in x.splitlines() if
                             (m := re.match("(\\d+) (\\d+) (\\d+)",
                                            l))],
                  "\n".join(inp[1:]).split("map")[1:]))

# part 1
def run_assignment(assignment, output):
    for (dstart, sstart, rlen) in assignment:
        if sstart <= output < sstart + rlen:
            return dstart + (output - sstart)
    return output

outputs = []
for seed in seeds:
    output = seed
    for assignment in assignments:
        output = run_assignment(assignment, output)
    outputs.append(output)


print(f"part 1: {min(filter(lambda x: x,outputs))}")

# part 2

parts = [seeds[i:i+2] for i in range(len(seeds)) if not i%2]

def range_intersection(I, J):
    a, b = I
    c, d = J
    lower = max(a, c)
    upper = min(b, d)
    if upper <= lower:
        return None
    return (lower, upper)

def range_difference(I, J):
    a, b = I
    isection = range_intersection(I, J)
    if not isection:
        return [I]
    c, d = isection
    res = []

    if a < c:
        res.append((a, c))

    if d < b:
        res.append((d, b))
    return res


def run_assignment_ranges(assignment, rang: Tuple[int, int]) -> List[Tuple[int, int]]:
    res = []
    unaccounted_parts = [rang]
    for (dstart, sstart, rlen) in assignment:
        new_unaccounted_parts = []
        for interval in unaccounted_parts:
            intersection = range_intersection(interval, (sstart, sstart+rlen))
            if not intersection:
                new_unaccounted_parts.append(interval)
                continue
            res.append(tuple(x-sstart+dstart for x in intersection))
            rest = range_difference(interval, intersection)
            new_unaccounted_parts.extend(rest)
        unaccounted_parts = new_unaccounted_parts
    res.extend(unaccounted_parts)
    return res

results = [(a, a+b) for a, b in parts]
for assignment in assignments:
    new_results = [run_assignment_ranges(assignment, x) for x in results]
    results = []
    for x in new_results:
        results.extend(x)

lowerbounds = [x[0] for x in results]

print(f"part 2: {min(lowerbounds)}")
