from collections import Counter
from typing import List


def read_input(fn: str) -> List[str]:
    with open(fn, "r") as f:
        return list(map(str.strip, f.readlines()))


def count_valid_passwords(lines: List[str]) -> int:
    valid = 0
    for line in lines:
        freq, char, password = line.split()
        mn, mx = map(int, freq.split("-"))
        pcount = Counter(password)
        valid += mn <= pcount[char[0]] <= mx

    return valid


def count_valid_passwords_2(lines: List[str]) -> int:
    valid = 0
    for line in lines:
        pos, char, password = line.split()
        char = char[0]
        first, second = map(int, pos.split("-"))
        valid += (password[first - 1] == char) ^ (password[second - 1] == char)
    
    return valid


assert count_valid_passwords(read_input("sample/day02.txt")) == 2
assert count_valid_passwords_2(read_input("sample/day02.txt")) == 1

print(count_valid_passwords(read_input("input/day02.txt")))
print(count_valid_passwords_2(read_input("input/day02.txt")))
