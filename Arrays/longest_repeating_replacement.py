# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        #max length 26 chars(A-Z)
        d = {}
        
        left = 0
        
        for right in range(len(s)):
          d[s[right]] = d.get(s[right], 0) + 1
          
          if (right-left+1) - max(d.values()) <= k:
            res = max(res, right-left+1)
          else:
            while (right-left+1) - max(d.values()) > k:
              d[s[left]] -= 1
              left += 1
        
        return res