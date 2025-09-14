class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            """
            Replace all vowels in a word with '*' to create a vowel-agnostic pattern.
            """
            pattern = []
            for char in word:
                if char in "aeiou":
                    pattern.append("*")
                else:
                    pattern.append(char)
            return "".join(pattern)

        # Create a set for O(1) exact match lookups
        word_set = set(wordlist)
      
        # Dictionary to store first occurrence of each lowercase version
        lowercase_dict = {}
      
        # Dictionary to store first occurrence of each vowel pattern
        vowel_pattern_dict = {}
      
        # Build the dictionaries, keeping only the first occurrence of each pattern
        for word in wordlist:
            word_lower = word.lower()
          
            # Store first occurrence of lowercase version
            if word_lower not in lowercase_dict:
                lowercase_dict[word_lower] = word
          
            # Store first occurrence of vowel pattern
            pattern = devowel(word_lower)
            if pattern not in vowel_pattern_dict:
                vowel_pattern_dict[pattern] = word

        result = []
      
        # Process each query
        for query in queries:
            # Priority 1: Exact match (case-sensitive)
            if query in word_set:
                result.append(query)
                continue
          
            # Priority 2: Case-insensitive match
            query_lower = query.lower()
            if query_lower in lowercase_dict:
                result.append(lowercase_dict[query_lower])
                continue
          
            # Priority 3: Vowel error match (case-insensitive)
            query_pattern = devowel(query_lower)
            if query_pattern in vowel_pattern_dict:
                result.append(vowel_pattern_dict[query_pattern])
                continue
          
            # No match found
            result.append("")
          
        return result