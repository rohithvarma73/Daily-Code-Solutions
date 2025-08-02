# Day75 Rearranging Fruits

**Difficulty**: Hard  
**Topics**: Arrays, Greedy, Hash Map, Sorting  
**Companies**: 🔒 Premium

---

## Problem

You have two fruit baskets containing `n` fruits each.  
You are given two 0-indexed integer arrays `basket1` and `basket2` representing the **cost of each fruit** in both baskets.

You want to make both baskets **equal**. To do so, you can use the following operation as many times as you want:

- Choose two indices `i` and `j`, and **swap** the `i`-th fruit of `basket1` with the `j`-th fruit of `basket2`.
- The **cost** of the swap is `min(basket1[i], basket2[j])`.

> Two baskets are considered equal if, after sorting them, they are exactly the same.

Return the **minimum cost** to make both baskets equal or `-1` if impossible.

---

## Examples

### Example 1

**Input**:  
`basket1 = [4, 2, 2, 2]`  
`basket2 = [1, 4, 1, 2]`

**Output**:  
`1`

**Explanation**:  
Swap index 1 of `basket1` with index 0 of `basket2`, which costs `1`.  
Now:  
- `basket1 = [4, 1, 2, 2]`  
- `basket2 = [2, 4, 1, 2]`  
After sorting, both become `[1, 2, 2, 4]`.

---

### Example 2

**Input**:  
`basket1 = [2, 3, 4, 1]`  
`basket2 = [3, 2, 5, 1]`

**Output**:  
`-1`

**Explanation**:  
It is impossible to make both baskets equal with any number of swaps.

---

## Constraints

- `basket1.length == basket2.length`
- `1 <= basket1.length <= 10^5`
- `1 <= basket1[i], basket2[i] <= 10^9`
