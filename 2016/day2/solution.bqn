inp ← •file.Lines "input"

MakeMove ← {
  curr_pos 𝕊 move :
  2‿2⌊0‿0⌈curr_pos + move
}

ToMove ← {
  ⟨¯1‿0,0‿¯1,0‿1,1‿0⟩ ⊑˜ <⁼ "ULRD" ⊐ 𝕩
}

ToNumber ← {
  +´ 𝕩 × ⌽10⋆↕≠𝕩
}

keypad ← 1 + 3‿3⥊↕9
•Show ToNumber (⊑⟜keypad) (<1‿1) ((MakeMove⟜ToMove)˜˝ ⟜ ⌽)` inp
