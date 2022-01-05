# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def helper(i):
          if i >= len(s):
            res.append(part.copy())
          
          for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]: #check palindrome
              part.append(s[i:j+1])
              helper(j+1)
              part.pop()
        
        helper(0)
        return res