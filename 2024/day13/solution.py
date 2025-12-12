"""day n"""

from dataclasses import dataclass
import numpy as np
import numpy.typing
import scipy as sp
import re


@dataclass
class Problem:
    buttonA: np.typing.ArrayLike
    buttonB: np.typing.ArrayLike
    prizeLocation: np.typing.ArrayLike

    costA: int = 3
    costB: int = 1

    def solvept1(self):
        best = float("inf")
        for num_a in range(101):
            for num_b in range(101):
                if np.all(  # TODO
                    np.abs(
                        (
                            num_a * self.buttonA
                            + num_b * self.buttonB
                            - self.prizeLocation
                        )
                    )
                    < 1e-6
                ):
                    best = min(best, self.costA * num_a + self.costB * num_b)
        return best if best < 1e10 else 0

    def solvept2(self):
        actualPrizeLocation = 10000000000000 + self.prizeLocation

        sol = sp.optimize.milp(
            c=np.array((self.costA, self.costB)),
            integrality=np.ones(2),
            constraints=sp.optimize.LinearConstraint(
                np.column_stack((self.buttonA, self.buttonB)),
                lb=actualPrizeLocation,
                ub=actualPrizeLocation,
            ),
        )
        if sol.status == 2:
            print("infeasible")
            return 0
        else:
            assert(sol.success)
            print(sol.fun)
            return int(sol.fun)


def getints(s):
    return np.array([int(x) for x in re.findall(r"-?\d+", s)])


def parse_prob(prob):
    btna, btnb, prize = map(getints, prob.splitlines())
    return Problem(btna, btnb, prize)


with open("input") as f:
    inp = [parse_prob(line) for line in f.read().split("\n\n")]

# ans = sum(prob.solvept1() for prob in inp)

# part 1
# print(f"part 1: {ans}")

print(sum(prob.solvept2() for prob in inp))

# part 2


print(f"part 2: {None}")
