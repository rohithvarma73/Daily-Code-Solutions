# Day 13 - Problem: Integer to Roman

**Leetcode Problem 12. Integer to Roman**  
**Difficulty:** Medium

---

## Description

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. The rules are:

1. **Regular subtraction**: Keep subtracting the largest Roman symbol less than or equal to the number.
2. **Subtractive form**: If a digit is 4 or 9 (in any decimal place), use a subtractive combination:
   - 4 (IV), 9 (IX)
   - 40 (XL), 90 (XC)
   - 400 (CD), 900 (CM)

### Note:
Only powers of 10 (I, X, C, M) can be used consecutively up to 3 times. You cannot repeat V, L, or D. Use subtractive forms instead.

---

## Examples

### Example 1:
**Input:** `num = 3749`  
**Output:** `"MMMDCCXLIX"`  
**Explanation:**
- 3000 = MMM  
- 700 = DCC  
- 40 = XL  
- 9 = IX  

---

### Example 2:
**Input:** `num = 58`  
**Output:** `"LVIII"`  
**Explanation:**
- 50 = L  
- 8 = VIII  

---

### Example 3:
**Input:** `num = 1994`  
**Output:** `"MCMXCIV"`  
**Explanation:**
- 1000 = M  
- 900 = CM  
- 90 = XC  
- 4 = IV  

---

## Constraints:
- `1 <= num <= 3999`
