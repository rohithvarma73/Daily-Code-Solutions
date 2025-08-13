class Solution:
    def isPowerOfThree(self, number: int) -> bool:
        # The largest power of 3 value that fits in a 32-bit signed integer is 3^19, which is 1162261467.
        # If 'number' is a power of 3, it must divide 1162261467 without any remainder.
        # 'number' must be positive since 0 and negative numbers cannot be powers of 3.
      
        # We check that the number is positive and that the modulo operation of 1162261467 by 'number' is zero.
        # If the result is zero, 'number' is a divisor of 1162261467, implying it is a power of 3.
        return number > 0 and 1162261467 % number == 0