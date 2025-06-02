# Experimental!
IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← :⊜(⊙⋕°⊂) ⊸(¬⦷", ") ▽⊸≠@\n &fras "input"

Dirs  ← A₂
Start ← 0_0
# newpos newdirs ? currpos dirs turn nsteps
Step₁ ← ⊃(⋅∘|+×⊙⊢)⊙(↻-⊸¬=@R)

Part₁ ← /+⌵◌∧Step₁ Inp Dirs Start
&p $"Part 1: _" Part₁

# newposes newdirs ? currpos dirs turn nsteps
# Step₂ ← ⊃(⋅∘|˜⊂+⊸⊙⊣×⊙⊢)⊙(↻-⊸¬=@R)

# ◌∧Step₂ Inp Dirs ¤Start

# /+⌵⊢▽⊸⧆
