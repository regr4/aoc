IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit

Inp ← ↯∞_2_2 GetNumbers &fras "input"

# assumes 0_0 ≤ argument.
R ← ⨬(⊞×⊃(⇡₀⊢|±)|♭₂⇡+₁)/↥⊸=₀
S ← /+=1⧆ /◇⊂ ≡(□⧋+⊃(⊢|R/-) ⍆)

&p $"Part 1: _" S ▽⊸(≡/↥=₀ ≡/-) Inp
&p $"Part 2: _" S Inp
