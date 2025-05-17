from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the array in-place so that all 0s come first, followed by all 1s, and then all 2s.
        This uses the Dutch National Flag Algorithm.
        Do not return anything; the function modifies nums in-place.
        """
        
        # Initialize pointers:
        # low: boundary for placing 0s
        # mid: current index being evaluated
        # high: boundary for placing 2s
        low, mid, high = 0, 0, len(nums) - 1

        # Loop until mid pointer crosses high
        while mid <= high:
            if nums[mid] == 0:
                # If current number is 0, swap it with the number at low pointer
                # Then move both low and mid one step forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # If the number is 1, it's in the correct place; just move mid forward
                mid += 1
            else:
                # If current number is 2, swap it with the number at high pointer
                # Then move high one step backward (mid is not incremented to re-evaluate swapped element)
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
