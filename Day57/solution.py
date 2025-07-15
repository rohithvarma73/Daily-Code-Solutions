class Solution:
  def isValid(self, word: str) -> bool:
    VOWELS = 'aeiouAEIOU'  # Define all lowercase and uppercase vowels

    # Helper function to check if a character is a consonant
    def isConsonant(c: str) -> bool:
      return c.isalpha() and c not in VOWELS  # Must be a letter and not a vowel

    # Return True only if all the following conditions are met:
    return (
      len(word) >= 3 and                             # Condition 1: At least 3 characters
      all(c.isalnum() for c in word) and             # Condition 2: Only letters and digits (no special characters)
      any(c in VOWELS for c in word) and             # Condition 3: At least one vowel
      any(isConsonant(c) for c in word)              # Condition 4: At least one consonant
    )
