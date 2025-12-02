Inp ← ⊜□⊸≠@, ▽⊸≠@\n &fras "input"

# num digits
N  ← +₁⌊°ₑ₁₀
P₁ ← ×⊃(=₀◿⊸(+₁ₑ₁₀⌊÷₂ N)|=₀◿₂N)
P₂ ← ¬/↧⧆₁ ≡↻ ⊙¤ ⇡⧻ . °⋕

# inefficient but it works
Solve! ← (
  ≡(°⊟⊜⋕⊸≠@- °□
    /+ ▽⊸(≡^0) ⍜-(⇡+₁))
  /+
)

&p $"Part 1: _" Solve!P₁ Inp
&p $"Part 2: _" Solve!P₂ Inp
