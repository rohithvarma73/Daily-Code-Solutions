from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # We need to calculate the total number of characters generated for each initial character after t transformations.
        def get_growth_matrix(nums):
            # This is the transition matrix: growth[i] represents how many new characters
            # a character `i` (from 'a' to 'z') will create in one transformation.
            growth = [[0] * 26 for _ in range(26)]
            for i in range(26):
                steps = nums[i]
                for j in range(steps):
                    growth[i][(i + j + 1) % 26] += 1
            return growth
        
        def mat_mult(A, B):
            # Matrix multiplication (modular)
            size = len(A)
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    C[i][j] = sum(A[i][k] * B[k][j] for k in range(size)) % MOD
            return C
        
        def mat_pow(A, exp):
            # Matrix exponentiation
            size = len(A)
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]  # Identity matrix
            base = A
            while exp > 0:
                if exp % 2 == 1:
                    result = mat_mult(result, base)
                base = mat_mult(base, base)
                exp //= 2
            return result
        
        # Build the growth matrix based on nums
        growth = get_growth_matrix(nums)
        
        # Exponentiate the growth matrix to t steps
        growth_t = mat_pow(growth, t)
        
        # Initial frequencies of characters in s
        result = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            # Sum the growth of the starting character after t steps
            result = (result + sum(growth_t[idx]) % MOD) % MOD
        
        return result

