import regex
import graphviz


class Graph:
    def __init__(self):
        self.adj = dict()
        self.dot = graphviz.Digraph(format="png", graph_attr={"rankdir": "LR"})

    def add_edge(self, u, v):
        """
        add a directed edge from u -> v
        """
        self.adj[u] = self.adj.get(u, []) + [v]
        self.dot.edge(u, v)

    def subtree_size(self, u):
        self.visited = set()
        self._subtree_size(u)
        return len(self.visited)

    def _subtree_size(self, u):
        self.visited.add(u)
        for v in self.adj.get(u, []):
            if v not in self.visited:
                self._subtree_size(v)

    def render(self):
        self.dot.render()


fn = "day 7/in"
with open(fn, "r") as f:
    rules = f.read().splitlines()

pattern = r"(.+) bags contain (?:(\d+) (.+?) bag(?:s?)(?:, |.$))*"

g = Graph()

for r in rules:
    m = regex.match(pattern, r)
    parent = m.captures(1)[0]
    children = m.captures(3)

    for child in children:
        g.add_edge(child, parent)


print(g.subtree_size("shiny gold") - 1)
