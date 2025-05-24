IsDigitOrMinus ← ↥↧⊃(≤ @9|≥ @0|=@-|)
GetNumbers     ← ⊜⋕ ⊸IsDigitOrMinus
Inp            ← ⊜GetNumbers≠@\n .&fras "input"

Size   ← 71_71
NBytes ← 1024
Step   ← ▽⤚(¬≡(⬚1⊡)⊙¤)+A₂¤
Goal   ← ≍-1Size
⬚0↙Size°⊚↙NBytes Inp
-1⧻⊢path(Step|Goal)0_0
&p $"Part 1: _"

ExistsPath ← (
  ⬚0↙Size°⊚˜↙Inp
  ⍣(⋅1⊢path(Step|Goal)0_0)0
)

# just manual binary search until I found that 2851 does not work, but 2850 does.
⍤.ExistsPath 2851
⍤.¬ExistsPath 2852
⊏2851 Inp
&p $"Part 2: _"

# display grid
# ≡(&p≡(⊡:".#"))
