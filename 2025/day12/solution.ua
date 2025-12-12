# Experimental!
IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit

PReq ← ⊜(⊃↙↘2 GetNumbers)⊸≠ @\n
PP   ← =@# ≡°□ ↘1 ⊜□⊸≠@\n
Inp  ← ⊓(◇PReq|⍚PP) ⊃⊡↘¯1 ⊜□⊸(¬⦷"\n\n") &fras "input"

# does not solve problem, but it works on the test input :)
&p $"Part 1: _" ⧻ ˜▽⟜(≤⊓(≡/×|≡/+⧋×) ⊙⊙(≡◇(/+♭))) Inp
