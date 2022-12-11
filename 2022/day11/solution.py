"""day n"""

# common imports
from __future__ import annotations

import re
from typing import List, Callable
from dataclasses import dataclass
import functools
import math

with open("input") as f:
    inp = f.read()

per_monkey = [x.strip() for x in inp.split("\n\n")]


@dataclass
class Monkey:
    label: int
    items: List[int]
    operation: Callable[[int], int]
    test: int
    if_true: int
    if_false: int

    items_inspected: int = 0

    def throw_things(self, others: List[Monkey]):
        while self.items:
            self.items_inspected += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item //= 3

            others[
                self.if_true if item % self.test == 0 else self.if_false
            ].items.insert(1, item)

    def throw_things_pt_2(self, others: List[Monkey], M: int):
        while self.items:
            self.items_inspected += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item %= M  # this does not change any of the logic, but keeps the numbers from growing super big and slowing everything to a halt

            others[
                self.if_true if item % self.test == 0 else self.if_false
            ].items.insert(1, item)

    @staticmethod
    def parse_monkey(m: str) -> Monkey:
        [label, items, operation, test, if_true, if_false] = m.split("\n")
        op = re.search(r"new = (old (?:\+|\*) (?:old|\d+))", operation)
        return Monkey(
            get_ints(label)[0],
            get_ints(items),
            lambda old: eval(op.group(1)),  # evil
            get_ints(test)[0],
            get_ints(if_true)[0],
            get_ints(if_false)[0],
        )


# should put in a utils library
def get_ints(s: str) -> List[int]:
    return [int(m) for m in re.findall(r"\d+", s)]


# part 1

monkeys = [Monkey.parse_monkey(m) for m in per_monkey]
for _ in range(20):
    for monkey in monkeys:
        monkey.throw_things(monkeys)

l = sorted([m.items_inspected for m in monkeys], reverse=True)
business = l[0] * l[1]

print(f"part 1: {business}")

# part 2

monkeys = [Monkey.parse_monkey(m) for m in per_monkey]
tests = [m.test for m in monkeys]
# in 3.11 you can just use math.lcm(*tests)
# but i'm on 3.8 so i have to do this
M = math.prod(tests) // functools.reduce(math.gcd, tests)

for i in range(10000):
    for monkey in monkeys:
        monkey.throw_things_pt_2(monkeys, M)

l = sorted([m.items_inspected for m in monkeys], reverse=True)
business = l[0] * l[1]

print(f"part 2: {business}")
