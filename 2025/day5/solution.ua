IsDigit    ← ×⊃(≤@9|≥@0)
GetNumbers ← ⊜⋕⊸IsDigit

Inp ← ∩°□ °⊟ ⊜□⊸(¬⌕"\n\n") &fras "input"
# Freshness ranges
FR ← ↯ ∞_2 GetNumbers ⊙◌ Inp
# Ingredients
I ← GetNumbers ◌ Inp
# In range?
IR ← /×≥0 ⍜⊣¯ -

# range, list of ranges -> updated list
M ← ⨬(˜⊂|⍜⊙(⊣⊣)↥⊣) ⊃(≥⊓⊢⊣⊙⊣|⊙∘)

# deduplicated freshness ranges
DFR ← ∧M ⟜[⊢] ⍆ FR

&p $"Part 1: _" /+/↥⊞IR DFR I
&p $"Part 2: _" /++₁≡/- DFR
