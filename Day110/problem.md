# Day110 Vowel Spellchecker

**Medium**

---

## Problem Statement

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

1. **Capitalization**  
   If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.  

   Examples:
   - wordlist = `["yellow"]`, query = `"YellOw"` → correct = `"yellow"`  
   - wordlist = `["Yellow"]`, query = `"yellow"` → correct = `"Yellow"`  
   - wordlist = `["yellow"]`, query = `"yellow"` → correct = `"yellow"`  

2. **Vowel Errors**  
   If after replacing the vowels (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`) of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.  

   Examples:
   - wordlist = `["YellOw"]`, query = `"yollow"` → correct = `"YellOw"`  
   - wordlist = `["YellOw"]`, query = `"yeellow"` → correct = `""` (no match)  
   - wordlist = `["YellOw"]`, query = `"yllw"` → correct = `""` (no match)  

---

## Precedence Rules

The spellchecker works in the following order:

1. When the query **exactly matches** a word in the wordlist (case-sensitive), return the same word back.  
2. When the query matches a word **up to capitalization**, return the first such match in the wordlist.  
3. When the query matches a word **up to vowel errors**, return the first such match in the wordlist.  
4. If the query has no matches in the wordlist, return the empty string `""`.  

---

## Examples

### Example 1

**Input:**  
```

wordlist = \["KiTe","kite","hare","Hare"]
queries = \["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

```

**Output:**  
```

\["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

```

---

### Example 2

**Input:**  
```

wordlist = \["yellow"]
queries = \["YellOw"]

```

**Output:**  
```

\["yellow"]

```

---

## Constraints

- `1 <= wordlist.length, queries.length <= 5000`  
- `1 <= wordlist[i].length, queries[i].length <= 7`  
- `wordlist[i]` and `queries[i]` consist only of **English letters**.  
