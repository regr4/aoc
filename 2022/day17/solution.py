"""day n"""

# common imports
from dataclasses import dataclass
import itertools
import re

with open("input") as f:
    inp = f.read().strip()



Rock = list[list[bool]]

rock_diagrams = [
    "####",
    ".#.\n###\n.#.",
    "..#\n..#\n###",
    "#\n#\n#\n#",
    "##\n##",
]


def read_rock_diagram(s):
    res = []
    for line in s.split('\n'):
        res.append([])
        for c in line:
            if c == "#":
                res[-1].append(True)
            else:
                res[-1].append(False)
    return res

def display_rock(r):
    for line in r:
        print("".join(map(lambda b: "#" if b else ".", line)))


rocks = [read_rock_diagram(x) for x in rock_diagrams]

@dataclass
class State:
    board: list[list[bool]]
    current_rock: Rock
    rock_position: tuple[int, int]
    # x position of left edge, y position of bottom edge

    @staticmethod
    def new_empty() -> State:
        return State([], rocks[0], (0,1))

    def introduce_rock(self, rock: Rock):
        self.current_rock = rock
        y = len(self.board)
        self.rock_position = (2, y+3)

    def run_step_has_landed(self, gas_direction: bool) -> bool:
        return False

    def debug_print(self):
        ...


state = State.new_empty()

ix = 0
for rock in itertools.cycle(rocks):
    state.introduce_rock(rock)
    gas_direction = inp[ix] == ">"
    if state.run_step_has_landed(gas_direction):

        continue
    ix += 1


# part 1
print(f"part 1: {None}")

#part 2
print(f"part 2: {None}")
