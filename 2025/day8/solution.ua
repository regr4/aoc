IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit

Inp ← ↯∞_3 GetNumbers &fras "input"

Dist    ← ⍜°√≡₁/+-
Dists   ← Dist˙⊞⊙∘ Inp
MaxDist ← ⊡(-₁ 1000) ⍆ /⊂ ↥Dists ×1e10˙⊞≤ ⇡⧻ Inp

&p $"Part 1: _" /×↙₃⇌⍆≡/+◴⍥˙(↧1 ⍜⍉⊞(/+×))∞ ≤MaxDist Dists

# Manual binary search by replacing 1000 in MaxDist: after 5231
# connections we have one big network. Then we have a distance of
# 14514.65824606284.

# number of networks
# ⧻◴⍥˙(↧1 ⍜⍉⊞(/+×))∞ ≤MaxDist Dists

# float equality comparison works for some reason :)
&p $"Part 2: _" ×∩(⊢⊢) ∩⌞▽ =14514.65824606284 ∩₃/⊂ ◡Dist ˙⊞⊙∘ Inp
