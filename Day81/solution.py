class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Check if n is less than or equal to 0; negative numbers and zero are not powers of two
        if n <= 0:
            return False

        # Use bitwise AND to determine if n has only one bit set.
        # If n is a power of two, n & (n - 1) will be 0.
        return (n & (n - 1)) == 0
