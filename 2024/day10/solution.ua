IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp        ← ⊜≡⋕⊸≠@\n &fras "input"
Trailheads ← ⊚=0 Inp
Trailheads

Step ← ▽=⊃(≡⬚¯1⊡:¤Inp|⋅(+1⊡:Inp)|⊙◌) +A₂ ¤.
Goal ← =9⬚0˜⊡Inp

/+≡(⧻◴≡⊣path(Step)(Goal))
$"Part 1: _"
&p

Trailheads
/+≡(⧻path(Step)(Goal))
$"Part 2: _"
&p
