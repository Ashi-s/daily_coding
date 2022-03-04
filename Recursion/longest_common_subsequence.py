# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

def longestCommonSubsequence(text1, text2):
  n = len(text1)
  m = len(text2)
  
  LIS = [[0 for _ in range(len(text2)+1) ] for _ in range(len(text1) + 1)]
  
  for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
      if text1[i] == text2[j]:
        LIS[i][j] = 1 + LIS[i+1][j+1]
      else:
        LIS[i][j] = max(LIS[i+1][j], LIS[i][j+1])
  
  return LIS[0][0]