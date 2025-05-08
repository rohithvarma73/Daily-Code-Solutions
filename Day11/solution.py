class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list is empty or has only one element, return its length
        if not nums:
            return 0

        # Initialize a pointer to keep track of the index of unique elements
        k = 1  # Since the first element is always unique

        # Start from the second element and iterate through the list
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous unique one
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # Update the position at k with the new unique value
                k += 1  # Move the pointer forward

        return k  # k is the count of unique elements
