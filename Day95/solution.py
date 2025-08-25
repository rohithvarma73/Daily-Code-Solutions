from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # Determine the number of rows and columns in the matrix.
        num_rows, num_cols = len(matrix), len(matrix[0])
      
        # This is the list which will hold the elements in diagonal order.
        diagonal_order = []
      
        # There will be (num_rows + num_cols - 1) diagonals to cover in the matrix.
        for k in range(num_rows + num_cols - 1):
          
            # Temp list to store the elements of the current diagonal.
            temp = []
          
            # Calculate the starting row index. It is 0 for the first 'num_cols' diagonals,
            # otherwise we start at an index which goes down from 'num_rows - 1'.
            row = 0 if k < num_cols else k - num_cols + 1
          
            # Calculate the starting column index. It is 'k' for the first 'num_cols' diagonals,
            # otherwise we start at 'num_cols - 1' and go down.
            col = k if k < num_cols else num_cols - 1
          
            # Fetch the elements along the current diagonal.
            # Continue while 'row' is within the matrix row range and 'col' is non-negative.
            while row < num_rows and col >= 0:
                temp.append(matrix[row][col])
                row += 1  # Move down to the next row.
                col -= 1  # Move left to the next column.
          
            # Reverse every other diagonal's elements before appending it to the result list
            # to get the right order.
            if k % 2 == 0:
                temp = temp[::-1]
          
            # Extend the main result list with the elements of the current diagonal.
            diagonal_order.extend(temp)
      
        # Return the final result list.
        return diagonal_order