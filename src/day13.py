from typing import List, Tuple
from math import ceil
from operator import itemgetter


def read_input(fn: str) -> Tuple[int, str]:
    with open(fn, "r") as f:
        timestamp, ids = f.read().splitlines()
    return int(timestamp), ids


def find_earliest_bus(timestamp: int, ids) -> int:
    ids = list(map(int, filter(str.isnumeric, ids.split(","))))
    times = [ceil(timestamp / id) * id - timestamp for id in ids]
    earliest = min(times)
    return earliest * ids[times.index(earliest)]


def check_coprimality(L: List[int]) -> bool:
    for idx, i in enumerate(L):
        for j in L[idx + 1 :]:
            if i % j == 0 or j % i == 0:
                return False
    return True


def chinese_remainder_theorem_solver(equations: List[Tuple[int, int]]) -> int:
    """
    equations = [(a_1, n_1), (a_2, n_2), ..., (a_m, n_m)]
    we want to find x, such that:
    x === a_1 (mod n_1)
    x === a_2 (mod n_2)
    .
    .
    .
    x === a_m (mod n_m)

    This solution uses the search by sieving method (https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving)

    x_(i+1) = x_i + k * (n1 * n2 * ... * n_i)
    x_0 = a_1
    """
    if not check_coprimality(list(list(zip(*equations))[1])):
        raise Exception("n_i are not coprime. No solution exists.")

    equations.sort(key=itemgetter(1), reverse=True)

    x, N = equations[0]  # x = a_1, N = n1 * n2 * ...
    for a, n in equations[1:]:
        while True:
            if x % n == a:
                N *= n
                break
            else:
                x += N
    return x


def find_earliest_timestamp(ids: str) -> int:
    equations = [
        (-idx % int(val), int(val))
        for idx, val in enumerate(ids.split(","))
        if val != "x"
    ]
    return chinese_remainder_theorem_solver(equations)


assert find_earliest_bus(*read_input("day 13/sample")) == 295
print(find_earliest_bus(*read_input("day 13/in")))

assert find_earliest_timestamp(read_input("day 13/sample")[1]) == 1068781
assert find_earliest_timestamp("17,x,13,19") == 3417
assert find_earliest_timestamp("67,7,59,61") == 754018
assert find_earliest_timestamp("67,x,7,59,61") == 779210
assert find_earliest_timestamp("67,7,x,59,61") == 1261476
assert find_earliest_timestamp("1789,37,47,1889") == 1202161486
print(find_earliest_timestamp(read_input("day 13/in")[1]))
