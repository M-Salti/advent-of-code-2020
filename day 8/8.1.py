import unittest


def solve(fn: str):
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


class TestSample(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve("day 8/sample"), 5)


print(solve("day 8/in"))
unittest.main()
