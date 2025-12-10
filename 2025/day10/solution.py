"""day n"""

from dataclasses import dataclass
import functools
from pulp import *


@dataclass
class Problem:
    lamps: tuple[bool]
    buttons: tuple[frozenset[int]]
    joltages: tuple[int]


with open("input") as f:
    inp = [line.split() for line in f.read().splitlines()]

    problems = []
    for lamps, *buttons, joltages in inp:
        d = {}
        btns = []
        for button in buttons:
            btns.append(frozenset(int(n) for n in button[1:-1].split(",")))

        p = Problem(
            lamps=tuple(c == "#" for c in lamps[1:-1]),
            buttons=tuple(btns),
            joltages=tuple(int(n) for n in joltages[1:-1].split(",")),
        )
        problems.append(p)

total = 0
for prob in problems:
    lprob = LpProblem("my_problem", LpMinimize)
    variables = []
    for i in range(len(prob.buttons)):
        variables.append(LpVariable(f"v{i}", lowBound=0, cat="Integer"))

    for ix_j, joltage in enumerate(prob.joltages):
        lprob += (
            lpSum(
                var for ix_v, var in enumerate(variables) if ix_j in prob.buttons[ix_v]
            )
            == joltage
        )

    lprob += lpSum(var for var in variables)
    # would be nice to eliminate the spam, but I don't see anything in the docs
    lprob.solve()
    assert LpStatus[lprob.status] == "Optimal"
    total += value(lprob.objective)

print(f"part 2: {int(total)}")
