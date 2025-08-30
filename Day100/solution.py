class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize tracking arrays for rows, columns, and 3x3 sub-boxes
        # Each inner array tracks whether digits 1-9 have been seen (index 0-8)
        rows_seen = [[False] * 9 for _ in range(9)]
        cols_seen = [[False] * 9 for _ in range(9)]
        boxes_seen = [[False] * 9 for _ in range(9)]
      
        # Iterate through each cell in the 9x9 board
        for row_idx in range(9):
            for col_idx in range(9):
                cell_value = board[row_idx][col_idx]
              
                # Skip empty cells
                if cell_value == '.':
                    continue
              
                # Convert digit character to 0-based index (1-9 becomes 0-8)
                digit_idx = int(cell_value) - 1
              
                # Calculate which 3x3 sub-box this cell belongs to
                # Formula maps (row, col) to box index 0-8
                box_idx = (row_idx // 3) * 3 + (col_idx // 3)
              
                # Check if this digit already exists in current row, column, or box
                if (rows_seen[row_idx][digit_idx] or 
                    cols_seen[col_idx][digit_idx] or 
                    boxes_seen[box_idx][digit_idx]):
                    return False
              
                # Mark this digit as seen in the current row, column, and box
                rows_seen[row_idx][digit_idx] = True
                cols_seen[col_idx][digit_idx] = True
                boxes_seen[box_idx][digit_idx] = True
      
        # All cells are valid if we reach here
        return True