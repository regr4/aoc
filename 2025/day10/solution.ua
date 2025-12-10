IsDigit    ← ↧⊃(≤ @9|≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ≡◇(□⊜□⊸≠ @\s) ⊜□⊸≠@\n &fras "input"

# goal, [box numbers] -> matrix of which button does what
ParseButtons ← ≡◇(˜⬚0↯ °⊚) ˜⊙∘ ¤¤⧻

Inp
≡◇(
  ↘¯1
  ⊓(=@# ↘¯1↘1 °□|⍚GetNumbers)°⊂
  ⟜ParseButtons
  -₁⧻⊢path(≠¤|/×=0)
)
/+

&p $"Part 1: _"

# Inp

# °□⊢
# ↘1
# ⊃↙↘ ¯1
# ⊓(◇GetNumbers°¤|⍚GetNumbers)
# ⟜ParseButtons

# /+
# &p $"Part 2: _"
