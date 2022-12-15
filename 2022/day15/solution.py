"""day n"""

# common imports
import array
import re

with open("input") as f:
    inp = f.read().strip()

YVALUE = 2000000
MAX_COORD = 4000000


def manhattan_dist(v1, v2):
    (x1, x2) = v1
    (y1, y2) = v2
    return abs(x1-y1) + abs(x2-y2)


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

res = 0
for (x0, x1) in intervals:
    res += x1 - x0 + 1

res -= len(set(b for (s, b) in coords if b[1] == YVALUE))

print(f"part 1: {res}")

# part 2

res = 0
tiles_to_check_sx = array.array('l', [0])
tiles_to_check_sy = array.array('l', [0])
tiles_to_check_ex = array.array('l', [MAX_COORD])
tiles_to_check_ey = array.array('l', [MAX_COORD])

tiles_excluded = 0
i = 0

while True:
    i += 1
    if i % 100000 == 0:
        print(f"{tiles_excluded / (MAX_COORD**2) * 100}")

    if not tiles_to_check_sx:
        print("no solution found")
        break

    sx = tiles_to_check_sx.pop()
    sy = tiles_to_check_sy.pop()
    ex = tiles_to_check_ex.pop()
    ey = tiles_to_check_ey.pop()

    # is there any sensor that eliminates the entire tile? then False.
    # faster than nested for loops, apparently
    # eliminated itertools.product because this seems to be slightly faster
    put_smaller = not any(
        all(manhattan_dist(s, v) <= d for v in [(sx, sy), (sx, ey), (ex, sy), (ex, ey)])
        for s, d in sensors_dists.items()
    )

    if not put_smaller:
        tiles_excluded += (ex - sx) * (ey - sy)

    if put_smaller:
        if sx == ex and sy == ey:
            print(f"got it: {(sx, sy)}")
            res = sx * MAX_COORD + sy
            break

        if sx <= ex and sy <= ey:
            midpoint_x = (sx + ex) // 2
            midpoint_y = (sy + ey) // 2

            tiles_to_check_sx.fromlist([sx, sx, midpoint_x+1, midpoint_x+1])
            tiles_to_check_sy.fromlist([sy, midpoint_y+1, sy, midpoint_y+1])
            tiles_to_check_ex.fromlist([midpoint_x, midpoint_x, ex, ex])
            tiles_to_check_ey.fromlist([midpoint_y, ey, midpoint_y, ey])

print(f"part 2: {res}")
