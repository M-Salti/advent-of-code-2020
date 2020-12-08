from itertools import accumulate


fn = "day 6/in"

print(
    sum(
        len(list(accumulate(map(set, g.split()), lambda s1, s2: s1 & s2))[-1])
        for g in open(fn, "r").read().split("\n\n")
    )
)
