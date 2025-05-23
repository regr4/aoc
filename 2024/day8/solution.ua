IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

IsValid     ← ¬∊".-"
Inp         ← ⊜∘⊸≠@\n &fras "input"
Shp         ← △ Inp
N           ← ⊢ Shp
Indices     ← ▽¬≡≍¤0_0./⊂-¤¤⌊÷2⟜⇡-1×2 Shp
RunRotation ← ⬚0↻⊃(∘|↧⊃(IsValid|=)⟜⬚@-˜↻Inp)
Indices
/↥≡RunRotation
/+♭

$"Part 1: _"
&p

RunRotation₂ ← /↥≡(⬚0↻⊙°□)⊙□≡×⊙¤⇡N⊃(∘|↧⊃(IsValid|=)⟜⬚@-˜↻Inp)
Indices
/↥≡RunRotation₂
/+♭

$"Part 2: _"
&p
