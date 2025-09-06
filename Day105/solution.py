import math
from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # Precompute ranges where step count stays constant
        # steps = ceil(log4(x+1))
        ranges = []
        limit = 10**9 + 5
        k = 1
        prev = 1
        while prev <= limit:
            nxt = 4**k - 1
            ranges.append((prev, min(nxt, limit), k))  # [prev, nxt] needs k steps
            prev = nxt + 1
            k += 1

        ans = 0
        for l, r in queries:
            total_steps = 0
            for start, end, steps in ranges:
                if end < l or start > r:
                    continue
                overlap_l = max(l, start)
                overlap_r = min(r, end)
                count = overlap_r - overlap_l + 1
                if count > 0:
                    total_steps += count * steps
            ans += (total_steps + 1) // 2  # ceil(total_steps/2)
        return ans
