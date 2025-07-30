from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Find the maximum value in the array nums.
        max_value = max(nums)
      
        # Initialize the longest length and the current length counter to zero.
        longest_length = current_length = 0
      
        # Iterate through each element in the list.
        for number in nums:
            # If the current element is equal to the maximum value...
            if number == max_value:
                # Increment the current length counter.
                current_length += 1
                # Update the longest length if the current length is greater.
                longest_length = max(longest_length, current_length)
            else:
                # If the current element is not equal to the max value, reset current length to 0.
                current_length = 0
              
        # After iterating through the list, return the longest length of the subarray with max values.
        return longest_length