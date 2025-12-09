IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ↯∞_2 GetNumbers &fras "input"

RectArea ← ⌵≡₁/×+₁-

&p $"Part 1: _" /↥♭ RectArea˙⊞(⊙∘) Inp
# &p $"Part 2: _"
