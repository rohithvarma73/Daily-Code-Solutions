from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Count the frequency of each element in the array
        frequency_counter = Counter(nums)
      
        # Find the maximum frequency among all elements
        max_frequency = max(frequency_counter.values())
      
        # Calculate the sum of frequencies for all elements that have the maximum frequency
        # This gives us the total count of elements with maximum frequency
        total_count = sum(freq for freq in frequency_counter.values() if freq == max_frequency)
      
        return total_count