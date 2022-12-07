"""day n"""

# common imports
import re
from typing import List, Dict, Any

with open("input") as f:
    inp = f.read()

# part 1
curr_path: List[str] = []
dir_tree: Dict[str, Any] = {}


def idx(tree, path):
    curr_tree = tree
    for seg in path:
        if seg not in curr_tree:
            curr_tree[seg] = {}
        curr_tree = curr_tree[seg]
    return curr_tree


for line in inp.split("\n"):
    if not line:
        continue

    if line == "$ cd /":
        curr_path = []
    elif line == "$ cd ..":
        curr_path.pop()
    elif m := re.match(r"^\$ cd (\w+)$", line):
        arg = m[1]
        curr_path.append(arg)
    elif m := re.match(r"^\$ ls$", line):
        pass  # do nothing
    elif m := re.match(r"(\d+) ((?:\w|\.)+)", line):
        name = m[2]
        idx(dir_tree, curr_path)[name] = m[1]
    elif m := re.match(r"dir \w+", line):
        pass  # do nothing
    else:
        print(line, "didnt recognise")
        break

# print(dir_tree)
def walk_tree(dir_tree, output) -> int:
    dir_size = 0
    for (name, contents) in dir_tree.items():
        if type(contents) is dict:
            output[name] = {}
            dir_size += walk_tree(contents, output[name])
            # print(name, "is dict")
        else:
            size = int(contents)
            dir_size += size
            # print(f"{name} is file of size {size}")
    output["size"] = dir_size
    return dir_size


dir_tree2: Dict[str, Any] = {}

walk_tree(dir_tree, dir_tree2)

# print(dir_tree2)

res = 0


def add_up_sizes(tree):
    global res
    for (name, subdir) in tree.items():
        if name == "size":
            continue
        if (size := subdir["size"]) <= 100000:
            res += size
        add_up_sizes(subdir)


add_up_sizes(dir_tree2)

print(f"part 1: {res}")

# part 2
res = 100000000000000000  # large enough

used_size = dir_tree2["size"]
need_to_free = used_size - (70000000 - 30000000)


def find_smallest(tree):
    global res
    for (name, subdir) in tree.items():
        if name == "size":
            continue
        if (size := subdir["size"]) >= need_to_free:
            res = min(res, size)
        find_smallest(subdir)


find_smallest(dir_tree2)

print(f"part 2: {res}")
