# https://www.youtube.com/watch?v=XYQecbcd6_c&ab_channel=NeetCode
# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

def longestPalindrome(s):
  res = ''
  maxLen = 0

  for i in range(len(s)):
    odd = helper(i, i, s, maxLen)
    even = helper(i, i+1, s, maxLen)
    if len(odd) > len(res):
      res = odd
    if len(even) > len(res):
     res = even
    print(odd, even, res)
  return res
    
def helper(left, right,s, maxLen):
  temp = ''
  while left >=  0 and right < len(s) and s[left] == s[right]:
    if right-left+1 > maxLen:
      temp = s[left:right+1]
      maxLen = right-left+1
    left -= 1
    right += 1
  return temp

print(longestPalindrome(s='aaaa'))