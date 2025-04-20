from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the index of numbers
        num_map = {}
        
        # Iterate through the list with both index and value
        for i, num in enumerate(nums):
            # Calculate the complement (target - num)
            complement = target - num
            
            # If the complement is already in the map, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the number and its index in the map
            num_map[num] = i
        
        # Return empty if no solution (This case should not occur per the problem)
        return []
