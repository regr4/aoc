IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

IsValid     ← ¬∊".-"
Inp         ← ⊜∘⊸≠@\n &fras "input"
Shp         ← △Inp
N           ← ⊢Shp
Indices     ← ▽¬≡≍¤0_0./⊂-¤¤⌊÷2⟜⇡-1×2 Shp
RunRotation ← ⬚0↻⊃(∘|↧⊃(IsValid|=)⟜⬚@-˜↻Inp)
/+♭ /↥≡RunRotation Indices
&p $"Part 1: _"

RunRotation₂ ← /↥≡(⬚0↻⊙°□)⊙□≡×⊙¤⇡N⊃(∘|↧⊃(IsValid|=)⟜⬚@-˜↻Inp)
/+♭ /↥≡RunRotation₂ Indices
&p $"Part 2: _"
