class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize an array to store the powers of 2 found in the binary representation of n
        powers_of_two = []
      
        # Extract powers of 2 from n by finding the rightmost set bit continuously
        while n:
            # x is the largest power of 2 in n, given by the bitwise AND of n and its two's complement
            x = n & -n
            # Add x to the list
            powers_of_two.append(x)
            # Remove the largest power of 2 from n
            n -= x
      
        # Set modulo as per the problem statement to avoid large integer overflow
        mod = 10**9 + 7
      
        # Initialize an array to store the results of the queries
        results = []
      
        # Loop through each query, which is a pair of indices (l, r)
        for l, r in queries:
            # Start with a product result of 1 for each query
            product_result = 1
          
            # Multiply the values from powers_of_two[l] to powers_of_two[r]
            # and take the modulo to prevent overflow
            for power in powers_of_two[l : r + 1]:
                product_result = (product_result * power) % mod
          
            # Append the product result to the results list
            results.append(product_result)

        # Return the final list of results for all queries
        return results