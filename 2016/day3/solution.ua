IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⊜GetNumbers⊸≠ @\n &fras "input"

IsTriangle ← /↧♭≡(</+⊃↙↘2↻∘) ⇡3¤

# ≡↻ ⇡3 ¤[1 2 3] why does this not work?
# ≡(↻∘) ⇡3 ¤[1 2 3] while this does?

Part₁ ← /+≡IsTriangle Inp
&p $"Part 1: _" Part₁

Inp₂ ← ↯ ∞_3 /⊂⍉Inp

Part₂ ← /+≡IsTriangle Inp₂
&p $"Part 2: _" Part₂
