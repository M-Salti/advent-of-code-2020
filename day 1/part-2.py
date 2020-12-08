with open("day 1/in", "r") as f:
    nums = list(map(int, f.read().split()))

for i in nums:
    for j in nums:
        if (2020 - i - j) in nums:
            print(i * j * (2020 - i - j))
            exit(0)
