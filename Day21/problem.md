# Day 21: Type of Triangle

**Difficulty**: Easy  
**Topics**: Geometry, Arrays  
**Hint**: Check triangle inequality and side equality conditions

---

You are given a 0-indexed integer array `nums` of size 3 which can form the sides of a triangle.

A triangle is called:
- **Equilateral** if it has all sides of equal length.
- **Isosceles** if it has exactly two sides of equal length.
- **Scalene** if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or `"none"` if it cannot form a triangle.

---

### Example 1:

**Input:**  
`nums = [3,3,3]`

**Output:**  
`"equilateral"`

**Explanation:**  
All sides are equal, so it forms an equilateral triangle.

---

### Example 2:

**Input:**  
`nums = [3,4,5]`

**Output:**  
`"scalene"`

**Explanation:**  
- 3 + 4 > 5  
- 3 + 5 > 4  
- 4 + 5 > 3  
Since the triangle inequality holds and all sides are different, it forms a scalene triangle.

---

### Constraints:

- `nums.length == 3`
- `1 <= nums[i] <= 100`
