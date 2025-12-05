"""day n"""

# common imports

with open("input") as f:
    freshranges_, ingredients_ = f.read().split("\n\n")
    freshranges = [tuple(int(ing) for ing in line.split("-")) for line in freshranges_.splitlines()]
    ingredients = [int(l) for l in ingredients_.splitlines()]

freshranges.sort(key=lambda x: x[0])
deduped = [freshranges[0]]
for (lower, upper) in freshranges:
    lastlower, lastupper = deduped.pop()
    if lastupper >= lower:
        deduped.append((lastlower, max(upper, lastupper)))
    else:
        deduped.append((lastlower, lastupper))
        deduped.append((lower, upper))

# part 1
def fresh(deduped, ing):
    for l, u in reversed(deduped):
        if l <= ing:
            return ing <= u
    return False

ans = sum(1 for ing in ingredients if fresh(deduped, ing))
print(f"part 1: {ans}")

# part 2
ans = 0
for (l, u) in deduped:
    ans += u-l+1

print(f"part 2: {ans}")
