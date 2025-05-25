IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜GetNumbers⊸≠@\n &fras "input"

A ← +⊃(×2/+|/↧) ×⊸↻₁
/+≡A Inp
&p $"Part 1: _"
P ← +⊃(/×|×2/↧+⊸↻₁)
/+≡P Inp
&p $"Part 2: _"
