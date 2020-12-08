from collections import Counter

fn = "day 2/in"
with open(fn, "r") as f:
    lines = list(map(str.strip, f.readlines()))

valid = 0

for line in lines:
    pos, char, password = line.split()
    char = char[0]
    first, second = map(int, pos.split('-'))
    valid += (password[first - 1] == char) ^ (password[second - 1] == char)

print(valid)