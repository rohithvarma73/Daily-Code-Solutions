from collections import defaultdict

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Dictionary to store frequency count of each number in nums
        frequency = defaultdict(int)
        
        # Count the frequency of each number
        for num in nums:
            frequency[num] += 1
        
        # Initialize the maximum length of a harmonious subsequence found
        max_length = 0
        
        # Iterate through each unique number in the frequency dictionary
        for num in frequency:
            # Check if there exists a number exactly 1 greater than current number
            # This means num and num + 1 can form a harmonious subsequence
            if num + 1 in frequency:
                # Calculate the length of this subsequence (sum of counts of num and num+1)
                current_length = frequency[num] + frequency[num + 1]
                # Update max_length if this subsequence is longer than the previous ones
                if current_length > max_length:
                    max_length = current_length
        
        # Return the length of the longest harmonious subsequence found
        return max_length
