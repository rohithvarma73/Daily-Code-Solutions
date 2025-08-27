from typing import List
from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])
      
        # Define what the next digit should be for each current digit
        next_digit = {1: 2, 2: 0, 0: 2}

        # Check if the given coordinates are within the grid bounds
        def within_bounds(i, j):
            return 0 <= i < m and 0 <= j < n

        # Memoized recursive function to calculate the length of the diagonal
        @cache
        def f(i, j, di, dj, turned):
            result = 1
            successor = next_digit[grid[i][j]]

            # Move in the current direction if the next cell has the expected successor digit
            if within_bounds(i + di, j + dj) and grid[i + di][j + dj] == successor:
                result = 1 + f(i + di, j + dj, di, dj, turned)

            # If not already turned, try turning and continue in the new direction, checking if allowed
            if not turned:
                new_di, new_dj = dj, -di
                if within_bounds(i + new_di, j + new_dj) and grid[i + new_di][j + new_dj] == successor:
                    result = max(result, 1 + f(i + new_di, j + new_dj, new_di, new_dj, True))

            return result

        # Define possible diagonal directions
        directions = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        result = 0

        # Iterate over each cell in the grid
        for i in range(m):
            for j in range(n):
                # Start exploring only if the cell contains a 1
                if grid[i][j] != 1:
                    continue
                # Try each diagonal direction from the current 1 cell
                for di, dj in directions:
                    result = max(result, f(i, j, di, dj, False))

        return result