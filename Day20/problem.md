# Day 19 Problem - Painting a Grid With Three Different Colors

**Difficulty:** Hard  
**Topics:** Dynamic Programming, Graph Coloring  
**Companies:** [Unknown]

---

## Problem Statement

You are given two integers `m` and `n`. Consider an `m x n` grid where each cell is initially white. You can paint each cell red, green, or blue. **All cells must be painted**.

Return the number of ways to color the grid such that **no two adjacent cells have the same color**.  
Since the answer can be very large, return it modulo **10⁹ + 7**.

---

## Example 1:

**Input:**  
`m = 1, n = 1`  
**Output:**  
`3`  

**Explanation:**  
The three possible colorings are simply using red, green, or blue in the single cell.

---

## Example 2:

**Input:**  
`m = 1, n = 2`  
**Output:**  
`6`  

**Explanation:**  
Each of the two cells must have different colors, so for the first cell 3 choices, and second 2 choices.  
`3 × 2 = 6` valid configurations.

---

## Example 3:

**Input:**  
`m = 5, n = 5`  
**Output:**  
`580986`  

---

## Constraints

- `1 <= m <= 5`  
- `1 <= n <= 1000`

---

## Notes

- No two adjacent cells (either horizontally or vertically) can have the same color.
- This is a classic **grid coloring** problem that can be solved using **state compression DP** or **DFS + memoization**.

---

## Tags

`Dynamic Programming` `Grid Coloring` `Combinatorics` `Graph Theory`
