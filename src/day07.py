from typing import List
from collections import defaultdict
import regex
import graphviz


pattern = regex.compile(r"(.+) bags contain(?: (\d+) (.+?) bag[s]?[,.])*")


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
        self.dot = graphviz.Digraph(
            name="day07", format="png", graph_attr={"rankdir": "LR", "dpi": "300"}
        )

    def add_edge(self, u, v, w=None):
        """
        add a directed edge from u -> v, with weight w
        """
        self.adj[u] += [(v, int(w) if w else 0)]
        self.dot.edge(u, v, label=w)

    def subtree_size(self, u):
        self.visited = set()
        self._subtree_size(u)
        return len(self.visited)

    def _subtree_size(self, u):
        self.visited.add(u)
        for v, _ in self.adj[u]:
            if v not in self.visited:
                self._subtree_size(v)

    def num_nested_bags(self, u):
        num = 0
        for v, w in self.adj[u]:
            num += w + w * self.num_nested_bags(v)
        return num

    def render(self):
        self.dot.render()


def read_input(fn):
    with open(fn, "r") as f:
        return f.read().splitlines()


def count_containing_shiny_gold(rules: List[str]) -> int:
    g = Graph()
    for r in rules:
        m = pattern.match(r)
        (parent,) = m.captures(1)
        children = m.captures(3)

        for child in children:
            g.add_edge(child, parent)

    # g.render()

    return g.subtree_size("shiny gold") - 1


def size_shiny_gold(rules: List[str]) -> int:
    g = Graph()
    for r in rules:
        m = pattern.match(r)
        (parent,) = m.captures(1)
        nums, children = m.captures(2, 3)

        for child, num in zip(children, nums):
            g.add_edge(parent, child, num)

    # g.render()

    return g.num_nested_bags("shiny gold")


assert count_containing_shiny_gold(read_input("sample/day07_1.txt")) == 4
assert size_shiny_gold(read_input("sample/day07_1.txt")) == 32
assert size_shiny_gold(read_input("sample/day07_2.txt")) == 126

print(count_containing_shiny_gold(read_input("input/day07.txt")))
print(size_shiny_gold(read_input("input/day07.txt")))
