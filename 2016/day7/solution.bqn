inp ← •file.Lines "input"

IsAlpha ← {('a'≤𝕩) ∧ (𝕩≤'z')}
ParseLine ← (1-˜ ((1+ +`) × ¬)∘¬∘IsAlpha)⊸⊔
IsAbba ← (1⊸⌽⊸≢)∧(≡⟜⌽)
ContainsAbba ← ∨´ (IsAbba˘ (4⊸↕))
Solve1 ← {
  a ← ContainsAbba¨ 𝕩
  m ← 2|↕≠𝕩
  (¬∨´ m×a) ∧ (∨´ (¬m)×a)
}

•Show +´ Solve1¨ ParseLine¨ inp
