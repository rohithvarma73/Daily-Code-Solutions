## 29. Divide Two Integers  
**Medium**  
**Topics**: Math, Bit Manipulation  

### Problem Statement  
Given two integers `dividend` and `divisor`, divide them **without using** multiplication (`*`), division (`/`), or mod (`%`) operators.

The integer division should **truncate toward zero**, meaning it drops the fractional part.  
- For example: `8.345` becomes `8`, and `-2.7335` becomes `-2`.

Return the **quotient** after dividing `dividend` by `divisor`.

**Note**:  
Assume we are working in an environment that stores only 32-bit signed integers.  
- The result must be in the range **[−2³¹, 2³¹ − 1]**.  
- If the result exceeds this range, return **2³¹ − 1**.

---

### Examples

#### Example 1:
**Input**:  
`dividend = 10`, `divisor = 3`  
**Output**:  
`3`  
**Explanation**:  
10 / 3 = 3.333... which is truncated to 3.

#### Example 2:
**Input**:  
`dividend = 7`, `divisor = -3`  
**Output**:  
`-2`  
**Explanation**:  
7 / -3 = -2.333... which is truncated to -2.

---

### Constraints:
- −2³¹ ≤ `dividend`, `divisor` ≤ 2³¹ − 1  
- `divisor` ≠ 0
