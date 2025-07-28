from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Initialize the maximum OR value and answer to zero.
        max_or_value = answer = 0

        # Compute the maximum OR value across all numbers in the list.
        for num in nums:
            max_or_value |= num

        # Define the depth-first search function to explore all subsets.
        def dfs(index, current_or):
            nonlocal max_or_value, answer  # Access variables from the outer scope.
          
            # Base case: if the index is equal to the length of nums,
            # we've considered all elements.
            if index == len(nums):
                # If the current OR is equal to the max OR value, increment the answer.
                if current_or == max_or_value:
                    answer += 1
                return
          
            # Recursive call to explore the subset without including the current number.
            dfs(index + 1, current_or)
          
            # Recursive call to explore the subset including the current number.
            dfs(index + 1, current_or | nums[index])

        # Begin the depth-first search with the first index and an initial OR value of 0.
        dfs(0, 0)
      
        # Return the total count of subsets that have the maximum OR value.
        return answer

# The Solution can now be used to create an instance and call the countMaxOrSubsets method.