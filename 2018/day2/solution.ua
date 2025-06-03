IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜□⊸≠@\n &fras "input"

&p $"Part 1: _" /×/+ ≡◇(˜∊2_3 ⊕⧻⊸⊛) Inp
&p $"Part 2: _" ▽⊸=°□₂ ˜⊏Inp ⊢⊚=1⊞(/+◇≠). Inp
