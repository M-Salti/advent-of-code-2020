fn = "day 9/in"
pre_len = 25

with open(fn, "r") as f:
    nums = list(map(int, f.read().splitlines()))

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
        print(nums[i])
        break
