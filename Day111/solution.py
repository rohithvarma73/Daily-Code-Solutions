from typing import List
from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        # Use a stack to process elements and merge non-coprime adjacent pairs
        stack = []
      
        for num in nums:
            # Add current number to stack
            stack.append(num)
          
            # Keep merging the last two elements if they are not coprime
            while len(stack) > 1:
                # Get the last two elements
                second_last, last = stack[-2:]
              
                # Calculate the greatest common divisor
                common_divisor = gcd(second_last, last)
              
                # If GCD is 1, they are coprime, no merge needed
                if common_divisor == 1:
                    break
              
                # Remove the last element
                stack.pop()
              
                # Replace the second-to-last element with LCM of the pair
                # LCM = (a * b) / GCD(a, b)
                stack[-1] = second_last * last // common_divisor
      
        return stack