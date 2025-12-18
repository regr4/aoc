inp ← •file.Lines "input"

Expand ← (∾ ·(•ParseFloat¨)⊸/˜´ ·<˘ ·⍉ ·> ·1⊸(↑⋈↓)¨ ','⊸((⊢-˜+`×¬)∘=⊔⊢))
ToPath ← +` ⟨0‿1⋄1‿0⋄0‿¯1⋄¯1‿0⟩ ⊏˜ "RULD" ⊐ ⊢
P1 ← ⌊´ ·+´¨ ·| ·(∊/⊣)´ ·ToPath¨ Expand¨

•Show P1 inp
