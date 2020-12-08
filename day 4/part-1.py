fn = "day 4/in"
with open(fn, "r") as f:
    data = f.read().split("\n\n")

fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]) # omit cid

valid_passports = 0
for passport in data:
    entries = passport.split()
    entries = set(map(lambda e: e.split(":")[0], entries))
    valid_passports += (entries & fields == fields)

print(valid_passports)
