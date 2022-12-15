"""day n"""

# common imports
import itertools
import re

with open("input") as f:
    inp = f.read().strip()

YVALUE = 2000000
MAX_COORD = 4000000

def manhattan_dist(v1, v2):
    return sum(abs(xi - yi) for (xi, yi) in zip(v1, v2))


coords = []
for l in inp.split("\n"):
    nums = []
    for m in re.findall(r"-?\d+", l):
        nums.append(int(m))

    [xs, ys, xb, yb] = nums
    coords.append(((xs, ys), (xb, yb)))

sensors_dists = {s: manhattan_dist(s, b) for (s, b) in coords}

# part 1

# inclusive
def excluded_interval(sensor, dist):
    (sx, sy) = sensor
    vertical_dist = abs(sy - YVALUE)
    horizontal_dist = dist - vertical_dist
    if horizontal_dist < 0:
        return None
    return (sx - horizontal_dist, sx + horizontal_dist)


intervals = []
for s, d in sensors_dists.items():
    if (xcl := excluded_interval(s, d)) is not None:
        intervals.append(xcl)

intervals.sort()

# remove overlap
ix = 0
while True:
    (currx, curry) = intervals[ix]
    (nextx, nexty) = intervals[ix + 1]

    if nexty <= curry:
        # remove whole next interval
        intervals.pop(ix + 1)
    elif nextx <= curry:
        # modify intervals
        intervals[ix] = (currx, nexty)
        intervals.pop(ix + 1)
    else:
        ix += 1
    if ix >= len(intervals) - 1:
        break

# print(intervals)

res = 0
for (x0, x1) in intervals:
    res += x1 - x0 + 1

res -= len(set(b for (s, b) in coords if b[1] == YVALUE))

print(f"part 1: {res}")

# part 2
def good_pos(x, y):
    for s, d in sensors_dists.items():
        if manhattan_dist((x, y), s) <= d:
            return False

    return True


# for s1, s2 in itertools.product(sensors_dists, sensors_dists):
#     if s1 == s2:
#         continue
#     if (sum(s1) - sum(s2)) % 2 != 0:
#         continue
#     # print(s1, s2)

#     # find manhattan intersection?

# the UNIQUE beacon must be on (/near?) the intersection of two 'circles' around sensors.
# or maybe bisect: can you quickly check a whole area is covered?
# divide into tiles and check which are entirely covered by a single beacon?
# let's try bisection


res = 0

tiles_to_check = [((0, 0), (MAX_COORD, MAX_COORD))]
# tiles_to_check = [((0, 0), (20, 20))]

tiles_excluded = 0
i = 0
while True:
    i += 1
    if i % 10000 == 0:
        print(f"{tiles_excluded / (MAX_COORD**2) * 100}")

    if not tiles_to_check:
        print("no solution found")
        break

    ((sx, sy), (ex, ey)) = tiles_to_check.pop()

    put_smaller = True
    for s, d in sensors_dists.items():
        if (
            max(
                *[
                    manhattan_dist(s, v)
                    for v in [(sx, sy), (sx, ey), (ex, sy), (ex, ey)]
                ]
            )
            <= d
        ):
            put_smaller = False

    if not put_smaller:
        tiles_excluded += (ex - sx) * (ey - sy)

    if put_smaller:
        if sx == ex and sy == ey:
            print(f"got it: {(sx, sy)}")
            res = sx * MAX_COORD + sy
            break

        if sx > ex:
            pass
        elif sy > ey:
            pass
        else:
            midpoint_x = (sx + ex) // 2
            midpoint_y = (sy + ey) // 2

            tiles_to_check.append(((sx, sy), (midpoint_x, midpoint_y)))
            tiles_to_check.append(((sx, midpoint_y + 1), (midpoint_x, ey)))
            tiles_to_check.append(((midpoint_x + 1, sy), (ex, midpoint_y)))
            tiles_to_check.append(((midpoint_x + 1, midpoint_y + 1), (ex, ey)))

# coord_max = 4000001
# # coord_max = 20
# steps = 100

# tiles = [[False] * (steps + 1) for _ in range(steps + 1)]

# step = coord_max // steps
# print(f"{coord_max = }\n{steps = }\n{step = }")
# for i in range(0, coord_max, step):
#     for j in range(0, coord_max, step):
#         i1 = i + step - 1
#         j1 = j + step - 1
#         for s, d in sensors_dists.items():
#             if (
#                 max(
#                     *[
#                         manhattan_dist(s, v)
#                         for v in [(i, j), (i, j1), (i1, j), (i1, j1)]
#                         # typo i1 instead of j1 cost me like 20 mins...
#                     ]
#                 )
#                 <= d
#             ):
#                 tiles[i // step][j // step] = True
#                 break

# # for row in tiles:
#     # for col in row:
#         # if col: print("1", end="")
#         # else: print("0", end="")
#     # print("")

# tiles_to_inspect = []

# for i, row in enumerate(tiles):
#     for j, col in enumerate(row):
#         if not col:
#             tiles_to_inspect.append((i, j))

# print(tiles_to_inspect)
# print(len(tiles_to_inspect))

print(f"part 2: {res}")
