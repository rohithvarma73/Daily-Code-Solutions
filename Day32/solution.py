class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        
        def is_possible(mid):
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count >= p:
                    return True
            return count >= p
        
        while left < right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left