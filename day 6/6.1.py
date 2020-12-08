fn = "day 6/in"
print(
    sum(
        len(set("".join(group.split()))) for group in open(fn, "r").read().split("\n\n")
    )
)
