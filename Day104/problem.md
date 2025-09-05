# Day104 – Minimum Operations to Make the Integer Zero
**Solved – Medium**

---

### Problem

You are given two integers `num1` and `num2`.

In one operation, you can choose an integer `i` in the range `[0, 60]` and subtract  
`(2^i + num2)` from `num1`.

Return the minimum number of operations needed to make `num1` equal to `0`.  

If it is impossible to make `num1` equal to `0`, return `-1`.

---

### Example 1

**Input:**
```python
num1 = 3, num2 = -2
````

**Output:**

```python
3
```

**Explanation:**
We can make `3` equal to `0` with the following operations:

* Choose `i = 2`: `3 - (2^2 + (-2)) = 3 - (4 - 2) = 1`
* Choose `i = 2`: `1 - (2^2 + (-2)) = 1 - (4 - 2) = -1`
* Choose `i = 0`: `-1 - (2^0 + (-2)) = -1 - (1 - 2) = 0`

Thus, 3 operations are required.

---

### Example 2

**Input:**

```python
num1 = 5, num2 = 7
```

**Output:**

```python
-1
```

**Explanation:**
It is impossible to make `5` equal to `0` with the given operation.

---

### Constraints

* `1 <= num1 <= 10^9`
* `-10^9 <= num2 <= 10^9`

