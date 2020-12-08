def convert(s: str):
    row = s[:7].replace("F", "0").replace("B", "1")
    col = s[7:].replace("L", "0").replace("R", "1")
    return int(row, base=2) * 8 + int(col, base=2)


fn = "day 5/in"
ids = sorted(convert(x) for x in open(fn, "r"))

for id1, id2 in zip(ids, ids[1:]):
    if id2 - id1 == 2:
        print(id1 + 1)