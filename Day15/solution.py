class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0 as per problem convention
        if not needle:
            return 0

        # Get lengths of both strings
        len_h, len_n = len(haystack), len(needle)

        # Only iterate up to the point where needle can still fit
        for i in range(len_h - len_n + 1):
            # Check if the substring from haystack matches needle
            if haystack[i:i+len_n] == needle:
                return i  # Found, return the index

        return -1  # Not found
