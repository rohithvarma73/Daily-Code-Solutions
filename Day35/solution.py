MOD = 10**9 + 7

class Solution(object):
    def countGoodArrays(self, n, m, k):
        """
        :type n: int
        :type m: int
        :type k: int
        :rtype: int
        """
        if k >= n:
            return 0
        
        # We need to compute the sum over t of C(n-1, t) * (m) * (m-1)^{n-1-t} where t >=k
        # Wait, no. The problem is to have exactly k adjacent pairs equal.
        # So the array is divided into (n - k) segments where the first element is chosen freely,
        # and each subsequent segment's first element must differ from the previous segment's last.
        # The number of such arrays is m * (m-1)^{n -k -1} * C(n-1, k)
        # Wait, let's think:
        # The array has exactly k adjacent pairs equal. So the array has (n -k) distinct blocks where
        # each block is a sequence of the same number. For example, [1,1,2,2,1] has 3 blocks (1-1, 2-2, 1) and 2 adjacent pairs.
        # The number of such arrays is m * (m-1)^{n -k -1} * C(n-1, k)
        # Because:
        # - The first block can be any of m numbers.
        # - Each subsequent block must choose a different number from the previous block, hence (m-1) choices per block.
        # - The number of ways to split the array into (n -k) blocks is C(n-1, n-k-1) = C(n-1, k), because you need to place (n-k-1) boundaries between the blocks in (n-1) possible positions.
        
        if k > n -1:
            return 0
        
        # Compute combination(n-1, k) * m * (m-1)^{n -k -1} mod MOD
        # But need to handle cases where n -k -1 could be negative (i.e., when n ==k)
        if n ==k:
            return m % MOD
        
        # Precompute factorial, inverse factorial up to n-1 modulo MOD for combination calculation
        max_n = n
        fact = [1] * (max_n +1)
        inv_fact = [1] * (max_n +1)
        
        for i in range(1, max_n+1):
            fact[i] = fact[i-1] * i % MOD
        
        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in range(max_n -1, -1, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD
        
        def comb(a, b):
            if a <0 or b <0 or a <b:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a -b] % MOD
        
        c = comb(n-1, k)
        power = pow(m-1, n -k -1, MOD)
        res = c * m % MOD
        res = res * power % MOD
        return res