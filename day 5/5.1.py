def convert(s: str):
    row = s[:7].replace("F", "0").replace("B", "1")
    col = s[7:].replace("L", "0").replace("R", "1")
    return int(row, base=2) * 8 + int(col, base=2)


fn = "day 5/in"
print(max(convert(x) for x in open(fn, "r")))
