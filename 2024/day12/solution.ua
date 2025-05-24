IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜∘⊸≠@\n &fras "input"
Dims       ← △Inp
InRange    ← ∊♭₂⇡Dims

Area      ← ⧻
Perimeter ← /+♭¬×⊃(˜∊|InRange)≡(+¤)A₂¤.
Cost      ← ×⊃Area Perimeter

/+≡◇Cost ⊜□-@\0:°⊡ Inp
&p $"Part 1: _"
