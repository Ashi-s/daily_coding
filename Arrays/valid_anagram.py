# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        
        if len(s) != len(t):
          return False
        for i, j in zip(s, t):
          d1[i] = d1.get(i, 0) + 1
          d2[j] = d2.get(j, 0) + 1
        
        return d1 == d2