from functools import reduce
from typing import List


def read_input(fn) -> List[str]:
    return open(fn, "r").read().split("\n\n")


def sum_counts_1(groups: List[str]):
    return sum(len(set(g) - set("\n")) for g in groups)


def sum_counts_2(groups: List[str]):
    return sum(len(reduce(lambda s1, s2: s1 & s2, map(set, g.split()))) for g in groups)


assert sum_counts_1(read_input("day 6/sample")) == 11
assert sum_counts_2(read_input("day 6/sample")) == 6
print(sum_counts_1(read_input("day 6/in")))
print(sum_counts_2(read_input("day 6/in")))
