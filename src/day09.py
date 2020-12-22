from typing import List


def read_input(fn) -> List[int]:
    with open(fn, "r") as f:
        return list(map(int, f.read().splitlines()))


pre_len = 25


def find_invalid_number(nums: List[int]) -> int:
    for i in range(pre_len, len(nums)):
        found = False
        for j in range(i - pre_len, i):
            for k in range(j + 1, i):
                if nums[i] == nums[j] + nums[k]:
                    found = True
                    break
            if found:
                break
        if not found:
            return nums[i]
    return -1


def find_range(nums: List[int]) -> int:
    invalid = find_invalid_number(nums)
    index = 0
    queue = []
    qsum = 0

    while True:
        if qsum == invalid:
            break
        if qsum > invalid:
            qsum -= queue[0]
            queue.pop(0)
        if qsum < invalid:
            queue.append(nums[index])
            qsum += queue[-1]
            index += 1

    rng = sorted(queue)
    return rng[0] + rng[-1]


pre_len = 5
assert find_invalid_number(read_input("sample/day09.txt")) == 127
assert find_range(read_input("sample/day09.txt")) == 62

pre_len = 25
print(find_invalid_number(read_input("input/day09.txt")))
print(find_range(read_input("input/day09.txt")))
