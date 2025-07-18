from heapq import heappush, heappop

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        total_elements = len(nums)
        one_third_length = total_elements // 3  # Calculate the size of one-third of the array

        prefix_sum = 0
        max_heap_prefix = []  # Heap to keep track of the largest 'n' elements in the prefix
        prefix_sums = [0] * (total_elements + 1)  # Initialize prefix sum array
      
        # Calculate prefix sums and maintain the heap with the largest 'n' elements
        for i in range(1, one_third_length * 2 + 1):
            prefix_sum += nums[i - 1]
            heappush(max_heap_prefix, -nums[i - 1])  # Push the negation to use min-heap as max-heap
            if len(max_heap_prefix) > one_third_length:
                prefix_sum += heappop(max_heap_prefix)  # Pop the smallest (most negative) when heap size exceeds 'n'
            prefix_sums[i] = prefix_sum
      
        suffix_sum = 0
        min_heap_suffix = []  # Heap to keep track of the smallest 'n' elements in the suffix
        suffix_sums = [0] * (total_elements + 1)  # Initialize suffix sum array
      
        # Calculate suffix sums and maintain the heap with the smallest 'n' elements
        for i in range(total_elements, one_third_length - 1, -1):
            suffix_sum += nums[i - 1]
            heappush(min_heap_suffix, nums[i - 1])
            if len(min_heap_suffix) > one_third_length:
                suffix_sum -= heappop(min_heap_suffix)  # Pop the largest when heap size exceeds 'n'
            suffix_sums[i] = suffix_sum
      
        # Find the minimum difference between the prefix and suffix sums
        min_difference = float('inf')  # Start with an infinitely large difference
        for i in range(one_third_length, one_third_length * 2 + 1):
            min_difference = min(min_difference, prefix_sums[i] - suffix_sums[i + 1])  # Compare and store the minimum
      
        return min_difference