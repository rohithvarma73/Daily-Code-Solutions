class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Step 1: Find all indices where the element equals the key
        key_indices = [i for i, num in enumerate(nums) if num == key]

        # Step 2: Use a set to avoid duplicates
        result = set()
        
        # Step 3: For each key index, add all indices i such that |i - key_index| <= k
        for j in key_indices:
            # Calculate the range of indices within distance k from j
            start = max(0, j - k)
            end = min(len(nums) - 1, j + k)
            
            # Add all indices from start to end into the result set
            for i in range(start, end + 1):
                result.add(i)
        
        # Step 4: Convert the set to a sorted list before returning
        return sorted(result)
