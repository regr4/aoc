# IsDigitOrMinus ← ↥↧⊃(≤ @9|≥ @0|=@-|)
# GetNumbers     ← ⊜⋕ ⊸IsDigitOrMinus
Inp ← °{⊙∘} ⊜□¬⦷"\n\n" .&fras "input"
# Parse patterns, designs
PP   ← ⊜□¬⦷", ". ⊙◌
PD   ← ⊜□⊸≠ @\n
InpP ← PP Inp
InpD ← PD◌Inp

# IsPrfx : String String -> Bool
IsPrfx        ← ⊢⌕
Step          ← ≡(□↘◇⧻)⊃(▽⊃(≡◇IsPrfx InpP¤|InpP)|¤)°□
Possibilities ← |1 memo(⨬(⊙◌/+≡◇Possibilities⊃Step¤|⋅1)=0⧻.)

/+≥₁ ≡Possibilities InpD
&p $"Part 1: _"
/+≡Possibilities InpD
&p $"Part 2: _"
