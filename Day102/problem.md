# Day102: Find the Number of Ways to Place People I

**Difficulty:** Medium  
**Status:** Attempted  
**Topics:** Geometry, Hashing  
**Companies:** 🔒 Premium Problem  

---

## Problem Statement

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D plane, where `points[i] = [xi, yi]`.

Count the number of pairs of points `(A, B)`, where:

1. `A` is on the **upper left side** of `B`, and  
2. There are **no other points** in the rectangle (or line) they make (**including the border**).  

Return the count.

---

## Examples

### Example 1
**Input:**
```
points = [[1,1],[2,2],[3,3]]
```
**Output:**
```
0
```
**Explanation:**  
There is no way to choose A and B so A is on the upper left side of B.

---

### Example 2
**Input:**
```
points = [[6,2],[4,4],[2,6]]
```
**Output:**
```
2
```
**Explanation:**  
- Pair `(points[1], points[0])` → valid  
- Pair `(points[2], points[1])` → valid  
- Pair `(points[2], points[0])` → invalid because `points[1]` lies inside the rectangle  

---

### Example 3
**Input:**
```
points = [[3,1],[1,3],[1,1]]
```
**Output:**
```
2
```
**Explanation:**  
- Pair `(points[2], points[0])` → valid (even if they form a line)  
- Pair `(points[1], points[2])` → valid  
- Pair `(points[1], points[0])` → invalid because `points[2]` lies on the border  

---

## Constraints

- `2 <= n <= 50`
- `points[i].length == 2`
- `0 <= points[i][0], points[i][1] <= 50`
- All `points[i]` are **distinct**.

---
