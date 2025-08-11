from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Extract the powers of 2 from n in ascending order
        powers_of_two = []
        while n:
            x = n & -n
            powers_of_two.append(x)
            n -= x

        mod = 10**9 + 7
        
        # Precompute prefix products
        prefix_product = [1] * (len(powers_of_two) + 1)
        for i in range(len(powers_of_two)):
            prefix_product[i+1] = (prefix_product[i] * powers_of_two[i]) % mod

        # Answer each query in O(1) using modular inverse
        results = []
        for l, r in queries:
            product = (prefix_product[r+1] * pow(prefix_product[l], mod-2, mod)) % mod
            results.append(product)

        return results
