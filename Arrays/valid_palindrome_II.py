# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        def palindrome(str, left, right):
          while left < right:
            if s[left] != s[right]:
              return False

            left += 1
            right -= 1
        
          return True
        
        while left < right:
          if s[left] != s[right]:
            return palindrome(s, left+1, right) or palindrome(s, left, right-1)
          left += 1
          right -= 1
        
        return True