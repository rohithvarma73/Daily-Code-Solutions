from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Create a list of tuples containing the value and its original index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort the list in descending order based on the value
        indexed_nums.sort(key=lambda x: -x[0])
        
        # Take the top k elements
        top_k = indexed_nums[:k]
        
        # Sort these elements based on their original indices to maintain the order
        top_k.sort(key=lambda x: x[1])
        
        # Extract the values to form the subsequence
        result = [num for num, index in top_k]
        
        return result