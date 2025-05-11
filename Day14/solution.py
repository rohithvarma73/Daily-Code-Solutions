class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special overflow case: when dividing INT_MIN by -1, result is beyond INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result:
        # Result is negative if dividend and divisor have opposite signs
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values to simplify the division logic
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0  # This will hold the final result

        # Subtract multiples of divisor from dividend using bit manipulation
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            # Double the temp divisor until it's less than or equal to the dividend
            while dividend >= (temp << 1):
                temp <<= 1          # Double the value of temp (equivalent to temp * 2)
                multiple <<= 1      # Keep track of how many times we doubled

            dividend -= temp        # Subtract the largest found multiple from dividend
            quotient += multiple    # Add how many times we subtracted to the quotient

        # Apply the sign to the quotient and return
        return -quotient if negative else quotient
