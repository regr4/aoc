IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜(□GetNumbers)≠@\n. &fras "input"

Inp
/+≡◇(×⊸∊∧(⊂⊃+×):¤°⊂:°⊂)
&p $"Part 1: _"

NDig   ← +1↥0⌊ₙ10
Concat ← +⊃(×⊙(ⁿ:10 NDig)|⋅∘)

Inp
/+≡◇(×⊸∊∧(⊂⊂⊃(+|×|≡Concat:¤)):¤°⊂:°⊂)
&p $"Part 2: _"
