# Day 66: Minimum Score After Removals on a Tree  
**Status**: Solved  
**Difficulty**: Hard  

---

### 🧠 Topics  
*Premium* 🔒  
**Companies**: *(Hidden - Premium Content)*  
**Hint**:  

There is an undirected connected **tree** with `n` nodes labeled from `0` to `n - 1` and `n - 1` edges.

You are given:
- A 0-indexed integer array `nums` of length `n`, where `nums[i]` represents the **value** of the `i-th` node.
- A 2D integer array `edges` of length `n - 1`, where `edges[i] = [ai, bi]` indicates an edge between nodes `ai` and `bi`.

---

### 🧩 Problem

Remove **two distinct edges** of the tree to form **three connected components**. For each pair of removed edges:

1. Get the **XOR** of all the node values in each component.
2. Find the **difference** between the **largest** and **smallest** XOR values.
3. The score for the pair is that difference.

Return the **minimum score** of all possible edge removal pairs.

> 💡 **Example**:  
Say the three components have values:  
- `[4, 5, 7]` → XOR = `4 ^ 5 ^ 7 = 6`  
- `[1, 9]` → XOR = `1 ^ 9 = 8`  
- `[3, 3, 3]` → XOR = `3 ^ 3 ^ 3 = 3`  
Then the score = `8 - 3 = 5`.

---

### 📘 Examples

**Example 1:**
Input:
nums = [1,5,5,4,11]
edges = [[0,1],[1,2],[1,3],[3,4]]
Output: 9

Explanation:

Component 1: [1,3,4] → [5,4,11] → XOR = 10

Component 2: [0] → [1] → XOR = 1

Component 3: [2] → [5] → XOR = 5
Score = 10 - 1 = 9


**Example 2:**
Input:
nums = [5,5,2,4,4,2]
edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
Output: 0

Explanation:

Component 1: [3,4] → [4,4] → XOR = 0

Component 2: [1,0] → [5,5] → XOR = 0

Component 3: [2,5] → [2,2] → XOR = 0
Score = 0 - 0 = 0


---

### 📋 Constraints:
- `n == nums.length`  
- `3 <= n <= 1000`  
- `1 <= nums[i] <= 10⁸`  
- `edges.length == n - 1`  
- `edges[i].length == 2`  
- `0 <= ai, bi < n`  
- `ai != bi`  
- `edges` represent a valid **tree**
