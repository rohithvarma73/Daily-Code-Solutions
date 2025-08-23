import math

class Solution:
  def minimumSum(self, grid: list[list[int]]) -> int:
    m = len(grid)   # number of rows
    n = len(grid[0])  # number of columns
    ans = m * n     # initialize answer with max possible area

    """
    First strategy:
    - Fix a horizontal line at row `i`.
    - Rectangle 1 = all 1's in [0..i][0..n-1] (top part)
    - Then divide the bottom part (i+1..m-1) into two vertical rectangles:
      [0..j], [j+1..n-1].
    """
    for i in range(m):
      top = self._minimumArea(grid, 0, i, 0, n - 1)
      for j in range(n):
        ans = min(ans, top +
                  self._minimumArea(grid, i + 1, m - 1, 0, j) +
                  self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1))

    """
    Second strategy:
    - Fix a horizontal line at row `i`.
    - Rectangle 1 = all 1's in [i..m-1][0..n-1] (bottom part)
    - Then divide the top part (0..i-1) into two vertical rectangles:
      [0..j], [j+1..n-1].
    """
    for i in range(m):
      bottom = self._minimumArea(grid, i, m - 1, 0, n - 1)
      for j in range(n):
        ans = min(ans, bottom +
                  self._minimumArea(grid, 0, i - 1, 0, j) +
                  self._minimumArea(grid, 0, i - 1, j + 1, n - 1))

    """
    Third strategy:
    - Fix a vertical line at column `j`.
    - Rectangle 1 = all 1's in [0..m-1][0..j] (left part)
    - Then divide the right part into two horizontal rectangles:
      [0..i], [i+1..m-1].
    """
    for j in range(n):
      left = self._minimumArea(grid, 0, m - 1, 0, j)
      for i in range(m):
        ans = min(ans, left +
                  self._minimumArea(grid, 0, i, j + 1, n - 1) +
                  self._minimumArea(grid, i + 1, m - 1, j + 1, n - 1))

    """
    Fourth strategy:
    - Fix a vertical line at column `j`.
    - Rectangle 1 = all 1's in [0..m-1][j..n-1] (right part)
    - Then divide the left part into two horizontal rectangles:
      [0..i], [i+1..m-1].
    """
    for j in range(n):
      right = self._minimumArea(grid, 0, m - 1, j, n - 1)
      for i in range(m):
        ans = min(ans, right +
                  self._minimumArea(grid, 0, i, 0, j - 1) +
                  self._minimumArea(grid, i + 1, m - 1, 0, j - 1))

    """
    Fifth strategy:
    - Split grid into **3 horizontal bands** using rows i1 and i2.
    """
    for i1 in range(m):
      for i2 in range(i1 + 1, m):
        ans = min(ans, self._minimumArea(grid, 0, i1, 0, n - 1) +
                  self._minimumArea(grid, i1 + 1, i2, 0, n - 1) +
                  self._minimumArea(grid, i2 + 1, m - 1, 0, n - 1))

    """
    Sixth strategy:
    - Split grid into **3 vertical bands** using columns j1 and j2.
    """
    for j1 in range(n):
      for j2 in range(j1 + 1, n):
        ans = min(ans, self._minimumArea(grid, 0, m - 1, 0, j1) +
                  self._minimumArea(grid, 0, m - 1, j1 + 1, j2) +
                  self._minimumArea(grid, 0, m - 1, j2 + 1, n - 1))

    return ans

  def _minimumArea(
      self,
      grid: list[list[int]],
      si: int,  # start row
      ei: int,  # end row
      sj: int,  # start col
      ej: int,  # end col
  ) -> int:
    """
    Helper function:
    Finds the bounding box of all 1's inside the given subgrid
    defined by rows [si..ei] and cols [sj..ej].
    Returns the area of this bounding rectangle.
    If no 1 is found, returns 0.
    """
    x1 = math.inf
    y1 = math.inf
    x2 = 0
    y2 = 0
    for i in range(si, ei + 1):
      for j in range(sj, ej + 1):
        if grid[i][j] == 1:
          x1 = min(x1, i)
          y1 = min(y1, j)
          x2 = max(x2, i)
          y2 = max(y2, j)
    return 0 if x1 == math.inf else (x2 - x1 + 1) * (y2 - y1 + 1)
