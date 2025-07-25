class Solution:
  def maxSum(self, nums: list[int]) -> int:
    # Find the maximum number in the array
    mx = max(nums)

    # If the maximum number is <= 0, return it directly
    if mx <= 0:
      return mx

    # Convert list to set to get only unique elements and sum up the non-negative ones
    return sum(max(0, num) for num in set(nums))
