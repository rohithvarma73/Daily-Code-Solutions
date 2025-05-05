class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # Define 32-bit signed integer range

        sign = -1 if x < 0 else 1  # Check the sign of x
        x_abs = abs(x)  # Work with positive value of x

        reversed_num = 0
        while x_abs != 0:
            digit = x_abs % 10  # Get the last digit
            x_abs //= 10  # Remove the last digit

            # Check for overflow before actually adding the digit
            if reversed_num > (INT_MAX - digit) // 10:
                return 0  # Overflow condition

            reversed_num = reversed_num * 10 + digit  # Append the digit

        return sign * reversed_num  # Apply the sign back
