inp ← •file.Lines "input"

Split ← ((⊢-˜¬×+`)∘=⊔⊢)

P ← {
  ⟨range, ⟨chr, ·⟩, password⟩ ← ' 'Split𝕩
  nums ← •BQN¨ '-'Split range # wanted •ParseFloat, but CBQN didn't like that
  ⟨nums, chr, password⟩
}

S1 ← {
  ⟨range, chr, password⟩ ← 𝕩
  range +↩ ↕≠range
  ≠´ range ≤ +´ chr=password
}

S2 ← {
  ⟨indices, chr, password⟩ ← 𝕩
  ≠´ chr=(indices-1) ⊏ password
}

•Show +´ ((S1⋈S2)∘P)¨ inp
