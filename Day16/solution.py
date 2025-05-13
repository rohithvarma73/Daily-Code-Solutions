class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        if n == 1:
            return "1"

        # Get the previous term in the sequence recursively
        prev = self.countAndSay(n - 1)

        # Initialize result string and count
        result = ""
        count = 1

        # Iterate over the previous term to build the current term
        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                # Append count and previous character
                result += str(count) + prev[i - 1]
                count = 1  # Reset count

        # Append the last group
        result += str(count) + prev[-1]

        return result
