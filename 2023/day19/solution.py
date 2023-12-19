"""day n"""

# common imports
import collections
import itertools
import re

with open("input") as f:
    wfls_, ratings_ = f.read().split("\n\n")


Workflow = collections.namedtuple("Workflow", "label conditions otherwise")
Condition = collections.namedtuple("Condition", "var conds num then")
workflows = {}
for workflow in wfls_.splitlines():
    m = re.match(r"(\w+)\{((?:\w[<>]\d+:\w+,)+)(\w+)\}$", workflow)
    (label, cs, otherwise) = m.group(1, 2, 3)

    conds = []
    for c in cs.split(","):
        if not c:
            continue
        v, c, n, t = re.match(r"(\w)([<>])(\d+):(\w+)", c).group(1, 2, 3, 4)
        conds.append(Condition(v, c, int(n), t))
    workflows[label] = Workflow(label, conds, otherwise)

Rating = collections.namedtuple("Rating", "x m a s")
ratings = []
for rating in ratings_.splitlines():
    ratings.append(
        Rating(
            *map(
                int,
                re.match(r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}", rating).group(
                    1, 2, 3, 4
                ),
            )
        )
    )


# part 1
def rwf(part, wfs):
    # print('-'*100)
    # print(part)
    crule = "in"
    while True:
        r = wfs[crule]
        for v, c, n, t in r.conditions:
            ourv = getattr(part, v)
            # print(f"{(v,c,n,t)}")
            # print(ourv)
            satisfied = ourv < n if c == "<" else ourv > n
            assert c in "<>"
            if satisfied:
                if t == "A":
                    return True
                if t == "R":
                    return False
                crule = t
                break
        else:
            if r.otherwise == "A":
                return True
            if r.otherwise == "R":
                return False
            crule = r.otherwise


res = 0
for p in ratings:
    if rwf(p, workflows):
        res += p.x + p.m + p.a + p.s


print(f"part 1: {res}")

# part 2

Bounds = collections.namedtuple("Bounds", "lower upper")
BL = list[Bounds]


def is_empty(b: Bounds | BL):
    if isinstance(b, list):
        return not b or all(is_empty(x) for x in b)
    return all(a >= b for a, b in zip(b.lower, b.upper))


def intersect(l1, l2):
    def intersectb(a, b):
        return Bounds(
            Rating(max(x, y) for x, y in zip(a.lower, b.lower)),
            Rating(min(x, y) for x, y in zip(a.upper, b.upper)),
        )

    res = []
    for a, b in itertools.product(l1, l2):
        i = intersectb(a, b)
        if not is_empty(i):
            res.append(i)
    return res


def union(l1, l2):
    return l1 + l2


def inv(b, full=whole()):
    return []


def whole(ub=4000):
    lower = Rating([0] * 4)
    upper = Rating(*[ub + 1] * 4)
    return Bounds(lower, upper)


def from_c(v, c, n):
    ((lower, upper),) = whole()
    if c == "<":
        setattr(upper, v, n)
    elif c == ">":
        setattr(lower, v, n + 1)
    else:
        assert False
    return [Bounds(lower, upper)]


import functools


@functools.lru_cache(maxsize=100000)
def rwfinterval(interval, crule, wfs):
    if is_empty(interval):
        return []
    if crule == "A":
        return interval
    if crule == "R":
        return []

    res = []
    r = wfs[crule]
    civ = interval

    for v, c, n, t in r.conditions:
        satisfied_region = intersection(from_c(v, c, n), civ)
        if satisfied_region == civ:
            res.extend(rwfinterval(satisfied_region, t, wfs))
            continue
        if not satisfied_region:
            continue

        # some part satisfied, others not
        res.extend(rwfinterval(satisfied_region, t, wfs))
        civ = intersection(civ, inv(from_c(v, c, n)))

    return res


print(rwfinterval(whole, "mhk", whole()))


# G = {"A": set(), "R": set()}
# for wf in workflows.values():
#     G[wf.label] = {wf.otherwise} | {r.then for r in wf.conditions}

# import graphlib

# accepted: dict[str, BL] = {}
# for wfl in graphlib.TopologicalSorter(G).static_order():
#     if wfl == "A":
#         accepted[wfl] = [Bounds(Rating(0, 0, 0, 0), Rating(4001, 4001, 4001, 4001))]
#         continue
#     elif wfl == "R":
#         accepted[wfl] = []
#         continue

#     wf = workflows[wfl]
#     s = []

#     accepted[wfl] = s


print(f"part 2: {None}")
