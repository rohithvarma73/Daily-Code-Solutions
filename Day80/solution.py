class Solution:
  def maxCollectedFruits(self, fruits: list[list[int]]) -> int:
    n = len(fruits)  # n is the size of the square grid

    # Diagonal path from top-left to bottom-right (i.e., (0,0) to (n-1,n-1))
    def getTopLeft() -> int:
      return sum(fruits[i][i] for i in range(n))  # Sum of main diagonal elements

    # Path from top-right to bottom-right corner
    def getTopRight() -> int:
      dp = [[0] * n for _ in range(n)]  # Create DP table
      dp[0][-1] = fruits[0][-1]  # Start from the top-right corner (0, n-1)

      # Loop through each cell
      for x in range(n):
        for y in range(n):
          # Skip invalid positions; we're only interested in upper-right triangle
          if x >= y and (x, y) != (n - 1, n - 1):
            continue

          # Move down and diagonally: (1,-1), (1,0), (1,1)
          for dx, dy in [(1, -1), (1, 0), (1, 1)]:
            i = x - dx
            j = y - dy

            # Skip if out of bounds
            if i < 0 or i == n or j < 0 or j == n:
              continue

            # Constraint to stay within a triangular zone of valid cells
            if i < j < n - 1 - i:
              continue

            # Update DP value: max fruits collected so far to this cell
            dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y])

      return dp[-1][-1]  # Return max fruits collected to reach bottom-right

    # Path from bottom-left to bottom-right corner
    def getBottomLeft() -> int:
      dp = [[0] * n for _ in range(n)]  # Create DP table
      dp[-1][0] = fruits[-1][0]  # Start from bottom-left corner (n-1, 0)

      # Loop through each cell
      for y in range(n):
        for x in range(n):
          # Skip invalid positions; only care about lower-left triangle
          if x <= y and (x, y) != (n - 1, n - 1):
            continue

          # Move right and diagonally up/down: (-1,1), (0,1), (1,1)
          for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
            i = x - dx
            j = y - dy

            # Skip if out of bounds
            if i < 0 or i == n or j < 0 or j == n:
              continue

            # Constraint to stay within a triangular zone of valid cells
            if j < i < n - 1 - j:
              continue

            # Update DP value
            dp[x][y] = max(dp[x][y], dp[i][j] + fruits[x][y])

      return dp[-1][-1]  # Return max fruits collected to reach bottom-right

    # Final result:
    # Add the fruits collected from three paths:
    # - Top-left to bottom-right (diagonal)
    # - Top-right to bottom-right (via DP)
    # - Bottom-left to bottom-right (via DP)
    # Since all three paths end at (n-1, n-1), we subtract 2 times that cell’s fruit to avoid double-counting
    return getTopLeft() + getTopRight() + getBottomLeft() - 2 * fruits[-1][-1]
