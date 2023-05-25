class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

      # Count the frequency of characters in magazine using Counter
      freq_b = Counter(magazine)

      # Check if each character in ransomNote can be constructed using the characters from magazine
      for char in ransomNote:
          # If the count of the character in magazine is zero, it is missing in magazine
          if freq_b[char] == 0:
              return False

          # Decrement the count of the character in freq_b to indicate its usage
          freq_b[char] -= 1

      return True
