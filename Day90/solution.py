from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6  # floating point tolerance

        def dfs(nums: List[float]) -> bool:
            # base case: one number left
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            # try all pairs
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    # possible next numbers after applying op on nums[i], nums[j]
                    a, b = nums[i], nums[j]
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]

                    for val in [
                        a + b,
                        a - b,
                        b - a,
                        a * b,
                    ]:
                        if dfs(next_nums + [val]):
                            return True

                    if abs(b) > EPSILON and dfs(next_nums + [a / b]):
                        return True
                    if abs(a) > EPSILON and dfs(next_nums + [b / a]):
                        return True
            return False

        return dfs([float(x) for x in cards])
