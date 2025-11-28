IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜□⊸≠@\n &fras "input"

C ← +⊓(×8°⋯⇌=@B|°⋯⇌=@R)⊃↙₇↘₇
S ← ⍆≡◇C Inp

&p $"Part 1: _" /↥S
&p $"Part 2: _" ⍜-(⊢⊚=0=°⊏)⊸⊢S
# alternate solutions to part 2
# +1+⊃(⊢|⊗2⧈/-2) S
# +1+⊃(⊢|⊢⊚=2-⟜↻₁)S
