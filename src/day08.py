from graphviz import Digraph


class disjoint_sets:
    def __init__(self, n: int) -> None:
        super().__init__()
        self.p = [-1] * n
        self.num_sets = n

    def find(self, x: int) -> int:
        if self.p[x] < 0:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.p[x] > self.p[y]:
            x, y = y, x
        self.p[x] += self.p[y]
        self.p[y] = x
        self.num_sets -= 1
        return True

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def size(self, x: int) -> int:
        return -self.p[self.find(x)]


class Solution:
    def __init__(self, fn):
        with open(fn, "r") as f:
            self.instructions = f.read().splitlines()
        self.program_length = len(self.instructions)
        self.dot = Digraph(
            name="day08", format="svg", graph_attr={"rankdir": "LR", "dpi": "55"}
        )
        self.dsu = disjoint_sets(self.program_length + 1)

        self.build_graph()

    def build_graph(self):
        for index in range(self.program_length):
            op, arg = self.instructions[index].split()
            increment = int(arg) if op == "jmp" else 1

            label = f"{index + 1}"
            nxt_label = f"{index + 1 + increment}"

            nxt_index = index + increment

            if nxt_index >= self.program_length:
                nxt_label = "X"
                nxt_index = self.program_length

            self.dot.edge(label, nxt_label)
            self.dsu.unite(index, nxt_index)

    def render(self):
        self.dot.render()

    def find_bad_instruction(self, index=0) -> int:
        op, arg = self.instructions[index].split()

        if op == "jmp" and self.dsu.same(index + 1, self.program_length):
            return index
        if op == "nop" and self.dsu.same(index + int(arg), self.program_length):
            return index

        return self.find_bad_instruction(index + (int(arg) if op == "jmp" else 1))

    def solve(self):
        index = self.find_bad_instruction()
        op, arg = self.instructions[index].split()
        self.instructions[index] = f'{"jmp" if op == "nop" else "nop"} {arg}'

        counter = 0
        acc = 0
        while counter < self.program_length:
            op, arg = self.instructions[counter].split()
            if op == "acc":
                acc += int(arg)
                counter += 1
            elif op == "jmp":
                counter += int(arg)
            elif op == "nop":
                counter += 1

        return acc


def calc_accumulater(fn: str) -> int:
    with open(fn) as f:
        instructions = f.read().splitlines()

    visited = [False] * len(instructions)
    acc = 0
    counter = 0  # program counter

    while True:
        if visited[counter]:
            break
        visited[counter] = True

        op, arg = instructions[counter].split()
        if op == "acc":
            acc += int(arg)
            counter += 1
        elif op == "jmp":
            counter += int(arg)
        elif op == "nop":
            counter += 1

    return acc


assert calc_accumulater("sample/day08.txt") == 5
sample = Solution("sample/day08.txt")
assert sample.solve() == 8
sample.render()

print(calc_accumulater("input/day08.txt"))
solution  = Solution("input/day08.txt")
print(solution.solve())
