# Day105 – Minimum Operations to Make Array Elements Zero
**Attempted – Hard**

---

### Problem

You are given a 2D array `queries`, where `queries[i]` is of the form `[l, r]`.  
Each `queries[i]` defines an array of integers `nums` consisting of elements ranging from `l` to `r` (inclusive).

In **one operation**, you can:

- Select two integers `a` and `b` from the array.  
- Replace them with `floor(a / 4)` and `floor(b / 4)`.

Your task is to determine the **minimum number of operations** required to reduce all elements of the array to `0` for each query.  

Return the **sum of the results for all queries**.

---

### Example 1

**Input:**
```python
queries = [[1,2],[2,4]]
````

**Output:**

```python
3
```

**Explanation:**

* For `queries[0]` → nums = `[1, 2]`

  * Operation 1: select `1` and `2` → `[0, 0]`
  * Minimum operations = **1**

* For `queries[1]` → nums = `[2, 3, 4]`

  * Operation 1: select `2` and `4` → `[0, 3, 1]`
  * Operation 2: select `3` and `1` → `[0, 0, 0]`
  * Minimum operations = **2**

* Total = `1 + 2 = 3`

---

### Example 2

**Input:**

```python
queries = [[2,6]]
```

**Output:**

```python
4
```

**Explanation:**

* For `queries[0]` → nums = `[2, 3, 4, 5, 6]`

  * Operation 1: select `2` and `5` → `[0, 3, 4, 1, 6]`
  * Operation 2: select `4` and `6` → `[0, 3, 1, 1, 1]`
  * Operation 3: select `3` and `1` → `[0, 0, 0, 1, 1]`
  * Operation 4: select `1` and `1` → `[0, 0, 0, 0, 0]`
  * Minimum operations = **4**

---

### Constraints

* `1 <= queries.length <= 10^5`
* `queries[i].length == 2`
* `queries[i] = [l, r]`
* `1 <= l < r <= 10^9`
