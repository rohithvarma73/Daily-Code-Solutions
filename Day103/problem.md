# Day103 – Find the Number of Ways to Place People II

**Solved – Hard**

---

### Problem

You are given a 2D array `points` of size `n x 2` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

We define directions:

* Right → increasing `x`
* Left → decreasing `x`
* Up → increasing `y`
* Down → decreasing `y`

We need to place **n people**, including **Alice** and **Bob**, at these points such that there is **exactly one person at every point**.

Alice wants to be alone with Bob, so she will build a **rectangular fence**:

* Alice’s position = **upper-left corner**
* Bob’s position = **lower-right corner**

⚠️ If any other person lies **inside or on the fence**, Alice becomes **sad**.

Return the number of **valid pairs (Alice, Bob)** such that Alice is not sad.

---

### Example 1

**Input:**

```python
points = [[1,1],[2,2],[3,3]]
```

**Output:**

```python
0
```

**Explanation:**
No way to place Alice and Bob without enclosing another person.

---

### Example 2

**Input:**

```python
points = [[6,2],[4,4],[2,6]]
```

**Output:**

```python
2
```

**Explanation:**
Valid placements:

* Alice `(4,4)` → Bob `(6,2)`
* Alice `(2,6)` → Bob `(4,4)`
  Not valid: `(2,6)` & `(6,2)` because `(4,4)` is inside fence.

---

### Example 3

**Input:**

```python
points = [[3,1],[1,3],[1,1]]
```

**Output:**

```python
2
```

**Explanation:**
Valid:

* Alice `(1,1)` → Bob `(3,1)`
* Alice `(1,3)` → Bob `(1,1)`
  Invalid: `(1,3)` → `(3,1)` because `(1,1)` lies on fence.

---

### Constraints

* `2 <= n <= 1000`
* `points[i].length == 2`
* `-10^9 <= xi, yi <= 10^9`
* All points are **distinct**

