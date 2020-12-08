with open("day 1/in", "r") as f:
    nums = list(map(int, f.read().split()))

for i in nums:
    if (2020 - i) in nums:
        print(i * (2020 - i))
        break
