# Experimental!
IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← GetNumbers &fras "input"

# number of digits (only positive integers >= 1 considered)
ND ← +₁⌊°ₑ₁₀
# blink once
BS ← ⨬(⋅[1]|⨬([×2024]|≡⋕↯2_∞°⋕)=₀◿₂⊸ND)⊸(≠₀)

# NS : n (int), stone -> number of stones after n blinks
# requires raised recursion limit (around 250 is enough)
NS ← |2 memo(⨬(1◌|/+≡(NS) ⊙BS-₁)⊸≠₀)

# /+≡NS 16 Inp

# how about recur?
# NS ← recur(⨬([]|[1])=₀⊢|≡⊟⊓(-₁|BS)°⊟|/+)

S ← /+≡NS

&p $"Part 1: _" S 25 Inp
&p $"Part 2: _" S 75 Inp
