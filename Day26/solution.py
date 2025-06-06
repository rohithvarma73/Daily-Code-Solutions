class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Step 1: Preprocess - find the minimum character from i to end
        n = len(s)
        min_from_i = [''] * n
        min_from_i[-1] = s[-1]
        
        for i in range(n - 2, -1, -1):
            min_from_i[i] = min(s[i], min_from_i[i + 1])
        
        # Step 2: Simulate the robot operations
        stack = []
        result = []
        i = 0
        
        while i < n:
            # Push s[i] to stack
            stack.append(s[i])
            # While the top of the stack is <= the min char in remaining string, pop it
            while stack and (i == n - 1 or stack[-1] <= min_from_i[i + 1]):
                result.append(stack.pop())
            i += 1
        
        # Pop remaining chars
        while stack:
            result.append(stack.pop())

        return ''.join(result)
