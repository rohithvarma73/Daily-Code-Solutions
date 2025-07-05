class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Count frequency of each number
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # Find the largest lucky number
        lucky = -1
        for num, count in freq.items():
            if num == count:  # Lucky number: frequency equals value
                lucky = max(lucky, num)
        
        return lucky