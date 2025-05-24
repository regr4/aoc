IsDigitOrMinus ← ↥↧⊃(≤ @9|≥ @0|=@-|)
GetNumbers     ← ⊜⋕ ⊸IsDigitOrMinus
Inp            ← memo(≡⊃↙₂↘₂⊜GetNumbers≠@\n .&fras "input")

WH            ← 101_103
Middle        ← ⌊÷2 WH
RunSimulation ← ◿¤WH+ ⊃(⋅∘|×⊙⋅∘)

RunSimulation 100 Inp
/×≡/+⊞≍C₂ ±-¤Middle
&p $"Part 1: _"

NNDist ← ⍜▽(+0.1)=0./↧+⊃(⊞(/↥⌵-).|⍜♭(⍜▽⋅∞.)⊞=.⇡⧻)
Avg    ← ÷⧻⟜/+
# http://jimbeck.caltech.edu/summerlectures/references/Entropy%20estimation.pdf
EEst ← Avg ln×⊸⧻NNDist
≡(EEst RunSimulation :Inp) ⇡10
