class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        n = len(events)
        
        # Binary search to find the latest event that doesn't overlap with current event
        def findLastNonOverlapping(i):
            left, right = 0, i - 1
            result = -1
            
            while left <= right:
                mid = (left + right) // 2
                # Check if events[mid] doesn't overlap with events[i]
                # Non-overlapping means events[mid][1] < events[i][0]
                if events[mid][1] < events[i][0]:
                    result = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            return result
        
        # dp[i][j] = maximum value using events[0..i-1] with at most j events
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, end, value = events[i - 1]
            
            for j in range(1, k + 1):
                # Option 1: Don't take current event
                dp[i][j] = dp[i - 1][j]
                
                # Option 2: Take current event
                # Find the latest non-overlapping event
                lastNonOverlapping = findLastNonOverlapping(i - 1)
                
                if lastNonOverlapping == -1:
                    # No previous non-overlapping event
                    dp[i][j] = max(dp[i][j], value)
                else:
                    # Add value to the best solution using lastNonOverlapping events
                    dp[i][j] = max(dp[i][j], dp[lastNonOverlapping + 1][j - 1] + value)
        
        return dp[n][k]