def convert(s: str) -> int:
    row = s[:7].replace("F", "0").replace("B", "1")
    col = s[7:].replace("L", "0").replace("R", "1")
    return int(row, base=2) * 8 + int(col, base=2)


def highest_seat_id(fn: str) -> int:
    return max(convert(x) for x in open(fn, "r"))


def seat_id(fn: str) -> int:
    ids = sorted(convert(x) for x in open(fn, "r"))
    for id1, id2 in zip(ids, ids[1:]):
        if id2 - id1 == 2:
            return id1 + 1


assert highest_seat_id("sample/day05.txt") == 820

print(highest_seat_id("input/day05.txt"))
print(seat_id("input/day05.txt"))
