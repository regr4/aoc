"""day 1"""

with open('input2') as f:
    data = f.read()

data = data.split("\n\n")

elf_cals_list = []

for elf_list in data:
    cal_list = [int(s) for s in elf_list.split()]
    cal_sum = sum(cal_list)
    elf_cals_list.append(cal_sum)

# top elf
print(max(elf_cals_list))

# top 3 elves
elf_cals_list_sorted = sorted(elf_cals_list, reverse=True)
print(sum(elf_cals_list_sorted[:3]))
