import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_leq(mid):
            count = 0
            for num in nums1:
                if num == 0:
                    if mid >= 0:
                        count += len(nums2)
                elif num > 0:
                    # Find nums2[j] <= mid / num
                    max_val = mid // num
                    if mid % num >= 0:
                        pass
                    else:
                        max_val -= 1
                    idx = bisect.bisect_right(nums2, max_val)
                    count += idx
                else:
                    # num is negative: nums2[j] >= mid / num
                    # since num is negative, dividing reverses the inequality
                    min_val = mid // num
                    if mid % num != 0:
                        min_val += 1
                    idx = bisect.bisect_left(nums2, min_val)
                    count += len(nums2) - idx
            return count
        
        left = -10**10 - 1
        right = 10**10 + 1
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if count_leq(mid) >= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer