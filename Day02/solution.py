class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Initialize two pointers: one at the beginning (left) and one at the end (right)
        left, right = 0, len(s) - 1
        
        # Continue swapping characters until the pointers meet in the middle
        while left < right:
            # Swap the characters at the left and right pointers
            s[left], s[right] = s[right], s[left]
            
            # Move the left pointer forward
            left += 1
            
            # Move the right pointer backward
            right -= 1

        # The input list s is modified in-place, as required by the problem
