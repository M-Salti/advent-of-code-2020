from collections import Counter, defaultdict
from functools import lru_cache
from graphviz import Digraph


def part_1(fn):
    """
    What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
    """
    with open(fn, "r") as f:
        adapters = sorted(map(int, f.read().splitlines()))

    adapters = [0] + adapters + [adapters[-1] + 3]

    diffs = Counter()

    for cur, nxt in zip(adapters[:-1], adapters[1:]):
        diffs[nxt - cur] += 1

    return diffs[1] * diffs[3]


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.dot = Digraph(format="png", directory="day 10")

    def add_edge(self, u, v):
        """
        add a directed edge from u -> v
        """
        self.adj[u].append(v)
        self.dot.edge(u, v)

    @lru_cache
    def count_ways(self, u):
        num_ways = 0
        for v in self.adj[u]:
            num_ways += self.count_ways(v)
        num_ways = max(num_ways, 1)
        return num_ways


def part_2(fn):
    """
    What is the total number of distinct ways you can arrange the adapters to
    connect the charging outlet to your device?
    """
    with open(fn, "r") as f:
        adapters = sorted(map(int, f.read().splitlines()))
    adapters = [0] + adapters + [adapters[-1] + 3]

    g = Graph()
    for i in range(len(adapters)):
        for j in range(i + 1, len(adapters)):
            if adapters[j] - adapters[i] <= 3:
                g.add_edge(str(adapters[i]), str(adapters[j]))

    # g.dot.render()

    return g.count_ways("0")


assert part_1(fn="sample/day10_1.txt") == 7 * 5
assert part_1(fn="sample/day10_2.txt") == 22 * 10

assert part_2(fn="sample/day10_1.txt") == 8
assert part_2(fn="sample/day10_2.txt") == 19208

print(part_1(fn="input/day10.txt"))
print(part_2(fn="input/day10.txt"))
