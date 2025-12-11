IsAlpha ← ↧⊃(≤ @z|≥ @a)
Inp     ← ⊜(□⊜∘ ⊸IsAlpha)⊸≠@\n &fras "input" # id since all labels are 3 letters

GM ← map ≡(⊙□◇°⊂)
NN ← ⊸(˜↯0 ⧻) °□⬚[]get # costs: all 0

&p $"Part 1: _" ⊙◌ ⧻path(NN|≍"out") "you" GM Inp

# check: no paths from dac to fft:
⍤ "path found :(" ⊙◌ ¬±⧻path(NN|≍ "fft") "dac" GM Inp

⊙◌ ⧻path(NN|≍ "fft") "svr" GM Inp
⊙◌ ⧻path(NN|≍ "dac") "fft" GM Inp
⊙◌ ⧻path(NN|≍ "out") "dac" GM Inp
&p $"Part 2: _" ××
