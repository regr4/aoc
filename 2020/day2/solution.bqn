inp ← •file.Lines "input"

Split ← ((⊢-˜¬×+`)∘=⊔⊢)

P ← {
  ⟨range, ⟨chr, ·⟩, password⟩ ← ' 'Split𝕩
  nums ← •ParseFloat¨ '-'Split range
  ⟨nums, chr, password⟩
}

S1 ← {
  𝕊 ⟨lo, hi⟩‿chr‿password :
  (lo⊸≤ ∧ ≤⟜hi) +´ chr=password
}

S2 ← {
  𝕊 indices‿chr‿password :
  ≠´ chr=(indices-1) ⊏ password
}

•Show +´ ((S1⋈S2) P)¨ inp
