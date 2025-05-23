# Day 23: Find the Maximum Sum of Node Values

## 🔍 Problem Statement

There exists an undirected **tree** with `n` nodes numbered from `0` to `n - 1`.  
You are given a **0-indexed** 2D integer array `edges` of length `n - 1`, where `edges[i] = [uᵢ, vᵢ]` indicates an edge between nodes `uᵢ` and `vᵢ` in the tree.

You are also given:
- A **positive integer** `k`
- A **0-indexed array** `nums` of **non-negative integers** of length `n`, where `nums[i]` represents the value of the node numbered `i`.

Alice wants to **maximize the sum** of the values of the tree nodes.  
She can perform the following operation **any number of times (including zero)**:

### ✨ Operation:
Choose any edge `[u, v]` and update the node values as:

```text
nums[u] = nums[u] XOR k  
nums[v] = nums[v] XOR k
```

Return the **maximum possible sum** of the node values that Alice can achieve by performing this operation any number of times.

---

## 💡 Examples

### Example 1:
**Input:**  
`nums = [1,2,1]`, `k = 3`, `edges = [[0,1],[0,2]]`  
**Output:**  
`6`  
**Explanation:**  
Choose edge `[0,2]`:  
- nums[0] becomes 1 XOR 3 = 2  
- nums[2] becomes 1 XOR 3 = 2  
Final `nums = [2, 2, 2]`, sum = 6

---

### Example 2:
**Input:**  
`nums = [2,3]`, `k = 7`, `edges = [[0,1]]`  
**Output:**  
`9`  
**Explanation:**  
Choose edge `[0,1]`:  
- nums[0] = 2 XOR 7 = 5  
- nums[1] = 3 XOR 7 = 4  
Final `nums = [5,4]`, sum = 9

---

### Example 3:
**Input:**  
`nums = [7,7,7,7,7,7]`, `k = 3`, `edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]`  
**Output:**  
`42`  
**Explanation:**  
The sum is already maximum; no operations needed.

---

## 📋 Constraints

- `2 <= n == nums.length <= 2 * 10⁴`
- `1 <= k <= 10⁹`
- `0 <= nums[i] <= 10⁹`
- `edges.length == n - 1`
- `0 <= edges[i][0], edges[i][1] <= n - 1`
- The input is guaranteed to represent a valid tree.
