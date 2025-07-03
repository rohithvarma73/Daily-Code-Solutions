class Solution:
    def kthCharacter(self, k: int) -> str:
        # Initialize the string with "a"
        word = "a"

        # Continue operations until the string has at least k characters
        while len(word) < k:
            # Generate the next segment by incrementing each character
            new_part = []
            for c in word:
                if c == 'z':
                    new_part.append('a')  # Wrap 'z' to 'a'
                else:
                    new_part.append(chr(ord(c) + 1))  # Increment character
            # Append the new segment to the original string
            word += ''.join(new_part)

        # Return the k-th character (1-based index)
        return word[k - 1]