from typing import List


def read_input(fn: str):
    with open(fn, "r") as f:
        return list(map(int, f.read().split()))


def find_product(nums: List[int]):
    for i in nums:
        if (2020 - i) in nums:
            return i * (2020 - i)


def find_product_3(nums: List[int]):
    for i in nums:
        for j in nums:
            if (2020 - i - j) in nums:
                return i * j * (2020 - i - j)


assert find_product(read_input("sample/day01.txt")) == 514579
print(find_product(read_input("input/day01.txt")))

assert find_product_3(read_input("sample/day01.txt")) == 241861950
print(find_product_3(read_input("input/day01.txt")))
