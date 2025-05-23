IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp       ← ⊜∘⊸≠@\n &fras "input"
Dims      ← △ Inp
InRange   ← ∊♭₂⇡Dims
Area      ← ⧻
Perimeter ← /+♭↥⊃(¬∊:|¯InRange)≡(+¤)A₂¤.
Cost      ← ×⊃Area Perimeter

Inp
⊜□-@\0:°⊡
/+≡◇Cost
$"Part 1: _"
&p
