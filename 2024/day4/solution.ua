IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜∘≠ @\n.&fras "input"

GetXMAS    ← /+≡(/+⌕ "XMAS")
Horizontal ← +∩GetXMAS ≡⇌.
Vertical   ← Horizontal ⍉
Diagonal₁  ← Vertical ≡↻°⊏≡(˜⊂˜↯@-⧻.)
Diagonal₂  ← Diagonal₁ ≡⇌

+++ ⊃(Diagonal₂|Diagonal₁|Vertical|Horizontal) Inp
&p $"Part 1: _"

IsXMas ← /↥≡≍["MMASS" "MSAMS" "SMASM" "SSAMM"] ¤ ⊏×2⇡5 ♭

/+♭⧈IsXMas 3_3 Inp
&p $"Part 2: _"
