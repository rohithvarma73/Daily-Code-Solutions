class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        def get_count(prefix, n):
            """Count how many numbers starting with `prefix` are ≤ n."""
            curr = prefix
            next = prefix + 1
            count = 0
            while curr <= n:
                count += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return count

        curr = 1
        k -= 1  # Because we're already at the first number "1"

        while k > 0:
            count = get_count(curr, n)
            if k >= count:
                # Move to next prefix (e.g., from 1 to 2)
                k -= count
                curr += 1
            else:
                # Go deeper in the tree (e.g., from 1 to 10)
                curr *= 10
                k -= 1

        return curr
