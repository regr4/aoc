"""day n"""

# common imports
import collections
import re

with open("input") as f:
    inp = f.read().splitlines()

# Node: list("typ label targets data")

TYPE = 0
LABEL = 1
TARGETS = 2
DATA = 3

LOW = False
HIGH = True

nodes: dict[str, list] = {}
for line in inp:
    if m := re.match(r"broadcaster -> (?P<targets>(?:\w+, )*\w+)$", line):
        nodes["broadcaster"] = ["b", "broadcaster", m.group("targets").split(", "), None]
    elif m := re.match(r"(?P<type>%|&)(?P<label>\w+) -> (?P<targets>(?:\w+, )*\w+)$", line):
        nodes[m.group("label")] = [m.group("type"), m.group("label"), m.group("targets").split(", "), False if m.group("type") == "%" else {}]
    else:
        print("OH NO")
        print(line)
        assert False


for k,v in nodes.items():
    print(str(k) + ": " + str(v))


for k,v in nodes.items():
    for t in v[TARGETS]:
        if not t in nodes:
            print(t)
            continue
        if nodes[t][TYPE] == "&":
            nodes[t][DATA][k] = LOW




Signal = collections.namedtuple("Signal", "dest level src")

q = collections.deque([Signal("broadcaster", LOW, "None")])
while q:
    sig = q.popleft()
    node = nodes[sig.dest]
    match node[TYPE]:
        case "b":
            q.extend(Signal(t, LOW, sig.dest) for t in node[TARGETS])
        case "%":
            if sig.level == HIGH:
                continue
            node[DATA] = not node[DATA]
            q.extend(Signal(t, node[DATA], sig.dest) for t in node[TARGETS])
        case "&":
            node[DATA][sig.src] = sig.level
            
            
            
                


# part 1
print(f"part 1: {None}")

# part 2
print(f"part 2: {None}")
