IsDigit ← ↧⊃(≤ @9) (≥ @0)

GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜∘≠ @\n.&fras "input"

GetXMAS ← /+≡(/+⌕ "XMAS")

Horizontal ← +∩GetXMAS ≡⇌.
Vertical   ← Horizontal ⍉
Diagonal₁  ← Vertical≡↻⇡⊸⧻≡(˜⊂↯¤⊙"-")⊸⧻
Diagonal₂  ← Diagonal₁ ≡⇌

+++ ⊃(Diagonal₂|Diagonal₁|Vertical|Horizontal) Inp
$"Part 1: _"
&p

IsXMas ← /↥≡≍["MMASS" "MSAMS" "SMASM" "SSAMM"] ¤ ⊏0_2_4_6_8 ♭

/+♭⧈IsXMas 3_3 Inp
$"Part 2: _"
&p
