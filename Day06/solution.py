class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the string is empty or has only one character, it is already a palindrome
        if not s or len(s) == 1:
            return s

        start, end = 0, 0  # Initialize pointers to track the start and end of the longest palindrome found

        for i in range(len(s)):
            # Check for the longest odd-length palindrome centered at i
            len1 = self.expandAroundCenter(s, i, i)
            # Check for the longest even-length palindrome centered between i and i+1
            len2 = self.expandAroundCenter(s, i, i + 1)
            # Take the maximum length from the two centers
            max_len = max(len1, len2)

            # If a longer palindrome is found, update the start and end pointers
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # Return the longest palindromic substring
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # Expand around the center as long as the characters match and boundaries are within the string
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the length of the palindrome found
        return right - left - 1
