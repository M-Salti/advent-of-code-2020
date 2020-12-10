fn = "day 9/in"
pre_len = 25

with open(fn, "r") as f:
    nums = list(map(int, f.read().splitlines()))


def find_invalid_number():
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


def find_range():
    invalid = find_invalid_number()
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

    return queue

rng = find_range()
rng = sorted(rng)
print(rng[0] + rng[-1])
