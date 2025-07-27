class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Initialize the count of hills and valleys
        count = 0
        # Initialize a pointer to track the last significant number (hill or valley)
        last_significant_number_index = 0
      
        # Iterate over the array starting from the second element and stopping before the last
        for i in range(1, len(nums) - 1):
            # Skip if the current number is the same as the next, as it cannot be a hill or valley
            if nums[i] == nums[i + 1]:
                continue
          
            # Check if the current number is a hill by comparing with the last significant number and next number
            if nums[i] > nums[last_significant_number_index] and nums[i] > nums[i + 1]:
                count += 1
            # Check if the current number is a valley by comparing with the last significant number and next number
            elif nums[i] < nums[last_significant_number_index] and nums[i] < nums[i + 1]:
                count += 1
              
            # Update the pointer to the last significant number as the current number
            last_significant_number_index = i
      
        # Return the total count of hills and valleys found
        return count