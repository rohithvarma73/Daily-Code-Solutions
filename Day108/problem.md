# Day108 – Number of People Aware of a Secret
**Solved – Medium**

---

### Problem

On day 1, one person discovers a secret.

You are given an integer `delay`, which means that each person will **share the secret** with a new person every day, starting from `delay` days after discovering the secret.  

You are also given an integer `forget`, which means that each person will **forget the secret** `forget` days after discovering it.  

A person **cannot share the secret** on the same day they forgot it, or on any day afterwards.

Given an integer `n`, return the **number of people who know the secret at the end of day n**.  

Since the answer may be very large, return it modulo `10^9 + 7`.

---

### Example 1

**Input:**
```python
n = 6, delay = 2, forget = 4
````

**Output:**

```python
5
```

**Explanation:**

* **Day 1:** Suppose the first person is named A. → (1 person)
* **Day 2:** A is the only person who knows the secret. → (1 person)
* **Day 3:** A shares the secret with a new person, B. → (2 people)
* **Day 4:** A shares the secret with a new person, C. → (3 people)
* **Day 5:** A forgets the secret, and B shares with a new person, D. → (3 people)
* **Day 6:** B shares with E, and C shares with F. → (5 people)

---

### Example 2

**Input:**

```python
n = 4, delay = 1, forget = 3
```

**Output:**

```python
6
```

**Explanation:**

* **Day 1:** A knows the secret. → (1 person)
* **Day 2:** A shares with B. → (2 people)
* **Day 3:** A and B share with C and D. → (4 people)
* **Day 4:** A forgets the secret. B, C, and D share with 3 new people. → (6 people)

---

### Constraints

* `2 <= n <= 1000`
* `1 <= delay < forget <= n`
