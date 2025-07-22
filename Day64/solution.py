from collections import defaultdict
from itertools import accumulate

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # Initialize a dictionary to store the most recent index of each number
        index_dict = defaultdict(int)
        # Create a prefix sum array with an initial value of 0 for convenience
        prefix_sums = list(accumulate(nums, initial=0))
        # Initialize the maximum subarray sum and the start index for the subarray
        max_sum = start_index = 0
      
        # Iterate over the numbers alongside their indices (starting from 1)
        for current_index, value in enumerate(nums, 1):
            # Update the start index to the maximum of the current start_index and the next index
            # after the previous occurrence of the current value
            start_index = max(start_index, index_dict[value])
            # Update the maximum sum if the current subarray sum is greater
            current_subarray_sum = prefix_sums[current_index] - prefix_sums[start_index]
            max_sum = max(max_sum, current_subarray_sum)
            # Update the dictionary with the current index of the value
            index_dict[value] = current_index
      
        # Return the maximum subarray sum containing unique elements
        return max_sum