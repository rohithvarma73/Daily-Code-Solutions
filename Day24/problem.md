# Day 24 - Find Closest Node to Given Two Nodes

## Problem Description

You are given a **directed graph** of `n` nodes numbered from `0` to `n - 1`, where **each node has at most one outgoing edge**.

The graph is represented with a given 0-indexed array `edges` of size `n`, indicating that there is a directed edge from node `i` to node `edges[i]`.  
If there is **no outgoing edge** from `i`, then `edges[i] == -1`.

You are also given two integers `node1` and `node2`.

---

### Objective

Return the **index of the node** that can be reached from both `node1` and `node2`, such that the **maximum** between the distance from `node1` to that node, and from `node2` to that node is **minimized**.

If there are **multiple answers**, return the node with the **smallest index**.  
If **no such node** exists, return `-1`.

> Note: `edges` may contain **cycles**.

---

## Input

- A 0-indexed integer array `edges` of length `n`, where `edges[i]` represents the next node from node `i`, or -1 if there is no outgoing edge.
- Two integers `node1` and `node2`, representing starting nodes.

---

## Output

- An integer representing the node that is reachable from both `node1` and `node2` such that the maximum of the distances is minimized. Return `-1` if no such node exists.

---

## Examples

### Example 1

**Input:**

edges = [2,2,3,-1]
node1 = 0
node2 = 1


**Output:**

2


**Explanation:**

- Distance from `node0` to `2` = 1  
- Distance from `node1` to `2` = 1  
- Max distance = 1 → Minimum possible  
- Return node 2

---

### Example 2

**Input:**

edges = [1,2,-1]
node1 = 0
node2 = 2


**Output:**

2


**Explanation:**

- Distance from `node0` to `2` = 2  
- Distance from `node2` to `2` = 0  
- Max distance = 2 → Best possible  
- Return node 2

---

## Constraints

- `n == edges.length`
- `2 <= n <= 10^5`
- `-1 <= edges[i] < n`
- `edges[i] != i`
- `0 <= node1, node2 < n`
