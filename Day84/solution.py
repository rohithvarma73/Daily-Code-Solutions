class Solution:
    def numberOfWays(self, total_sum: int, exponent: int) -> int:
        # Modulo constant to prevent overflow issues for large numbers
        MOD = 10 ** 9 + 7
      
        # Initializing a dynamic programming table where
        # dp[i][j] represents the number of ways to write j as a sum
        # of i-th powers of first i natural numbers.
        dp = [[0] * (total_sum + 1) for _ in range(total_sum + 1)]
      
        # There is one way to form the sum 0 using 0 numbers: use no numbers at all.
        dp[0][0] = 1
      
        # Iterate over all numbers from 1 to total_sum
        for i in range(1, total_sum + 1):
            # Calculate the i-th power of the number
            power = pow(i, exponent)
            # Iterate over all possible sums from 0 to total_sum
            for j in range(total_sum + 1):
                # The number of ways to form the sum j without using the i-th number
                dp[i][j] = dp[i - 1][j]
                # If the power is less than or equal to the sum j, then
                # add the number of ways to form the previous sum j-power
                if power <= j:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - power]) % MOD
      
        # Return the number of ways to write total_sum as a sum of
        # powers of the first total_sum natural numbers.
        return dp[total_sum][total_sum]