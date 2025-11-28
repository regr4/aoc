IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← GetNumbers &fras "input"

S₁ ← ↥0/+-2⌊÷₃

S₂ ← /+≡(/+⍢(.S₁|>0))

&p $"Part 1: _" S₁ Inp
&p $"Part 2: _" S₂ Inp
