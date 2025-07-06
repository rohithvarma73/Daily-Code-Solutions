class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        
        # Create frequency map for nums2
        self.freq2 = {}
        for num in nums2:
            self.freq2[num] = self.freq2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        # Remove old value from frequency map
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        
        # Update nums2 and add new value to frequency map
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq2[new_val] = self.freq2.get(new_val, 0) + 1

    def count(self, tot: int) -> int:
        count = 0
        # For each element in nums1, find how many elements in nums2 
        # can form the target sum
        for num1 in self.nums1:
            needed = tot - num1
            if needed in self.freq2:
                count += self.freq2[needed]
        return count