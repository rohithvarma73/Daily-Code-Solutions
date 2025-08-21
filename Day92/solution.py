class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # Get the number of rows (m) and columns (n) of the matrix.
        num_rows, num_cols = len(mat), len(mat[0])
      
        # Initialize a matrix to store the number of continuous ones in each row.
        continuous_ones = [[0] * num_cols for _ in range(num_rows)]
      
        # Populate the continuous_ones matrix.
        for row in range(num_rows):
            for col in range(num_cols):
                # If we encounter a '1', count the continuous ones. If in first column,
                # it can only be 1 or 0. Otherwise, add 1 to the left cell's count.
                if mat[row][col]:
                    continuous_ones[row][col] = 1 if col == 0 else 1 + continuous_ones[row][col - 1]
      
        # Initialize a count for total number of submatrices.
        total_submatrices = 0
      
        # Calculate the number of submatrices for each cell as the bottom-right corner.
        for row in range(num_rows):
            for col in range(num_cols):
                # This will keep track of the smallest number of continuous ones in the current column,
                # up to the current row 'row'.
                min_continuous_ones = float('inf')
              
                # Travel up the rows from the current cell.
                for k in range(row, -1, -1):
                    # Find the smallest number of continuous ones in this column up to the k-th row.
                    min_continuous_ones = min(min_continuous_ones, continuous_ones[k][col])
                  
                    # Add the smallest number to the total count.
                    total_submatrices += min_continuous_ones
      
        # Return the total number of submatrices.
        return total_submatrices