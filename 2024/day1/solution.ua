IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← °⊟⍉↯ ∞_2 GetNumbers &fras "input"

Inp
/+⌵-∩⍆
&p $"Part 1: _"

Inp
/+×⤚≡(/+=)⊙¤
&p $"Part 2: _"
