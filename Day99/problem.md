# Day 99 - Alice and Bob Playing Flower Game

**Solved**  
**Medium**  
**Topics:** Game Theory, Math  

---

## Problem Statement

Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them.  
- There are `x` flowers in the first lane between Alice and Bob, and `y` flowers in the second lane.  
- The game proceeds as follows:
  1. Alice takes the first turn.  
  2. In each turn, a player must choose one of the lanes and pick **one flower** from that side.  
  3. At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.  

Given two integers `n` and `m`, the task is to compute the number of possible pairs `(x, y)` that satisfy the conditions:  
- Alice **must win** the game according to the rules.  
- `x ∈ [1, n]`  
- `y ∈ [1, m]`  

Return the number of possible pairs `(x, y)` that satisfy the conditions.  

---

## Examples

### Example 1
**Input:**  
```

n = 3, m = 2

```

**Output:**  
```

3

```

**Explanation:**  
The following pairs satisfy the condition where Alice wins:  
- (1, 2)  
- (3, 2)  
- (2, 1)  

---

### Example 2
**Input:**  
```

n = 1, m = 1

```

**Output:**  
```

0

```

**Explanation:**  
No pairs satisfy the conditions for Alice to win.  

---

## Constraints
- `1 <= n, m <= 10^5`

