IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜GetNumbers⊸≠@\n &fras "input"

# claim to mask
# CTM : size, [x, y, w, h] -> boolean mask
CTM ← ˜(↻¯) ⬚0↙ ⊓(˙⊂|⊃(˜↯1 ↙₂|↘₂)⇌)
&p $"Part 1: _" ⧻⊚ >₁ /+≡(CTM 1000 ↘₁) Inp

# Inp
# ≡(□₂⊙(/⊂ ⧋+⊙⇡ ⊃↙₂↘₂) °⊂)

# &p $"Part 2: _"
