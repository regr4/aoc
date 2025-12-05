IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ∩°□ °⊟ ⊜□⊸(¬⌕"\n\n") &fras "input"
# Freshness ranges
FR ← ↯ ∞_2 GetNumbers ⊙◌ Inp
# Ingredients
I ← GetNumbers ◌Inp
# In range?
IR ← /×≥0 ⍜⊣¯ -

# &p $"Part 1: _" /+/↥⊞IR FR I

⊏⍏⊸≡⊢ FR

# &p $"Part 2: _"
