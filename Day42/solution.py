class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        current_value = 0  # Decimal value of the subsequence formed by '1's
        subsequence_length = 0 # Length of the subsequence
        
        # power_of_2 represents the bit significance (1, 2, 4, 8, ...)
        # It starts at 1 for the rightmost bit (2^0)
        power_of_2 = 1 

        # Iterate through the string from right to left (least significant bit to most significant bit)
        for i in range(len(s) - 1, -1, -1):
            bit = int(s[i])

            if bit == 0:
                # '0's can almost always be included to increase length without affecting value,
                # unless they become leading zeros of a significant '1' that pushes the value over k.
                # However, when building from right-to-left, '0's are always beneficial for length.
                subsequence_length += 1
            else: # bit == 1
                # Check if adding this '1' (at its current bit significance) would exceed k.
                # Only add if current_value + power_of_2 does not exceed k.
                if current_value + power_of_2 <= k:
                    current_value += power_of_2
                    subsequence_length += 1
                # Else: If we cannot add this '1', we don't.
                # Since we are processing from right to left, any subsequent '1's to the left
                # would have even greater significance (larger power_of_2), so they wouldn't fit either.
                # We can stop considering '1's if power_of_2 becomes too large.
            
            # Prepare for the next bit position (moving left means doubling significance).
            # Avoid overflow for power_of_2 if it's already very large, as it's only relevant if current_value is small.
            # If current_value is 0 and power_of_2 already exceeds k, future power_of_2 will also exceed k.
            # No, power_of_2 must keep track of the *potential* bit position correctly.
            # Max power_of_2 needed for k=10^9 is around 2^29.
            # So as long as power_of_2 doesn't exceed 2^30 or so, it's fine.
            # It only matters when we add a '1'. If current_value is already too high, 
            # or power_of_2 itself is too high such that power_of_2 > k, then multiplication isn't useful.
            
            # Safe way to update power_of_2 for the next iteration (bit to the left)
            # Only update if current_value + next_power_of_2 could potentially be <= k
            # This handles cases where power_of_2 grows extremely large
            if i > 0 and (current_value <= k - power_of_2 or power_of_2 < k / 2): # Avoid overflow or useless large powers
                power_of_2 *= 2
            elif i > 0 and power_of_2 > k: # If power_of_2 already too big, next will be too. Only keep it up to k.
                # This ensures `power_of_2` doesn't grow to arbitrarily massive numbers, preventing potential issues
                # with `current_value + power_of_2` exceeding standard integer limits in other languages,
                # though Python handles large integers automatically. It also helps with the logic.
                pass # Don't update power_of_2 if it's already too large to fit any '1'
            
        return subsequence_length