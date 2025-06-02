# Experimental!
IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ≡⋕ ▽⊸≠@\n &fras "input"

&p $"Part 1: _" /+▽⊸(=⟜↻₁) Inp
&p $"Part 2: _" /+▽⊸=⟜(↻÷2⊸⧻) Inp
