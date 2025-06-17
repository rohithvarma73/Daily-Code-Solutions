# Day35 - Count the Number of Arrays with K Matching Adjacent Elements

**Difficulty:** Hard  
**Topics:** Dynamic Programming, Combinatorics  
**Companies:** *Premium Problem*  

---

## 🧠 Problem Statement

You are given three integers `n`, `m`, and `k`. A **good array** `arr` of size `n` is defined as follows:

- Each element in `arr` is in the inclusive range `[1, m]`.
- Exactly `k` indices `i` (where `1 <= i < n`) satisfy the condition `arr[i - 1] == arr[i]`.

Return the number of good arrays that can be formed.

Since the answer may be very large, return it modulo `10⁹ + 7`.

---

## 💡 Examples

### Example 1:

**Input:**  
`n = 3`, `m = 2`, `k = 1`  
**Output:**  
`4`  
**Explanation:**  
There are 4 good arrays:  
- [1, 1, 2]  
- [1, 2, 2]  
- [2, 1, 1]  
- [2, 2, 1]  

---

### Example 2:

**Input:**  
`n = 4`, `m = 2`, `k = 2`  
**Output:**  
`6`  
**Explanation:**  
There are 6 good arrays:  
- [1, 1, 1, 2]  
- [1, 1, 2, 2]  
- [1, 2, 2, 2]  
- [2, 1, 1, 1]  
- [2, 2, 1, 1]  
- [2, 2, 2, 1]  

---

### Example 3:

**Input:**  
`n = 5`, `m = 2`, `k = 0`  
**Output:**  
`2`  
**Explanation:**  
There are 2 good arrays:  
- [1, 2, 1, 2, 1]  
- [2, 1, 2, 1, 2]  

---

## 🔒 Constraints:

- `1 <= n <= 10⁵`  
- `1 <= m <= 10⁵`  
- `0 <= k <= n - 1`

---