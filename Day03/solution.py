class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # Create a set to store unique elements
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add new number to the set
        return False  # No duplicates found
