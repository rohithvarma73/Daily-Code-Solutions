from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Get the length of the input array
        length = len(nums)

        # Initialize the result array with 1s, as the smallest non-empty subarray is the number itself.
        result = [1] * length

        # Initialize an array to store the latest positions of bits (0 to 31) seen in the binary representation of the numbers
        last_seen_at = [-1] * 32

        # Traverse the input array in reverse order
        for i in reversed(range(length)):
            max_size = 1  # Initialize current size to 1 (the size of a subarray containing only nums[i])
            # Go through each of the 32 bits to update 'last_seen_at' and calculate the subarray size
            for j in range(32):
                if (nums[i] >> j) & 1:  # Check if bit 'j' is set in nums[i]
                    last_seen_at[j] = i  # Update the position of bit 'j'
                elif last_seen_at[j] != -1:  # If bit 'j' was found at a position ahead of 'i'
                    # Update 'max_size': the size of the subarray that includes the current number and
                    # the last occurrence of every bit that is not present in the current number
                    max_size = max(max_size, last_seen_at[j] - i + 1)
            # Record the required subarray size for the current starting index 'i'
            result[i] = max_size

        # Return the array containing the sizes of the smallest subarrays
        return result