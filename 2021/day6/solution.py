"""day n"""

with open("input") as f:
    inp = f.read().strip().split(",")

school = [0] * 9
for i in map(int, inp):
    school[i] += 1


def step_school(s: list[int], days: int):
    for _ in range(days):
        zeros = s[0]
        s[0:] = s[1:]
        s.append(zeros)
        s[6] += zeros


# part 1
step_school(school, 80)
print(f"part 1: {sum(school)}")

# part 2
step_school(school, 256 - 80)
print(f"part 2: {sum(school)}")
