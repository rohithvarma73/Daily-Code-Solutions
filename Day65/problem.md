# Day 65: Maximum Score From Removing Substrings  
**Difficulty**: Medium  

---

### 🧠 Topics  
**Companies**: *(Not disclosed)*  
**Hint**:  

You are given a string `s` and two integers `x` and `y`.  
You can perform two types of operations any number of times:

- Remove substring `"ab"` and gain `x` points.  
  > Example: removing `"ab"` from `"cabxbae"` → `"cxbae"`  

- Remove substring `"ba"` and gain `y` points.  
  > Example: removing `"ba"` from `"cabxbae"` → `"cabxe"`  

Return the **maximum points** you can gain after applying the above operations on `s`.

---

### 📘 Examples

**Example 1:**
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:

Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab", score = 5

Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa", score = 4

Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba", score = 5

Remove the "ba" underlined in "cdbcba". Now, s = "cdbc", score = 5
Total Score = 5 + 4 + 5 + 5 = 19


**Example 2:**
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20

---

### 📋 Constraints:
- `1 <= s.length <= 10⁵`  
- `1 <= x, y <= 10⁴`  
- `s` consists of lowercase English letters only.
