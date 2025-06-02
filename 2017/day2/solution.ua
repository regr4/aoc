IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜GetNumbers⊸≠@\n &fras "input"

&p $"Part 1: _" /+≡(-⊃/↧/↥) Inp
&p $"Part 2: _" /+≡(⊢▽⊸(=⟜⌊)▽⊸≠1♭⊞÷.) Inp
