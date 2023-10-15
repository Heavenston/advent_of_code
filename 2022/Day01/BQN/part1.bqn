S2I ← 10⊸×⊸+˜´∘⌽-⟜'0'
Partition ← {
    b ← 1-𝕨
    (b/+`𝕨) ⊔ (b/𝕩)
}

input ← •file.Lines "../test.txt"

a ← 0 = (⊑≢)¨ input
groups ← a Partition input
parsed ← (S2I¨)¨ groups

solution ← ⌈´+´¨ parsed 
•Show (+´)¨ parsed 
•Show solution
