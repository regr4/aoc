IsDigit ← ↧⊃(≤ @9) (≥ @0)

GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← &fras "input"

Part₁ ← /+≡(×°⊟⋕↘1)regex "mul\\((\\d+),(\\d+)\\)"

Part₁ Inp
$"Part 1: _"
&p

.Inp
-⊃(⌕ "don't()"|⌕ "do()")
Temp ← ⨬(¯1◌|∘|1◌)+1:
▽≠¯1 \Temp
Part₁
$"Part 2: _"
&p
