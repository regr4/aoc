IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← &fras "input"
Inp₂       ← /- ⊞=")(" Inp

/+ Inp₂
&p $"Part 1: _"

+1⊢⊚=¯1\+ Inp₂
&p $"Part 2: _"
