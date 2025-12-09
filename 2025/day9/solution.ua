IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ↯∞_2 GetNumbers &fras "test_input"

RectArea ← ⌵≡₁/×+₁-

&p $"Part 1: _" /↥♭ RectArea˙⊞(⊙∘) Inp

# assumes points are in a vertical or horizontal straight line
Row ← +¤⟜(/⊂⇡+₁-) ⊃↧↥

°⊚/◇⊂≡(□Row)⟜(↻₋₁) Inp
↧₁ # filter out 2's at corners

¬
⊸(≡₁≍4_4 ⇡△)
⍥(⊸×/↥≡↻⊂0_0A₂¤)∞

# &p $"Part 2: _"
