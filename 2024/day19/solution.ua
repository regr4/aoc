# IsDigitOrMinus ← ↥↧⊃(≤ @9|≥ @0|=@-|)
# GetNumbers     ← ⊜⋕ ⊸IsDigitOrMinus
Inp ← °{⊙∘} ⊜□¬⦷"\n\n" .&fras "input"
# Parse patterns, designs
PP ← ⊜□¬⦷", ".
PD ← ⊜□⊸≠ @\n

# assert that all patterns are different (otherwise we might have some
# duplication in the pathfinding) ⍤.≍◴.PP Inp

# IsPrfx : String String -> Bool
IsPrfx ← ⊢⌕

Step ← ≡(□↘)≡◇⧻▽⊃(≡(◇˜IsPrfx)¤|⋅∘|¤)°□
Done ← =0 ◇⧻

# ⊃⋅PD PP Inp
# /+≡⍣(⋅1⊢path(Step|Done))0⊙¤
# &p $"Part 1: _"

# DOES NOT WORK (uses too much memory)
# /+≡(⊙◌⧻path(˜↯0⧻.Step|Done))⊙¤
# Guess we need some dynamic programming
# Or just memoization
⊃⋅PD PP Inp

Possibilities ← |2 memo(⨬(/+≡(Possibilities°□)⊙¤⊸Step|⋅⋅1)=0⧻.)
/+≡◇Possibilities⊙¤

# &p $"Part 2: _"
