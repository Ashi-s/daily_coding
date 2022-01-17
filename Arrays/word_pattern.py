# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
      d = {}
      visited_pattern = set()
      s = s.split(' ')

      if len(pattern) != len(s):
        return False
      
      for i, j in zip(pattern, s):
        if j not in d:
          if i in visited_pattern:
            return False
          d[j] = i
        else:
          if d[j] != i:
            return False
        visited_pattern.add(i)
      
      return True
        