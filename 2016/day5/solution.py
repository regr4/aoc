"""day n"""

import hashlib
import itertools

with open("input") as f:
    inp = f.read().strip()

pw1 = ""
pw2 = [""] * 8
visited = [False] * 8
for i in itertools.count():
    if i % 1000000 == 0:
        print(i)
    digest = hashlib.md5(bytes(inp + str(i), encoding="ascii")).digest().hex()
    if digest[:5] == "00000":
        print(f"found one: {i}")

        # part 1
        if len(pw1) < 8:
            pw1 += digest[5]

        # part 2
        pos = int(digest[5], base=16)
        value = digest[6]
        if pos < 8 and not visited[pos]:
            pw2[pos] = value
            visited[pos] = True

        # have we found enough?
        if all(visited) and len(pw1) == 8:
            break

print(f"part 1: {pw1}")
ans = "".join(pw2)
print(f"part 2: {ans}")
