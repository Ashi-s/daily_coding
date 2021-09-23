# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26

class Solution:
    def maxLength(self, arr: List[str]) -> int:
      res = ['']
      def find_dup(a, b):
        for i in set(a):
          if i in b:
            return True
        return False
      for i in arr:
        if len(i) != len(set(i)):
          continue
        n = len(res)
        tmp = []
        j = 0
        while j < n:
          if not find_dup(i, res[j]):
            tmp.append(i + res[j])
          j += 1
        res.extend(tmp)
      _max = 0

      for ele in res:
        _max = max(_max, len(ele))
        
      return _max
        