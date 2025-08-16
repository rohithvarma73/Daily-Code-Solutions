class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert the integer to a string to manipulate individual digits
        num_str = str(num)
      
        # Replace the first occurrence of '6' with '9' in the string
        # This ensures we make the maximum number by changing the leftmost '6'
        # Use only one replacement to maximize the number
        modified_num_str = num_str.replace('6', '9', 1)
      
        # Convert the modified string back to an integer and return it
        return int(modified_num_str)

# Example of usage:
# solution = Solution()
# print(solution.maximum69Number(9669)) # Output: 9969