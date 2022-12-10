"""day n"""

from enum import Enum

CpuState = Enum("CpuState", ["READY_STATE", "WAITING_STATE", "READY_TO_ADD_STATE"])

with open("input") as f:
    inp = f.read().strip()

instrs = iter(inp.split("\n"))
total_signal_strength = 0
next_important_number = 20

# CPU state
curr_cycle = 1
x = 1
cpu_state = CpuState.READY_STATE
n_to_add = 0

while True:
    if cpu_state == CpuState.WAITING_STATE:
        cpu_state = CpuState.READY_TO_ADD_STATE
    elif cpu_state == CpuState.READY_TO_ADD_STATE:
        x += n_to_add
        cpu_state = CpuState.READY_STATE
    # not elif! if we're ready, read a new instruction straight away.
    if cpu_state == CpuState.READY_STATE:
        try:
            instr = next(instrs)
        except StopIteration:
            break
        if instr == "noop":
            pass
        else:
            [cmd, arg_] = instr.split()
            assert cmd == "addx"
            arg = int(arg_)
            n_to_add = arg
            cpu_state = CpuState.WAITING_STATE

    if curr_cycle == next_important_number:
        signal_strength = curr_cycle * x
        total_signal_strength += signal_strength
        next_important_number += 40
    curr_cycle += 1

# part 1
print(f"part 1: {total_signal_strength}")

# part 2
print(f"part 2:")

instrs = iter(inp.split("\n"))

# CPU state
curr_cycle = 1
x = 1
cpu_state = CpuState.READY_STATE
n_to_add = 0

while True:
    if cpu_state == CpuState.WAITING_STATE:
        cpu_state = CpuState.READY_TO_ADD_STATE
    elif cpu_state == CpuState.READY_TO_ADD_STATE:
        x += n_to_add
        cpu_state = CpuState.READY_STATE
    # not elif! if we're ready, read a new instruction straight away.
    if cpu_state == CpuState.READY_STATE:
        try:
            instr = next(instrs)
        except StopIteration:
            break
        if instr == "noop":
            pass
        else:
            [cmd, arg_] = instr.split()
            assert cmd == "addx"
            arg = int(arg_)
            n_to_add = arg
            cpu_state = CpuState.WAITING_STATE

    if -1 <= (curr_cycle - 1) % 40 - x <= 1:
        print("#", end="")
    else:
        print(".", end="")

    if curr_cycle % 40 == 0:
        print("")

    curr_cycle += 1
