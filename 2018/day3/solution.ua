IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
N          ← 1000

Inp ← ⊜GetNumbers⊸≠@\n &fras "input"

# &p $"Part 1: _"
# &p $"Part 2: _"
Inp
/+≡(˜⌝↻≡≡(/×)>⊞⊂.⇡N ¤¤⊃↘↙ 2↘₁)
