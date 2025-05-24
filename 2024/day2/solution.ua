IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp    ← ⊜(□GetNumbers)⊸(≠ @\n) &fras "input"
IsSafe ← ×⊃(=1⧻◴±)(/× ×⊃(≤ 3)(≥ 1) ⌵)⧈/- 2

/+≡◇IsSafe Inp
&p $"Part 1: _"

IsSafe₂ ← /↥≡(IsSafe ▽)⊙¤ ⊞≠.°⊏

/+≡◇IsSafe₂ Inp
&p $"Part 2: _"
