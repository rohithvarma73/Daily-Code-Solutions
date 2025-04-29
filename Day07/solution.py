class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge case: Negative numbers are not palindromes.
        # Also, any number ending with 0 (but not 0 itself) cannot be a palindrome.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0  # This will store half of the number in reverse

        # Build the reversed second half of the number
        while x > reversed_half:
            # Add the last digit of x to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10

        # For even length numbers, x should equal reversed_half (e.g., 1221)
        # For odd length numbers, we ignore the middle digit using reversed_half // 10 (e.g., 12321)
        return x == reversed_half or x == reversed_half // 10
