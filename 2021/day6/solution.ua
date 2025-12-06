IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜⋕⊸≠@, ▽⊸≠@\n &fras "input"

# step school
SS ← ⍜⊙(⊏6_8)+ ⊃(⊢|⬚0↻₁)
S  ← /+⍥SS ⊙(≡/+⊞=⇡9)

&p $"Part 1: _" S 80 Inp
&p $"Part 2: _" S 256 Inp
