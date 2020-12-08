import regex
import graphviz


class Graph:
    def __init__(self):
        self.adj = dict()
        self.dot = graphviz.Digraph(format="png", graph_attr={"rankdir": "LR", "dpi": "300"}, directory="day 7")

    def add_edge(self, u, v, w=None):
        """
        add a directed edge from u -> v, with weight w
        """
        self.adj[u] = self.adj.get(u, []) + [(v, int(w))]
        self.dot.edge(u, v, label=w)

    def num_nested_bags(self, u):
        num = 0
        for v, w in self.adj.get(u, []):
            num += w + w * self.num_nested_bags(v)
        return num

    def render(self):
        self.dot.render()


fn = "day 7/in"
with open(fn, "r") as f:
    rules = f.read().splitlines()

pattern = r"(.+) bags contain(?: (\d+) (.+?) bag[s]?[,.])*"
pattern = regex.compile(pattern)

g = Graph()

for r in rules:
    m = pattern.match(r)
    parent, = m.captures(1)
    nums, children = m.captures(2, 3)

    for child, num in zip(children, nums):
        g.add_edge(parent, child, num)


print(g.num_nested_bags("shiny gold"))
# g.render()
