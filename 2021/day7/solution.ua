IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← ⍆GetNumbers &fras "input"

# it turns out that the optimal place is just the median of the array.
&p $"Part 1: _" /+⌵- ⊸(⊡⊸(÷₂⧻)) Inp

# given locations a_0, ..., a_n, we want to minimize the following
# quadratic polynomial: \sum_{i=0}^n Delta(x-a_i), where Delta(x) =
# x*(x+1)/2. Its derivative is \sum_{i=0}^n (x - a_i + 1/2) = nx + n/2
# - \sum_i a_i, so the minimum occurs at x = -1/2 + 1/n sum_i a_i.
# this might not be an integer, so check both its floor and ceiling
# and pick the best one.

&p $"Part 2: _" /↧≡/+ ÷₂ ×⊸+₁⌵ ⊞-⊸(⊃[⌊|⌈] -1/2 ÷⊃⧻/+) Inp
