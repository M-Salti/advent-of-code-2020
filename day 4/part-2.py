from re import match


fn = "day 4/in"
with open(fn, "r") as f:
    data = f.read().split("\n\n")

fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])  # omit cid


def validate(passport: dict):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    rules = {
        "byr": lambda x: match("\d{4}$", x) and 1920 <= int(x) <= 2002,
        "iyr": lambda x: match("\d{4}$", x) and 2010 <= int(x) <= 2020,
        "eyr": lambda x: match("\d{4}$", x) and 2020 <= int(x) <= 2030,
        # "hgt": lambda x: match("\d+(cm|in)$", x) and ((150 <= int(x[:-2]) <= 193) if x[-2:] == "cm" else (59 <= int(x[:-2]) <= 76)),
        "hgt": lambda x: (match("\d+cm$", x) and 150 <= int(x[:-2]) <= 193)
                      or (match("\d+in$", x) and 59 <= int(x[:-2]) <= 76),
        "hcl": lambda x: match("#[0-9,a-f]{6}$", x),
        "ecl": lambda x: x in eye_colors,
        "pid": lambda x: match("\d{9}$", x),
        "cid": lambda _: True
    }

    for field, value in passport.items():
        if not rules[field](value):
            return False
    
    return True


valid_passports = 0
for passport in data:
    entries = passport.split()
    entries = dict(map(lambda e: tuple(e.split(":")), entries))
    if entries.keys() & fields == fields:
        valid_passports += validate(entries)

print(valid_passports)
