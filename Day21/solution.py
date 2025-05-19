from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        
        # Check if the sides form a valid triangle
        if a + b <= c:
            return "none"
        
        # Check for equilateral
        if a == b == c:
            return "equilateral"
        
        # Check for isosceles
        if a == b or b == c or a == c:
            return "isosceles"
        
        # If none of the above, it's scalene
        return "scalene"
