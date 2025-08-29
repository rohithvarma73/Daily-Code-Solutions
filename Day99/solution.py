class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Calculate half of the garden, rounded up
        half_up_n = (n + 1) // 2
        half_up_m = (m + 1) // 2
      
        # Calculate half of the garden, rounded down
        half_down_n = n // 2
        half_down_m = m // 2
      
        # Calculate the result based on the game's logic, which seems to involve
        # multiplying the halves of the two dimensions, with one dimension always rounded up
        # and the other rounded down, then adding both results
        result = half_up_n * half_down_m + half_down_n * half_up_m
      
        return result