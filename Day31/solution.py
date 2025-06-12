class Solution(object):
    def maxAdjacentDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize max_diff to 0 to keep track of the maximum absolute difference found
        max_diff = 0
        
        # Get the length of the array to handle circular indexing
        n = len(nums)
        
        # Loop through each element in the array
        for i in range(n):
            # Current element in the array
            current = nums[i]
            
            # Next adjacent element in the circular array. 
            # Using modulo operation to wrap around to the first element after the last
            next_num = nums[(i + 1) % n]
            
            # Calculate the absolute difference between current and next element
            diff = abs(current - next_num)
            
            # Update max_diff if the current difference is larger than the previously recorded max_diff
            if diff > max_diff:
                max_diff = diff
        
        # Return the maximum absolute difference found
        return max_diff