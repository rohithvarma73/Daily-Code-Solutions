class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Iterate over the digits in descending order, starting from 9 to 0.
        for digit in range(9, -1, -1):
            # Create a string of three consecutive identical digits.
            triple_digit_str = str(digit) * 3
          
            # Check if this string of three identical digits is in the input 'num'.
            if triple_digit_str in num:
                # If found, return this largest 'good' integer as the result.
                return triple_digit_str

        # If no such triple is found in the number, return an empty string.
        return ""