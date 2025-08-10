class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Function to convert an integer to a count array of its digits
        def count_digits(num):
            count = [0] * 10  # Initialize count array for digits from 0 to 9
            while num:
                num, digit = divmod(num, 10)  # Split the number into its last digit and the rest
                count[digit] += 1  # Increment the corresponding digit count
            return count

        # Convert the input number to its digits count array
        input_digit_count = count_digits(n)

        # Start with the smallest power of 2 (2^0 = 1)
        power_of_two = 1
      
        # Loop through powers of 2 within the 32-bit integer range
        while power_of_two <= 10**9:
            # Compare the digit count array of the current power of 2 with the input number
            if count_digits(power_of_two) == input_digit_count:
                return True  # Found a power of 2 that can be reordered to the input number
            power_of_two <<= 1  # Go to the next power of 2 by left shifting bits
      
        # If no power of 2 matches after going through all 32-bit powers of 2
        return False