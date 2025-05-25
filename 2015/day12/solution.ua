IsDigitOrMinus ← ↥↧⊃(≤ @9|≥ @0|=@-|)
GetNumbers     ← ⊜⋕ ⊸IsDigitOrMinus

Inp ← &fras "input"

/+GetNumbers Inp
&p $"Part 1: _"
