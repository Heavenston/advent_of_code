S2I ← 10⊸×⊸+˜´∘⌽-⟜'0'
Partition ← {
    b ← 1-𝕨
    (b/+`𝕨) ⊔ (b/𝕩)
}

input ← •file.Lines "../input.txt"

a ← 0 = (⊑≢)¨ input
groups ← a Partition input
parsed ← (S2I¨)¨ groups

solution ← +´3↑∨+´¨ parsed 
•Show solution
