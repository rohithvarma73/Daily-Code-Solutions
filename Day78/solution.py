from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)  # Number of fruits
        visited = [False] * n  # Track which baskets have been used
        unplaced_count = n  # Initialize unplaced fruit count as total fruit count

        # Iterate over each fruit
        for fruit in fruits:
            # Attempt to place the fruit in a suitable basket
            for index, basket in enumerate(baskets):
                # Check if the basket can hold the fruit and if the basket is not already used
                if basket >= fruit and not visited[index]:
                    visited[index] = True  # Mark this basket as used
                    unplaced_count -= 1  # Decrease unplaced fruit count
                    break  # Move to the next fruit once a basket is found
        return unplaced_count  # Return the number of unplaced fruits