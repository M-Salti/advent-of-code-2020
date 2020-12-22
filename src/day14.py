from typing import Dict


def task1(fn: str):
    mask = ""
    memory: Dict[int, int] = dict()

    for line in open(fn, "r"):
        lhs, rhs = line.strip().split(" = ")
        if lhs == "mask":
            mask = rhs
        else:
            address = int(lhs[4:-1])
            value = int(rhs)
            for idx, bit in enumerate(reversed(mask)):
                if bit == "1":
                    value |= 1 << idx
                elif bit == "0":
                    value &= ~(1 << idx)
            memory[address] = value

    return sum(memory.values())


def task1_v2(fn: str):
    mask = ""
    memory: Dict[int, int] = dict()

    for line in open(fn, "r"):
        lhs, rhs = line.strip().split(" = ")
        if lhs == "mask":
            mask = rhs
        else:
            address = int(lhs[4:-1])
            value = f"{int(rhs):036b}"  # convert to binary string
            for idx, bit in enumerate(mask):
                if bit != "X":
                    value = value[:idx] + bit + value[idx + 1 :]
            memory[address] = int(value, 2)

    return sum(memory.values())


def task2(fn):
    mask = ""
    memory: Dict[int, int] = dict()

    for line in open(fn, "r"):
        lhs, rhs = line.strip().split(" = ")
        if lhs == "mask":
            mask = rhs
        else:
            address = f"{int(lhs[4:-1]):036b}"
            value = int(rhs)
            for idx, bit in enumerate(mask):
                if bit != "0":
                    address = address[:idx] + bit + address[idx + 1 :]

            x_pows = [
                (1 << idx) for idx, bit in enumerate(reversed(address)) if bit == "X"
            ]
            possible_additions = [0]
            for p in x_pows:
                adds = [p + a for a in possible_additions]
                possible_additions += adds

            address = int(address.replace("X", "0"), 2)
            for a in possible_additions:
                memory[address + a] = value

    return sum(memory.values())


assert task1("day 14/sample") == 165
print(task1("day 14/in"))

assert task1_v2("day 14/sample") == 165
print(task1_v2("day 14/in"))

assert task2("day 14/sample2") == 208
print(task2("day 14/in"))
