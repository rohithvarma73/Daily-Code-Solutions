class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings and compare them
        # If they are equal, then t is an anagram of s
        return sorted(s) == sorted(t)
