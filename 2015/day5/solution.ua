IsDigit    ← ↧⊃(≤ @9) (≥ @0)
GetNumbers ← ⊜⋕ ⊸IsDigit
Inp        ← ⊜□⊸≠@\n &fras "input"

V       ← "aeiou"
IsNice₁ ← ××⊃(=₀ /+♭≡⌕["ab" "cd" "pq" "xy"] ¤|/↥=⟜⬚@\0↻₁|≥₃/+∊V)
/+≡◇IsNice₁ Inp
&p $"Part 1: _"

IsNice₂ ← ×⊃(
  /↥≡(/↥⌕1_1=⊸⬚@\0↻)⊙¤↘₂°⊏
| /↥⧈₃(=⊃⊢⊣)
)

/+≡◇IsNice₂ Inp
&p $"Part 2: _"
