# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
 

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
      first = 0
      last = len(s) - 1
      s = list(s)
      while first < last:
        if s[first].isalpha() and s[last].isalpha():
          s[first], s[last] = s[last], s[first]
          first += 1
          last -= 1
          
        elif not s[first].isalpha():
          first += 1
        
        elif not s[last].isalpha():
          last -= 1
          
      return ''.join(s)
        