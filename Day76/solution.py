class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Initialize variables for the answer, starting index of the window, and the sum of fruits within the window
        max_fruits = window_start = total_fruits = 0
      
        # Iterate over the fruits list with index 'j' and unpack positions and fruits as 'position_j' and 'fruits_at_j'
        for window_end, (position_j, fruits_at_j) in enumerate(fruits):
            # Add the fruits at position 'j' to the running total within the window
            total_fruits += fruits_at_j
          
            # Shrink the window from the left as long as the condition is met
            while (
                window_start <= window_end
                and position_j
                - fruits[window_start][0]  # Distance between the current end of the window and its start
                + min(abs(startPos - fruits[window_start][0]), abs(startPos - position_j))  # Minimum distance to startPos from either end of the window
                > k  # Check if the total distance is within 'k'
            ):
                # If the window exceeds 'k' distance, subtract the fruits at 'window_start' and move window start to the right
                total_fruits -= fruits[window_start][1]
                window_start += 1
          
            # Update the 'max_fruits' if the current window's total fruits is greater than the previously recorded maximum
            max_fruits = max(max_fruits, total_fruits)
      
        # Return the maximum number of fruits that can be collected within 'k' units of movement
        return max_fruits