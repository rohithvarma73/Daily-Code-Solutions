# Day76: Maximum Fruits Harvested After at Most K Steps

**Difficulty**: Hard  
**Topics**: Arrays, Sliding Window, Binary Search  
**Companies**: 🔒 Premium

---

## Problem

Fruits are available at some positions on an infinite x-axis.  
You are given a **2D integer array** `fruits`, where `fruits[i] = [positioni, amounti]` represents `amounti` fruits at the position `positioni`.

- The `fruits` array is **already sorted** by `positioni` in ascending order, and each position is **unique**.
- You are also given:
  - an integer `startPos`: your starting position,
  - an integer `k`: the maximum number of **steps** you can take.

From any position, you can **walk to the left or right**, one unit at a time.  
For every position you reach, you **harvest all the fruits** at that position.  
Fruits **disappear** once harvested.

### Goal:
Return the **maximum total number of fruits** you can harvest **after at most `k` steps**.

---

## Examples

### Example 1

**Input**:  
`fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4`  
**Output**: `9`  

**Explanation**:  
Optimal path:  
- Move right to 6 (3 fruits)  
- Move right to 8 (6 fruits)  
You moved `3` steps and harvested `3 + 6 = 9` fruits.

---

### Example 2

**Input**:  
`fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4`  
**Output**: `14`  

**Explanation**:  
You can move at most `4` steps. You can't reach position `0` or `10`.  
Optimal path:  
- Start at 5 (7 fruits)  
- Left to 4 (1 fruit)  
- Right to 6 (2 fruits)  
- Right to 7 (4 fruits)  
Total steps = `1 + 3 = 4`, fruits = `7 + 1 + 2 + 4 = 14`.

---

### Example 3

**Input**:  
`fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2`  
**Output**: `0`  

**Explanation**:  
You can't reach any position with fruits in 2 steps. So, return `0`.

---

## Constraints

- `1 <= fruits.length <= 10^5`
- `fruits[i].length == 2`
- `0 <= startPos, positioni <= 2 * 10^5`
- `positioni-1 < positioni` (strictly increasing positions)
- `1 <= amounti <= 10^4`
- `0 <= k <= 2 * 10^5`
