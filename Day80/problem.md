# Day 80: Find the Maximum Number of Fruits Collected

**Difficulty**: Hard  
**Topics**: Dynamic Programming, 2D Grid  
**Companies**: 🔒 Premium  
**Hint Available**

---

## Problem

There is a game dungeon comprised of `n x n` rooms arranged in a grid.

You are given a 2D array `fruits` of size `n x n`, where `fruits[i][j]` represents the number of fruits in the room `(i, j)`.

Three children will play in the dungeon, starting from the following positions:

- Child 1: Top-left corner → `(0, 0)`
- Child 2: Top-right corner → `(0, n - 1)`
- Child 3: Bottom-left corner → `(n - 1, 0)`

They will **each make exactly `n - 1` moves** to reach the bottom-right corner `(n - 1, n - 1)` following these rules:

### Movement Rules:

- **Child 1** (from `(0, 0)`):  
  Can move to:  
  - `(i + 1, j + 1)`  
  - `(i + 1, j)`  
  - `(i, j + 1)`

- **Child 2** (from `(0, n - 1)`):  
  Can move to:  
  - `(i + 1, j - 1)`  
  - `(i + 1, j)`  
  - `(i + 1, j + 1)`

- **Child 3** (from `(n - 1, 0)`):  
  Can move to:  
  - `(i - 1, j + 1)`  
  - `(i, j + 1)`  
  - `(i + 1, j + 1)`

Each child collects all the fruits from the rooms they visit.  
If **two or more children enter the same room**, **only one** collects the fruits, and the room is emptied after.

---

## Return

The **maximum number of fruits** the children can collect from the dungeon.

---

## Examples

### Example 1

**Input**:  
`fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]`

**Output**:  
`100`

**Explanation**:
- Child 1 (green): `(0,0) → (1,1) → (2,2) → (3,3)`  
- Child 2 (red): `(0,3) → (1,2) → (2,3) → (3,3)`  
- Child 3 (blue): `(3,0) → (3,1) → (3,2) → (3,3)`

Fruits collected:  
`1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100`

---

### Example 2

**Input**:  
`fruits = [[1,1],[1,1]]`

**Output**:  
`4`

**Explanation**:
- Child 1: `(0,0) → (1,1)`
- Child 2: `(0,1) → (1,1)`
- Child 3: `(1,0) → (1,1)`

They collect: `1 + 1 + 1 + 1 = 4`

---

## Constraints

- `2 <= n == fruits.length == fruits[i].length <= 1000`
- `0 <= fruits[i][j] <= 1000`
