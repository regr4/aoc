"""day n"""

with open("input") as f:
    warehouse, moves = f.read().split("\n\n")
    warehouse = [list(l) for l in warehouse.splitlines()]
    moves = "".join(moves.splitlines())

for y, l in enumerate(warehouse):
    for x, c in enumerate(l):
        if c == "@":
            robot_pos = [x, y]
            break
    else:
        continue
    break


# updates its arguments
def make_move(warehouse, robot_pos, move):
    (rx, ry) = robot_pos
    match move:
        case "<":
            # does the robot have zero or more boxes to its left, followed by a space?
            # no bounds checking needed since the warehouse has a border.
            while warehouse[ry][rx] != "#":
                if warehouse[ry][rx] == ".":
                    break
                rx -= 1
            else:  # no break, so we hit the wall
                return

            # stupid, might need to optimize later.
            for i in range(rx, robot_pos[0]):
                warehouse[ry][i] = warehouse[ry][i + 1]

            warehouse[ry][robot_pos[0]] = "."
            robot_pos[0] -= 1
        case ">":
            while warehouse[ry][rx] != "#":
                if warehouse[ry][rx] == ".":
                    break
                rx += 1
            else:
                return

            for i in reversed(range(robot_pos[0] + 1, rx + 1)):
                warehouse[ry][i] = warehouse[ry][i - 1]

            warehouse[ry][robot_pos[0]] = "."
            robot_pos[0] += 1

        case "^":  # the positive y-axis is down!
            while warehouse[ry][rx] != "#":
                if warehouse[ry][rx] == ".":
                    break
                ry -= 1
            else:
                return

            for i in range(ry, robot_pos[1]):
                warehouse[i][rx] = warehouse[i + 1][rx]

            warehouse[robot_pos[1]][rx] = "."
            robot_pos[1] -= 1
        case "v":  # the positive y-axis is down!
            while warehouse[ry][rx] != "#":
                if warehouse[ry][rx] == ".":
                    break
                ry += 1
            else:
                return

            for i in reversed(range(robot_pos[1] + 1, ry + 1)):
                warehouse[i][rx] = warehouse[i - 1][rx]

            warehouse[robot_pos[1]][rx] = "."
            robot_pos[1] += 1


def disp_warehouse(w):
    print("\n".join("".join(line) for line in warehouse))


# disp_warehouse(warehouse)
for m in moves:
    # print(m)
    make_move(warehouse, robot_pos, m)
    # disp_warehouse(warehouse)

ans = 0
for y, l in enumerate(warehouse):
    for x, c in enumerate(l):
        if c == "O":
            ans += 100 * y + x

# part 1
print(f"part 1: {ans}")

# part 2
# print(f"part 2: {None}")
