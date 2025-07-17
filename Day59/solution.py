from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Initialize a 2D list (matrix) of size k x k with all values set to 0
        count_matrix = [[0] * k for _ in range(k)]
        max_length = 0
      
        # Traverse through each number in the input list
        for num in nums:
            # Calculate the remainder of the current number with k
            remainder = num % k
          
            # Iterate over each possible remainder
            for j in range(k):
                # Calculate complementary remainder required to form a valid pair with `remainder`
                complement_remainder = (j - remainder + k) % k
              
                # Update the matrix with the new sequence length
                count_matrix[remainder][complement_remainder] = count_matrix[complement_remainder][remainder] + 1
              
                # Update the maximum sequence length found
                max_length = max(max_length, count_matrix[remainder][complement_remainder])
      
        # Return the maximum sequence length found
        return max_length