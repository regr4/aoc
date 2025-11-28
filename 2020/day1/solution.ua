# Experimental!
IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← GetNumbers &fras "input"
Inp

&p $"Part 1: _" /×⊢▽⊸≡(=2020/+)/⊂˙⊞(⊂) Inp
&p $"Part 2: _" /×⊢▽⊸≡(=2020/+)/⊂/⊂˙⊞(⊂⊂)
