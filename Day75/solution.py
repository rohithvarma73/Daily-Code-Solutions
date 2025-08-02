from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Create a counter to track the frequency of each fruit type
        fruit_counter = Counter()
      
        # Iterate over both baskets simultaneously
        for fruit_type_a, fruit_type_b in zip(basket1, basket2):
            # Increment the count for fruit type from basket1
            fruit_counter[fruit_type_a] += 1
            # Decrement the count for fruit type from basket2
            fruit_counter[fruit_type_b] -= 1
      
        # Get the minimum fruit type value from our counter
        min_fruit_type = min(fruit_counter)
      
        # Prepare a list to count how many exchanges are needed
        exchange_list = []
      
        # Check if exchange is possible given the counts
        for fruit_type, count in fruit_counter.items():
            if count % 2:
                # If count is odd, return -1 (impossible to exchange)
                return -1
            # Add the fruit types for exchange to the list
            exchange_list.extend([fruit_type] * (abs(count) // 2))
      
        # Sort the list to facilitate minimum cost calculation
        exchange_list.sort()
      
        # Find the middle point of our sorted list
        mid_point = len(exchange_list) // 2
      
        # Calculate and return the cost of exchanges
        # By taking minimum exchange cost between the fruit type and double the minimum fruit type
        return sum(min(fruit_type, min_fruit_type * 2) for fruit_type in exchange_list[:mid_point])