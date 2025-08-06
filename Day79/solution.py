from typing import List

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n * 4)
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = nums[lo]
            return
        mid = (lo + hi) // 2
        self._build(nums, 2 * tree_index + 1, lo, mid)
        self._build(nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = max(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def update(self, i: int, val: int):
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, tree_index, lo, hi, i, val):
        if lo == hi:
            self.tree[tree_index] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self._update(2 * tree_index + 1, lo, mid, i, val)
        else:
            self._update(2 * tree_index + 2, mid + 1, hi, i, val)
        self.tree[tree_index] = max(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

    def query_first(self, target: int) -> int:
        return self._query_first(0, 0, self.n - 1, target)

    def _query_first(self, tree_index, lo, hi, target):
        if self.tree[tree_index] < target:
            return -1
        if lo == hi:
            # Found a valid basket, mark as used
            self.update(lo, -1)
            return lo
        mid = (lo + hi) // 2
        left_child = self.tree[2 * tree_index + 1]
        if left_child >= target:
            return self._query_first(2 * tree_index + 1, lo, mid, target)
        else:
            return self._query_first(2 * tree_index + 2, mid + 1, hi, target)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        tree = SegmentTree(baskets)
        for fruit in fruits:
            if tree.query_first(fruit) == -1:
                ans += 1
        return ans
