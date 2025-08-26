from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        # Initialize the maximum diagonal length and area seen so far
        max_diagonal_length = 0
        max_area = 0
      
        # Loop through each dimension pair in the dimensions list
        for length, width in dimensions:
            # Calculate the diagonal length's square based on Pythagorean theorem
            diagonal_length_sq = length**2 + width**2
          
            # If a new maximum diagonal length is found
            if diagonal_length_sq > max_diagonal_length:
                # Update maximum diagonal length and area
                max_diagonal_length = diagonal_length_sq
                max_area = length * width
            # If current diagonal is equal to the maximum found but the area is larger
            elif diagonal_length_sq == max_diagonal_length:
                # Update the area to the larger one
                max_area = max(max_area, length * width)
              
        # Return the maximum area corresponding to the largest diagonal length
        return max_area