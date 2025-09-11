class Solution:
    def sortVowels(self, s: str) -> str:
        # Extract all vowels (both uppercase and lowercase) from the string
        vowels = [char for char in s if char.lower() in "aeiou"]
      
        # Sort the vowels in ascending order (uppercase letters come before lowercase)
        vowels.sort()
      
        # Convert string to list for character replacement
        characters = list(s)
      
        # Index to track position in sorted vowels list
        vowel_index = 0
      
        # Replace each vowel in the original string with sorted vowels
        for i, char in enumerate(characters):
            if char.lower() in "aeiou":
                characters[i] = vowels[vowel_index]
                vowel_index += 1
      
        # Join the list back into a string and return
        return "".join(characters)