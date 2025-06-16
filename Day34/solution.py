class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = nums[0]
        max_diff = -1
        
        for num in nums[1:]:
            if num > min_num:
                max_diff = max(max_diff, num - min_num)
            min_num = min(min_num, num)
        
        return max_diff