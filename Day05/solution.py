from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        merged = sorted(nums1 + nums2)  # Combine both arrays and sort them

        n = len(merged)  # Get the total number of elements

        # If the total number of elements is odd
        if n % 2 == 1:
            return float(merged[n // 2])  # Return the middle element as the median
        else:
            # If even, return the average of the two middle elements
            mid1 = merged[(n // 2) - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0
