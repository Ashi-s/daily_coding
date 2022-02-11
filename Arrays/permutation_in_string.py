# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      c1 = collections.Counter(s1)
      c2 = collections.Counter(s2[0:len(s1)])
      
      i = 0
      while i < len(s2)-len(s1):
        if c1 == c2:
          return True
        tmp = s2[i+len(s1)]
        
        if tmp in c2:
          c2[tmp] += 1
        else:
          c2[tmp] = 1
        
        c2[s2[i]] -= 1
        
        if c2[s2[i]] == 0:
          del c2[s2[i]]
        
        i += 1
      
      return c1==c2