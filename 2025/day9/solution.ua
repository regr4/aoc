IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit

Inp ← ↯∞_2 GetNumbers &fras "input"

RectArea ← ⌵≡₁/×+₁-

&p $"Part 1: _" /↥♭ RectArea˙⊞(⊙∘) Inp

# assumes points are in a vertical or horizontal straight line

⌊÷1e3Inp
°⊚
≡(&p""≡&pf)
# /+≡/+⌵-⟜↻₁Inp

# &p $"Part 2: _"
