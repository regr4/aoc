Inp ← ⊜∘⊸≠@\n &fras "input"

&p $"Part 1: _" /++₁≡⋕ ▽∩♭ ⊸(/× ⧋<) ⊸(≡⬚@:↻A₂ ¤) Inp

# We want to separate out the different "basins" and calculate their
# areas. We use a trick: first we assign every place in the array an
# index. We then repeatedly assign to each place the minimum of all
# the indices of its neighbours in its own basin (which we can check
# for by it not being 9). Do inf yields a 2d array with every basin
# assigned a number. Deshaping and doing some group by classify magic
# yields the basins and their sizes.

Inp
≠@9
⟜(↯△) ⟜(⇡₁⧻♭)
⤚×
⊙◌⍥(⊸×/↥≡⬚0↻⊂0_0 A₂ ¤)∞
⊕(×⊃(≠0⊢|⧻)) ⊸⊛ ♭
/×↙₃⇌⍆

&p $"Part 2: _"
