# Day 22 - Zero Array Transformation III

**Difficulty:** Medium  
**Topics:** Arrays, Greedy, Interval Management

---

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [li, ri]`.

Each `queries[i]` represents the following action on `nums`:

Decrement the value at each index in the range `[li, ri]` in `nums` by **at most** 1.  
The amount by which the value is decremented can be chosen independently for each index.

A **Zero Array** is an array with all its elements equal to `0`.

Your task is to return the **maximum number of elements that can be removed from `queries`**, such that `nums` can still be converted to a zero array using the remaining queries.  

If it is **not possible** to convert `nums` to a zero array even using all queries, return `-1`.

---

## Examples

**Input:** `nums = [2, 0, 2]`, `queries = [[0, 2], [0, 2], [1, 1]]`  
**Output:** `1`  
**Explanation:** After removing queries[2], we can use queries[0] and [1] to decrement nums[0] and nums[2] by 1 each in both queries. Final result: `[0, 0, 0]`.

**Input:** `nums = [1, 1, 1, 1]`, `queries = [[1, 3], [0, 2], [1, 3], [1, 2]]`  
**Output:** `2`  
**Explanation:** We can remove queries[2] and [3] and still cover all indices with exactly 1 decrement per index.

**Input:** `nums = [1, 2, 3, 4]`, `queries = [[0, 3]]`  
**Output:** `-1`  
**Explanation:** A single query can't reduce values like 4 down to 0. Not possible to form zero array.

---

## Constraints

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`
- `1 <= queries.length <= 1000`
- `0 <= li <= ri < nums.length`

---

## Notes

- This problem involves determining the minimum number of range decrements needed per index.
- Think in terms of how many total "decrements" are needed per index and whether the available ranges cover them.
- The solution may use greedy logic, prefix sums, and efficient simulation.

---
