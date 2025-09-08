class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Find two positive integers without digit '0' that sum to n.
      
        Args:
            n: The target sum (2 <= n <= 10^4)
          
        Returns:
            A list containing two integers [a, b] where a + b = n
            and neither a nor b contains the digit '0'
        """
        # Iterate through all possible values for the first integer
        for first_num in range(1, n):
            # Calculate the second integer to make the sum equal to n
            second_num = n - first_num
          
            # Convert both numbers to strings and concatenate them
            combined_str = str(first_num) + str(second_num)
          
            # Check if the digit '0' appears in either number
            if '0' not in combined_str:
                # Return the valid pair as soon as we find one
                return [first_num, second_num]
