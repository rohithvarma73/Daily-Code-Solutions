from functools import lru_cache

class Solution:
    def new21Game(self, N: int, K: int, maxPoints: int) -> float:
        # Use an LRU cache to cache results and avoid re-computation.
        @lru_cache(None)
        def dfs(current_points: int) -> float:
            # Base condition: If current points are at or beyond K, 
            # the game stops; return 1.0 if not beyond N, otherwise 0.0.
            if current_points >= K:
                return float(current_points <= N)
          
            # If we are at the last point before K, the probability of 
            # getting a final score not more than N depends on how many 
            # points would lead to a score within the [K, N] range, 
            # divided by the maximum number of points we can get at this draw.
            if current_points == K - 1:
                return min(N - K + 1, maxPoints) / maxPoints
          
            # Recursively calculate the probability of winning by either
            # drawing a card of points 1 up to maxPoints from the current score. The probability 
            # is a difference of probabilities of getting the next score, and the score that is
            # 'maxPoints' away from current + 1, because that's no longer reachable in one draw.
            # The total is divided by maxPoints to get the average probability.
            return dfs(current_points + 1) + (dfs(current_points + 1) - dfs(current_points + maxPoints + 1)) / maxPoints

        # Start DFS from 0 points to calculate the probability of winning.
        return dfs(0)