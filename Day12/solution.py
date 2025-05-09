class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Initialize a pointer to track the position for non-val elements
        
        for i in range(len(nums)):  # Iterate over each element in the nums list
            if nums[i] != val:  # If the current element is not equal to the value to remove
                nums[k] = nums[i]  # Copy it to the position at index k
                k += 1  # Move the pointer forward for the next non-val element

        return k  # Return the count of elements that are not equal to val
