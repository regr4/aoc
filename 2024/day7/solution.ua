IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜(□GetNumbers)≠@\n. &fras "input"

Inp
/+≡◇(×⊸∊∧(⊂⊃+×):¤°⊂:°⊂)
$"Part 1: _"
&p

Concat ← ⋕⊂∩°⋕
Inp
/+≡◇(×⊸∊∧(⊂⊂⊃(+|×|≡Concat:¤)):¤°⊂:°⊂)
$"Part 2: _"
&p
