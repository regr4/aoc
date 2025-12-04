IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜(□≡⋕)⊸≠@\n &fras "input"

Inp

≡(/↥≡(+×₁₀°⊟)⧅< 2°□)
/+
# &p $"Part 1: _"
# &p $"Part 2: _"
