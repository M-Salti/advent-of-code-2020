from collections import defaultdict
from functools import lru_cache
from graphviz import Digraph


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


def solve(fn):
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


assert solve(fn="day 10/sample") == 8
assert solve(fn="day 10/sample2") == 19208
print(solve(fn="day 10/in"))
