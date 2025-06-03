IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜⋕⊸≠@\n &fras "input"

&p $"Part 1: _" /+Inp

# &p $"Part 2: _"
