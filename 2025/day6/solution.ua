IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit
GetOp      ← ▽⊸∊"*+"

Inp ← ⊜∘⊸≠@\n &fras "input"

# calculate: op, [num] -> num
C ← ⍣(
  /+ °"+"
| /× °"*"
| ⍤ 0 &s .
)

&p $"Part 1: _" /+≡C⊃(⊜∘⊸≠@ ⊣|⍉≡GetNumbers↘¯1) Inp
&p $"Part 2: _" /+⊜(C⊃(GetOp|GetNumbers)◇/⊂)⊸(≡/↥≠@ )⍉ Inp
