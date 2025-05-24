IsDigit    ← ×⊃(≤ @9|≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← &fras "input"

Part₁ ← /+≡(×°⊟⋕↘1) regex "mul\\((\\d+),(\\d+)\\)"

Part₁ Inp
&p $"Part 1: _"

.Inp
-⊃(⌕ "don't()"|⌕ "do()")
▽≠¯1 \(⨬(¯1◌|∘|1◌)+1:)
Part₁
&p $"Part 2: _"
