# You are given a string s of lowercase English letters and an integer array shifts of the same length.

# Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

# Return the final string after all such shifts to s are applied.

 

# Example 1:

# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
# Example 2:

# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
      _sum = sum(shifts)
      s = [i for i in s]
      for i in range(len(s)):
        s[i] = self.helper(s[i], _sum)
        _sum -= shifts[i]
        
      return ''.join(s)
    
    def helper(self, char, sh):
      asci = ord(char) - 96 + sh
      asci %= 26
      
      return 'z' if asci == 0 else chr(asci + 96)