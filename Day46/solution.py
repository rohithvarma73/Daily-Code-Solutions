class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        # Initialize total_possible_strings to 1. 
        # This accounts for the scenario where Alice did NOT over-press any key,
        # meaning the 'word' itself is one of the possible original strings.
        total_possible_strings = 1
        
        # The problem constraints state 1 <= word.length, so 'word' will never be empty.
        n = len(word)
        
        # Use a pointer 'i' to traverse the string. 
        # 'i' will mark the beginning of each new block of consecutive identical characters.
        i = 0
        while i < n:
            current_char = word[i]
            block_length = 0
            
            # Use a nested loop with pointer 'j' to find the end of the current block
            # and calculate its length.
            j = i
            while j < n and word[j] == current_char:
                block_length += 1
                j += 1
            
            # If the 'block_length' is greater than 1, it means this character was repeated
            # at least once. This block could be the specific location where Alice
            # over-pressed a key.
            # For a block of length 'L', it could have originally been of length 1, 2, ..., L-1.
            # Each of these (L-1) shorter lengths represents a distinct possible original string,
            # assuming this was the *only* instance of over-pressing.
            if block_length > 1:
                total_possible_strings += (block_length - 1)
            
            # Move the main pointer 'i' to the beginning of the next block
            i = j
            
        return total_possible_strings