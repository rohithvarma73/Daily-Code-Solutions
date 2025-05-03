class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # To keep track of opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}  # Matching pairs

        for char in s:
            if char in bracket_map.values():
                stack.append(char)  # Push opening bracket
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False  # Mismatch or empty stack
                stack.pop()  # Correct match, pop it
            else:
                return False  # Invalid character

        return not stack  # Valid if no unmatched brackets left
