S2I ← 10⊸×⊸+˜´∘⌽-⟜'0'
Partition ← {
    b ← 1-𝕨
    (b/+`𝕨) ⊔ (b/𝕩)
}
IndexIn ← { ⊑(𝕨=𝕩)/(↕⊑≢𝕩) }

input ← •file.Lines "../input.txt"
parsed ← (' '⊸≠⊸/)¨input

list ← 'X'‿'Y'‿'Z'
kill_list ← ∘‿2 ⥊ 'X'‿⟨'B', 'A', 'C'⟩‿'Y'‿⟨'C', 'B', 'A'⟩‿'Z'‿⟨'A', 'C', 'B'⟩

# Does 𝕨 kill 𝕩
Round ← { +´ 0‿3‿6 × 𝕩=0‿1⊑(⊑˘𝕨=kill_list)/kill_list }
Score ← { 1+(𝕩 IndexIn list) }

solution ← +´{
    a ← 0⊑𝕩
    b ← 1⊑𝕩
    (Score b) + (b Round a)
}¨parsed
•Show solution
