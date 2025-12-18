# Experimental!
IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit
Inp        ← GetNumbers &fras "input"

S ← /×⊢▽⊸≡(=2020/+)

&p $"Part 1: _" S♭₂˙⊞⊟₂ Inp
&p $"Part 2: _" S♭₂˙⊞⊟₃ Inp
