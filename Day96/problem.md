# Day96: Maximum Area of Longest Diagonal Rectangle

**Problem:**  
You are given a 2D 0-indexed integer array `dimensions`.

For all indices `i`, `0 <= i < dimensions.length`, `dimensions[i][0]` represents the length and `dimensions[i][1]` represents the width of the rectangle `i`.

Return the area of the rectangle having the longest diagonal.  
If there are multiple rectangles with the longest diagonal, return the area of the rectangle having the maximum area.

---

### Example 1:
**Input:**
```
dimensions = [[9,3],[8,6]]
```
**Output:**
```
48
```
**Explanation:**  
- For index = 0: length = 9, width = 3 → diagonal = sqrt(9² + 3²) = sqrt(90) ≈ 9.487  
- For index = 1: length = 8, width = 6 → diagonal = sqrt(8² + 6²) = sqrt(100) = 10  

Rectangle at index 1 has a greater diagonal, so return area = 8 × 6 = **48**.

---

### Example 2:
**Input:**
```
dimensions = [[3,4],[4,3]]
```
**Output:**
```
12
```
**Explanation:**  
Both have diagonal = 5, so choose the one with **maximum area = 12**.

---

### Constraints:
- 1 <= dimensions.length <= 100  
- dimensions[i].length == 2  
- 1 <= dimensions[i][0], dimensions[i][1] <= 100  

---

## Python Solution

```python
import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        max_diag = 0
        max_area = 0
        
        for length, width in dimensions:
            diag = math.sqrt(length * length + width * width)
            area = length * width
            
            if diag > max_diag:
                max_diag = diag
                max_area = area
            elif diag == max_diag:
                max_area = max(max_area, area)
        
        return max_area
```
