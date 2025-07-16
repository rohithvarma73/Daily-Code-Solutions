from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        # Initialize a 2D list to keep track of sequences with different remainders
        remainder_count = [[0] * k for _ in range(k)]
        max_length = 0
      
        # Iterate through each number in the list
        for num in nums:
            # Calculate the remainder of the current number when divided by k
            remainder = num % k
            # Update dp table for current number
            for j in range(k):
                previous_remainder = (j - remainder + k) % k
                remainder_count[remainder][previous_remainder] = remainder_count[previous_remainder][remainder] + 1
                # Update the maximum length found so far
                max_length = max(max_length, remainder_count[remainder][previous_remainder])
      
        return max_length