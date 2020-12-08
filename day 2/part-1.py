from collections import Counter


fn = "day 2/in"
with open(fn, "r") as f:
    lines = list(map(str.strip, f.readlines()))

valid = 0

for line in lines:
    freq, char, password = line.split()
    mn, mx = map(int, freq.split('-'))
    pcount = Counter(password)
    valid += (mn <= pcount[char[0]] <= mx)

print(valid)
