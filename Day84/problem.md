# Day 84: Ways to Express an Integer as Sum of Powers

**Difficulty**: Medium  
**Topics**: Dynamic Programming, Combinatorics, Number Theory  
**Companies**: 🔒 Premium

---

## Problem

You are given two positive integers `n` and `x`.  

Return the **number of ways** `n` can be expressed as the sum of the **x-th power** of **unique positive integers**.  

Formally, we count the number of unique sets of integers `[n1, n2, ..., nk]` such that:

```

n = n1^x + n2^x + ... + nk^x

````

Since the result may be very large, return it modulo `10^9 + 7`.

---

## Example 1
**Input**:  
`n = 10`, `x = 2`

**Output**:  
`1`

**Explanation**:  
Only one valid expression:  
`10 = 3^2 + 1^2`

---

## Example 2
**Input**:  
`n = 4`, `x = 1`

**Output**:  
`2`

**Explanation**:  
Two valid expressions:  
- `4 = 4^1`  
- `4 = 3^1 + 1^1`

---

## Constraints
- `1 <= n <= 300`
- `1 <= x <= 5`
