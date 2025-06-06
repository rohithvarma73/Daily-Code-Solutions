# Day 26: Using a Robot to Print the Lexicographically Smallest String

## Difficulty: Medium  
## Topics: Stack, Greedy, Simulation

---

### Problem Description

You are given a string `s` and a robot that currently holds an empty string `t`.  
Apply one of the following operations **until both `s` and `t` are empty**:

1. **Remove the first character** of the string `s` and give it to the robot.  
   The robot will **append** this character to the string `t`.
2. **Remove the last character** of the string `t` and give it to the robot.  
   The robot will **write this character on paper**.

Return the **lexicographically smallest string** that can be written on the paper.

---

### Example 1:

**Input:**  
`s = "zza"`  
**Output:**  
`"azz"`

**Explanation:**  
Let `p` denote the written string.  
- Initially: `p = ""`, `s = "zza"`, `t = ""`
- Perform operation 1 three times: `p = ""`, `s = ""`, `t = "zza"`
- Perform operation 2 three times: `p = "azz"`, `t = ""`

---

### Example 2:

**Input:**  
`s = "bac"`  
**Output:**  
`"abc"`

**Explanation:**  
Let `p` denote the written string.  
- Perform operation 1 twice: `p = ""`, `s = "c"`, `t = "ba"`  
- Perform operation 2 twice: `p = "ab"`, `s = "c"`, `t = ""`  
- Perform operation 1: `p = "ab"`, `s = ""`, `t = "c"`  
- Perform operation 2: `p = "abc"`, `s = ""`, `t = ""`

---

### Example 3:

**Input:**  
`s = "bdda"`  
**Output:**  
`"addb"`

**Explanation:**  
- Initially: `p = ""`, `s = "bdda"`, `t = ""`
- Perform operation 1 four times: `s = ""`, `t = "bdda"`
- Perform operation 2 four times: `p = "addb"`

---

### Constraints:

- `1 <= s.length <= 10^5`
- `s` consists of only English **lowercase letters**

---

### Tags

`#Greedy` `#Stack` `#String` `#Simulation`

