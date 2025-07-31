class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Initialize a set to store unique bitwise OR results
        unique_or_results = set()
        # 'prev' will hold the cumulative OR result of the current iteration
        prev = 0
        # Iterate over the input array with both value and index
        for index, value in enumerate(arr):
            # Update 'prev' by taking the OR with the current value
            prev |= value
            # 'current' will hold the cumulative OR result starting from 'index' going back to the start
            current = 0
            # Iterate backwards from the current index to the start of the array
            for j in range(index, -1, -1):
                # Update 'current' by taking the OR with the value at j
                current |= arr[j]
                # Add 'current' to the set of unique OR results
                unique_or_results.add(current)
                # If 'current' equals 'prev', no new unique values can be found by continuing; break
                if current == prev:
                    break
        # Return the number of unique bitwise OR results found
        return len(unique_or_results)