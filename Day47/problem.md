# Day 47: Find the K-th Character in String Game I

**Solved**  
**Difficulty**: Easy  
**Topics**:  
**Companies**:  
**Hint**:  

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a positive integer `k`.

Now Bob will ask Alice to perform the following operation **forever**:

> Generate a new string by changing each character in `word` to its next character in the English alphabet, and append it to the original word.

For example:
- Performing the operation on `"c"` generates `"cd"`.
- Performing the operation on `"zb"` generates `"zbac"`.

Return the value of the **k-th character** in `word`, after enough operations have been done for `word` to have at least `k` characters.

**Note**: The character `'z'` wraps around to `'a'` in the operation.

---

### Examples

#### Example 1:

Input: k = 5
Output: "b"

Explanation:
Initially, word = "a"
We perform the operation three times:

word = "a" → "ab" (append next of 'a' = 'b')

word = "ab" → "abbc" (append nexts of 'a', 'b' = "bc")

word = "abbc" → "abbcbccd" (append nexts of 'a', 'b', 'b', 'c' = "bccd")


So the 5th character is `'b'`.

---

#### Example 2:

Input: k = 10
Output: "c"


---

### Constraints

- 1 <= k <= 500
