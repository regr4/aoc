IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

RawInp  ← ⊜∘⊸≠@\n &fras "input"
Inp     ← ⬚@.+˜↯0×2⊸△ RawInp
Shp     ← △ RawInp
Indices ← ▽¬≡≍¤0_0./⊂+1-¤¤÷2:⇡-1.△Inp
Indices
/↥≡(↻⊃(∘|↧⊃(=|≠@.)⬚@.⊸↻:Inp))
/+♭↙Shp

$"Part 1: _"
&p

# $"Part 2: _"
# &p
