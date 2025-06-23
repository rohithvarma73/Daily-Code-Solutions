class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # Helper function to check if a string is a palindrome
        def is_palindrome(s):
            return s == s[::-1]  # returns True if the string is same when reversed
        
        # Converts a number to its representation in base 'k' and returns it as a string
        def number_to_base(num, base):
            if num == 0:
                return "0"
            digits = []
            while num > 0:
                digits.append(str(num % base))  # get the remainder (digit in base-k)
                num = num // base  # reduce the number by dividing by base
            return ''.join(reversed(digits))  # reverse the list to get the correct order

        # Generator function to yield palindromic numbers in base-10 in increasing order
        def generate_palindromes():
            length = 1  # start generating palindromes of length 1
            while True:
                if length == 1:
                    # Single digit palindromes: 1 to 9
                    for num in range(1, 10):
                        yield num
                else:
                    half_length = length // 2
                    start = 10 ** (half_length - 1)  # e.g., for half_length=2 => 10
                    end = 10 ** half_length         # e.g., for half_length=2 => 100
                    
                    if length % 2 == 0:
                        # Even length palindromes
                        for left in range(start, end):
                            left_str = str(left)
                            palindrome_str = left_str + left_str[::-1]  # mirror the left half
                            yield int(palindrome_str)
                    else:
                        # Odd length palindromes
                        for left in range(start, end):
                            left_str = str(left)
                            for mid in range(10):  # middle digit can be 0–9
                                palindrome_str = left_str + str(mid) + left_str[::-1]
                                yield int(palindrome_str)
                length += 1  # increase length for next round (e.g., 2-digit, 3-digit palindromes, etc.)

        res = []  # to store the first 'n' k-mirror numbers
        gen = generate_palindromes()  # initialize the palindrome generator
        
        # Keep collecting k-mirror numbers until we have 'n
