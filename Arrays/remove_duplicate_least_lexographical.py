# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
      d = {c: i  for (i, c) in enumerate(s)}
      
      st = []
      
      for i, c in enumerate(s):
        if c not in st:
          while st and c < st[-1] and i < d[st[-1]]:
            st.pop()
          st.append(c)
      
      return ''.join(st)