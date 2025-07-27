# Day 69: Count Hills and Valleys in an Array

**Difficulty**: Easy  
**Topics**: Arrays

---

## Problem Statement

You are given a 0-indexed integer array `nums`.  
An index `i` is part of a **hill** in `nums` if the closest non-equal neighbors of `i` are **smaller** than `nums[i]`.  
Similarly, an index `i` is part of a **valley** in `nums` if the closest non-equal neighbors of `i` are **larger** than `nums[i]`.  

> Adjacent indices `i` and `j` are part of the same hill or valley if `nums[i] == nums[j]`.

**Note**: For an index to be part of a hill or valley, it must have a non-equal neighbor on **both** the left and right of the index.

Return the number of **hills** and **valleys** in `nums`.

---

## Example 1

**Input**:  
`nums = [2, 4, 1, 1, 6, 5]`

**Output**: `3`

**Explanation**:
- At index 0: No non-equal neighbor on the left → Not a hill/valley
- At index 1: Neighbors are 2 and 1 → 4 > 2 and 4 > 1 → **Hill**
- At index 2: Neighbors are 4 and 6 → 1 < 4 and 1 < 6 → **Valley**
- At index 3: Same value as index 2 → Same **Valley**
- At index 4: Neighbors are 1 and 5 → 6 > 1 and 6 > 5 → **Hill**
- At index 5: No non-equal neighbor on the right → Not a hill/valley

→ Total: 3 hills/valleys

---

## Example 2

**Input**:  
`nums = [6, 6, 5, 5, 4, 1]`

**Output**: `0`

**Explanation**:
- Index 0 & 1: No non-equal neighbor on the left → Not a hill/valley
- Index 2 & 3: Neighbors are 6 and 4 → 5 < 6 and 5 > 4 → Not a hill/valley
- Index 4: Neighbors are 5 and 1 → 4 < 5 and 4 > 1 → Not a hill/valley
- Index 5: No non-equal neighbor on the right → Not a hill/valley

→ Total: 0 hills/valleys

---

## Constraints

- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
