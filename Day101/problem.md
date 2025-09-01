# Day 101 - Maximum Average Pass Ratio

## Problem Statement
There is a school with multiple classes, each having a final exam.  
You are given a 2D array `classes`, where:
- `classes[i] = [passi, totali]`
- `passi` = number of students passing
- `totali` = total students in the class

You also have `extraStudents` brilliant students who are guaranteed to pass any exam.  
Your goal is to distribute these `extraStudents` among classes to **maximize the average pass ratio** across all classes.

- **Pass Ratio of a class:** `passi / totali`
- **Average Pass Ratio:** `(sum of all pass ratios) / number of classes`

Return the **maximum possible average pass ratio** after optimal distribution.  
Answers within `1e-5` are accepted.

---

## Examples

### Example 1
**Input:**
```

classes = \[\[1,2],\[3,5],\[2,2]]
extraStudents = 2

```

**Output:**
```

0.78333

```

**Explanation:**
- Assign both students to class `[1,2]` → becomes `[3,4]`
- Ratios: `3/4, 3/5, 2/2`
- Average = `(0.75 + 0.6 + 1.0) / 3 = 0.78333`

---

### Example 2
**Input:**
```

classes = \[\[2,4],\[3,9],\[4,5],\[2,10]]
extraStudents = 4

```

**Output:**
```

0.53485

````

---

## Constraints
- `1 <= classes.length <= 1e5`
- `classes[i].length == 2`
- `1 <= passi <= totali <= 1e5
- `1 <= extraStudents <= 1e5`
