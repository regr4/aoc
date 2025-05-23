IsDigit ← ↧⊃(≤ @9) (≥ @0)

GetNumbers ← ⊜⋕ ⊸IsDigit

Inp ← °⊟⊜□¬⌕"\n\n". &fras "input"

Rules        ← ↯∞_2 ◇GetNumbers ⊙◌ Inp
PagesNeeded  ← ⊜(□ GetNumbers)⊸≠@\n °□◌ Inp
IsCorrect    ← ¬/↥≡(∊)¤Rules ⧅>2
Middle       ← ⊡⌊÷2⊸⧻
CorrectPages ← ▽⊸≡◇IsCorrect PagesNeeded

/+≡◇Middle CorrectPages
$"Part 1: _"
&p

IncorrectPages          ← ▽⊸≡◇(¬IsCorrect) PagesNeeded
Ordering                ← ∊Rules⊟:
IncorrectPagesReordered ← ≡⍜°□(⊏⍏≡/+⊸(⊞Ordering.)) IncorrectPages
/+≡◇Middle IncorrectPagesReordered
$"Part 2: _"
&p
