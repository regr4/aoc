IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Dirs       ← map ">^<v" A₂

Inp ← ≡(get :Dirs) &fras "input"

V ← \+⊂0_0

⧻◴V Inp
&p $"Part 1: _"

⧻◴ ⊂∩V ⊃(▽|▽¬)◿2°⊏ Inp
&p $"Part 2: _"
