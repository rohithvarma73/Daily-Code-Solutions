class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Initialize an empty list to store the result
        result = []
        
        # Define a helper function to perform DFS
        def dfs(current):
            # If the current number exceeds n, return
            if current > n:
                return
            # Add the current number to the result list
            result.append(current)
            # For each digit from 0 to 9, recursively call dfs with current * 10 + digit
            for i in range(10):
                dfs(current * 10 + i)
        
        # Start DFS from numbers 1 to 9
        for i in range(1, 10):
            dfs(i)
        
        # Return the result list
        return result