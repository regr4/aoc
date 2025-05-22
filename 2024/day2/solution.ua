IsDigit ← ↧⊃(≤ @9) (≥ @0)

GetNumbers ← ⊜⋕ ⊸IsDigit

IsSafe ← ↧⊃(=1⧻◴±)(/↧↧ ⊃(≤ 3)(≥ 1) ⌵)⧈(-°⊟) 2

Inp ← ⊜(□GetNumbers) ⊸(≠ @\n) &fras "input"

Inp
≡(IsSafe°□)
/+
$"Part 1: _"
&p

IsSafe₂ ← ↥⊃(IsSafe|/↥≡(IsSafe ▽)⊙¤ ⊞≠.⇡⊸⧻)

Inp
≡(IsSafe₂°□)
/+
$"Part 2: _"
&p
