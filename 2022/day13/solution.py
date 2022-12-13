"""day n"""

# common imports
import functools
import itertools

with open("input") as f:
    inp = f.read().strip()


Ordering = int
less = -1
eq = 0
more = 1


def compare_list(list1, list2) -> Ordering:
    list1list = isinstance(list1, list)
    list2list = isinstance(list2, list)
    if list1list and list2list:
        for i in itertools.count():
            i_in_list1 = i in range(len(list1))
            i_in_list2 = i in range(len(list2))
            if i_in_list1 and i_in_list2:
                if (c := compare_list(list1[i], list2[i])) != eq:
                    return c
            elif i_in_list1 and not i_in_list2:
                return more
            elif not i_in_list1 and i_in_list2:
                return less
            else:
                # lists are of equal length and contain identical elements
                return eq

    if list1list and not list2list:
        return compare_list(list1, [list2])
    if not list1list and list2list:
        return compare_list([list1], list2)
    # numbers
    if list1 < list2:
        return less
    if list1 == list2:
        return eq
    if list1 > list2:
        return more
    raise Exception("this should never happen")


# part 1
pairs = [tuple(eval(x) for x in a.split("\n")) for a in inp.split("\n\n")]
res = 0
for i, pair in enumerate(pairs, start=1):
    if compare_list(*pair) != more:
        res += i

print(f"part 1: {res}")

# part 2
things = [eval(a) for a in inp.split("\n") if a] + [[[2]], [[6]]]
things.sort(key=functools.cmp_to_key(compare_list))
res = (things.index([[2]]) + 1) * (things.index([[6]]) + 1)

print(f"part 2: {res}")
