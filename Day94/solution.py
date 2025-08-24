from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Determine the length of the nums list
        n = len(nums)

        # Initialize two lists to keep track of consecutive ones to the left and right of each index
        left_ones_count = [0] * n
        right_ones_count = [0] * n

        # Calculate the consecutive ones to the left of each index
        for i in range(1, n):
            if nums[i - 1] == 1:
                left_ones_count[i] = left_ones_count[i - 1] + 1

        # Calculate the consecutive ones to the right of each index
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right_ones_count[i] = right_ones_count[i + 1] + 1

        # Find the maximum length subarray formed by summing up counts of left and right ones.
        # Note that the question assumes we can remove one zero to maximize the length.
        # So, connecting two streaks of ones effectively means removing one zero between them.
        max_length = max(a + b for a, b in zip(left_ones_count, right_ones_count))

        return max_length