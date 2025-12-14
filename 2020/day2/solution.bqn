inp ← •file.Lines "input"

Split ← ((⊢-˜¬×+`)∘=⊔⊢)

P ← {
  ⟨range, ⟨chr, ·⟩, password⟩ ← ' 'Split𝕩
  nums ← •BQN¨ '-'Split range # wanted •ParseFloat, but CBQN didn't like that
  ⟨nums, chr, password⟩
}

S1 ← {
  𝕊 ⟨range, chr, password⟩ :
  range +↩ ↕≠range
  ≠´ range ≤ +´ chr=password
}

S2 ← {
  𝕊 ⟨indices, chr, password⟩ :
  ≠´ chr=(indices-1) ⊏ password
}

•Show +´ ((S1⋈S2)∘P)¨ inp
