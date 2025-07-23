class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, val):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += val
                else:
                    stack.append(ch)
            return ''.join(stack), score

        res = 0
        if x >= y:
            # Remove "ab" first, then "ba"
            s, gain = remove_substring(s, 'a', 'b', x)
            res += gain
            _, gain = remove_substring(s, 'b', 'a', y)
            res += gain
        else:
            # Remove "ba" first, then "ab"
            s, gain = remove_substring(s, 'b', 'a', y)
            res += gain
            _, gain = remove_substring(s, 'a', 'b', x)
            res += gain
        return res
