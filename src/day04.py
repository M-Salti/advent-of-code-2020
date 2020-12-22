from re import match
from typing import List


def read_input(fn: str) -> List[str]:
    with open(fn, "r") as f:
        return f.read().split("\n\n")


def count_valid_passports(data: List[str]) -> int:
    fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])  # omit cid

    valid_passports = 0
    for passport in data:
        entries = passport.split()
        entries = set(map(lambda e: e.split(":")[0], entries))
        valid_passports += entries & fields == fields

    return valid_passports


def validate(passport: dict):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    rules = {
        "byr": lambda x: match(r"\d{4}$", x) and 1920 <= int(x) <= 2002,
        "iyr": lambda x: match(r"\d{4}$", x) and 2010 <= int(x) <= 2020,
        "eyr": lambda x: match(r"\d{4}$", x) and 2020 <= int(x) <= 2030,
        # "hgt": lambda x: match(r"\d+(cm|in)$", x) and ((150 <= int(x[:-2]) <= 193) if x[-2:] == "cm" else (59 <= int(x[:-2]) <= 76)),
        "hgt": lambda x: (match(r"\d+cm$", x) and 150 <= int(x[:-2]) <= 193)
        or (match(r"\d+in$", x) and 59 <= int(x[:-2]) <= 76),
        "hcl": lambda x: match(r"#[0-9,a-f]{6}$", x),
        "ecl": lambda x: x in eye_colors,
        "pid": lambda x: match(r"\d{9}$", x),
        "cid": lambda _: True,
    }

    for field, value in passport.items():
        if not rules[field](value):
            return False

    return True


def count_valid_passports_2(data: List[str]) -> int:
    fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])  # omit cid

    valid_passports = 0
    for passport in data:
        entries = passport.split()
        entries = dict(map(lambda e: tuple(e.split(":")), entries))
        if entries.keys() & fields == fields:
            valid_passports += validate(entries)

    return valid_passports


assert count_valid_passports(read_input("sample/day04_1.txt")) == 2
print(count_valid_passports(read_input("input/day04.txt")))

assert count_valid_passports_2(read_input("sample/day04_1.txt")) == 2
assert count_valid_passports_2(read_input("sample/day04_2.txt")) == 4
assert count_valid_passports_2(read_input("sample/day04_3.txt")) == 0
print(count_valid_passports_2(read_input("input/day04.txt")))
