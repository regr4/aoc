IsDigitOrMinus ← ↥↧⊃(≤ @9|≥ @0|=@-|)
GetNumbers     ← ⊜⋕ ⊸IsDigitOrMinus

Inp      ← ⊜GetNumbers≠@\n .&fras "input"
Size     ← 71_71
NBytes   ← 1024
FindPath ← ⊢path(▽⤚(¬≡(⬚1⊡)⊙¤)+A₂¤|≍-1Size)0_0
⬚0↙Size°⊚↙NBytes Inp
-1⧻FindPath
$"Part 1: _"
&p

ExistsPath ← (
  ⬚0↙Size°⊚˜↙Inp
  ◌FindPath
)

# just manual binary search until I found that 2851 does not work, but 2850 does.
# ExistsPath 2851
⊏ 2851 Inp
$"Part 2: _"
&p

# display grid
# ≡(&p≡(⊡:".#"))
