IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜⋕⊸≠@\n &fras "input"

# Bitwise XOR
Mix   ← °⋯ ⬚0≡≠ ∩⋯
Prune ← ◿ 16777216

Step ← (
  Prune Mix⟜×₆₄
  Prune Mix⟜(⌊÷₃₂)
  Prune Mix⟜×₂₀₄₈
)

/+≡(⍥₂₀₀₀Step) Inp
&p $"Part 1: _"
