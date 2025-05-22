# Day 22: Next Permutation

## 📘 Problem Statement

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`:  
- `[1,2,3]`  
- `[1,3,2]`  
- `[2,1,3]`  
- `[2,3,1]`  
- `[3,1,2]`  
- `[3,2,1]`

The **next permutation** of an array of integers is the next lexicographically greater permutation of its elements.  
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container.  
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

## 🧠 Examples

### Example 1:
**Input:**  
`nums = [1,2,3]`  
**Output:**  
`[1,3,2]`

### Example 2:
**Input:**  
`nums = [3,2,1]`  
**Output:**  
`[1,2,3]`

### Example 3:
**Input:**  
`nums = [1,1,5]`  
**Output:**  
`[1,5,1]`

## 📋 Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

---

## 🧩 Approach

To generate the next lexicographical permutation:

1. Traverse the array from **right to left** to find the first index `i` such that `nums[i] < nums[i+1]`.
2. If such an index exists:
   - Find the smallest number **greater than** `nums[i]` from the right subarray (`nums[i+1:]`).
   - Swap those two elements.
3. Reverse the subarray `nums[i+1:]` to get the next smallest lexicographic order.
4. If no such index exists (i.e., the array is in descending order), reverse the entire array to get the smallest permutation.
