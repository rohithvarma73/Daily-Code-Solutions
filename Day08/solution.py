class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for the binary search window
        left, right = 0, len(nums) - 1

        # Continue searching while the window is valid
        while left <= right:
            mid = (left + right) // 2  # Find the middle index

            if nums[mid] == target:
                return mid  # Target found, return index
            elif nums[mid] < target:
                left = mid + 1  # Search right half
            else:
                right = mid - 1  # Search left half

        return -1  # Target not found
