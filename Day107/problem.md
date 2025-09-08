# Day107 – Convert Integer to the Sum of Two No-Zero Integers
**Solved – Easy**

---

### Problem

A **No-Zero integer** is a positive integer that does not contain any `0` in its decimal representation.

Given an integer `n`, return a list of two integers `[a, b]` where:

- `a` and `b` are **No-Zero integers**.  
- `a + b = n`.

The test cases are generated so that there is **at least one valid solution**.  
If there are many valid solutions, you can return **any of them**.

---

### Example 1

**Input:**
```python
n = 2
````

**Output:**

```python
[1, 1]
```

**Explanation:**
Let `a = 1` and `b = 1`.
Both `a` and `b` are No-Zero integers, and `a + b = 2 = n`.

---

### Example 2

**Input:**

```python
n = 11
```

**Output:**

```python
[2, 9]
```

**Explanation:**
Let `a = 2` and `b = 9`.
Both are No-Zero integers, and `a + b = 11 = n`.
Other valid answers such as `[8, 3]` are also accepted.

---

### Constraints

* `2 <= n <= 10^4`

