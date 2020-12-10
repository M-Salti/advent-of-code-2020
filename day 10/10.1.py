from collections import Counter


def solve(fn):
    with open(fn, "r") as f:
        adapters = sorted(map(int, f.read().splitlines()))

    adapters = [0] + adapters + [adapters[-1] + 3]

    diffs = Counter()

    for cur, nxt in zip(adapters[:-1], adapters[1:]):
        diffs[nxt - cur] += 1

    return diffs[1] * diffs[3]


assert solve(fn="day 10/sample") == 7 * 5
assert solve(fn="day 10/sample2") == 22 * 10
print(solve(fn="day 10/in"))
