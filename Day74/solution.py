class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the first row of Pascal's Triangle
        pascal_triangle = [[1]]
      
        # Generate each row of Pascal's Triangle
        for i in range(1, numRows):
            # The first element of each row is always 1
            new_row = [1]
          
            # Calculate the intermediate elements of the row
            # by adding the pairs of adjacent elements from the previous row
            for j in range(1, i):
                sum_of_elements = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
                new_row.append(sum_of_elements)
          
            # The last element of each row is also always 1
            new_row.append(1)
          
            # Append the newly generated row to Pascal's Triangle
            pascal_triangle.append(new_row)
      
        # Return the completed Pascal's Triangle
        return pascal_triangle
