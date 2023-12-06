"""day 1"""

# common imports
import re

with open("input") as f:
    inp = f.read()

# part 1



total = 0
for line in inp.splitlines():
    digits = [int(x) for x in line if x in "0123456789"]
    total += digits[0]*10 + digits[-1]
print(f"part 1: {total}")

#part 2
english_digits = ["zero", "one", "two", "three", "four", "five", "six",
                "seven", "eight", "nine"]

def to_number(digit: str):
    if re.match("[1-9]", digit):
        return int(digit)
    else:
        return english_digits.index(digit)

total = 0
for line in inp.splitlines():
    matches = [match.group(1) for match in
               re.finditer(f"(?=({'|'.join(english_digits[1:])}|[1-9]))", line)]
    digits = [to_number(x) for x in matches]
    total += digits[0]*10 + digits[-1]

print(f"part 2: {total}")
