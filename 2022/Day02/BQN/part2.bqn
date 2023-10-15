S2I ← 10⊸×⊸+˜´∘⌽-⟜'0'
Partition ← {
    b ← 1-𝕨
    (b/+`𝕨) ⊔ (b/𝕩)
}
IndexIn ← { ⊑(𝕨=𝕩)/(↕⊑≢𝕩) }

input ← •file.Lines "../test.txt"
parsed ← (' '⊸≠⊸/)¨input

list ← 'A'‿'B'‿'C'

# In <- Other player
# Out -> Possible plays
# 0 = Lose
# 1 = Draw
# 2 = Win 
rt ← ∘‿2 ⥊ 'A'‿⟨'C', 'A', 'B'⟩‿'B'‿⟨'A', 'B', 'C'⟩‿'C'‿⟨'B', 'C', 'A'⟩

•Show parsed
#•Show list
•Show {
    i ← (𝕩-'A')⊏rt
    choice ← (𝕩 - 'X')⊑1⊑i⊏rt
}´⚇1 parsed
