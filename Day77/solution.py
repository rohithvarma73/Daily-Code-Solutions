from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Initialize a counter to keep track of the count of each type of fruit
        fruit_counter = Counter()
        # Initialize a variable to keep track of the starting index of the current window
        start_index = 0
        # Iterate over the list of fruits
        for fruit in fruits:
            # Increment the count for the current fruit
            fruit_counter[fruit] += 1
            # If the counter has more than two types of fruits, we shrink the window
            if len(fruit_counter) > 2:
                # The fruit at the start index needs to be removed or decremented
                start_fruit = fruits[start_index]
                fruit_counter[start_fruit] -= 1
                # Remove the fruit from counter if its count drops to 0
                if fruit_counter[start_fruit] == 0:
                    del fruit_counter[start_fruit]
                # Move the start index forward
                start_index += 1
        # Calculate the maximum length of the subarray with at most two types of fruits
        max_length = len(fruits) - start_index
        return max_length
