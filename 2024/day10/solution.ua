IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜≡⋕⊸≠@\n &fras "input"

Trailheads ← ⊚=0 Inp
Step       ← ▽=⊃(≡⬚¯1⊡:¤Inp|⋅(+1⊡:Inp)|⊙◌) +A₂ ¤.
Goal       ← =9⬚0˜⊡Inp

Trailheads
/+≡(⧻◴≡⊣path(Step|Goal))
&p $"Part 1: _"

Trailheads
/+≡(⧻path(Step|Goal))
&p $"Part 2: _"
