IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Instrs   ← map ["turn on" "toggle " "turn of"] 0_1_2
ParseRow ← □₂⊃(˜get Instrs↙₇|↯2_2 GetNumbers)
Inp      ← ≡◇ParseRow ⊜□⊸≠@\n &fras "input"

Solve‼! ← /+♭∧(⍜⊙(↙⊙↘:)⨬(^0|^1|^2) ⊙(⟜- -₁) °{⊙⊟}) : ↯1000_1000 0

Solve‼!(≡₀⋅1|¬|≡₀⋅0) Inp
&p $"Part 1: _"

Solve‼!(+₁|+₂|↥₀-₁) Inp
&p $"Part 2: _"
