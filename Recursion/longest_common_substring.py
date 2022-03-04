# Given two strings. The task is to find the length of the longest common substring.


# Example 1:

# Input: S1 = "ABCDGH", S2 = "ACDGHR"
# Output: 4
# Explanation: The longest common substring
# is "CDGH" which has length 4.
# Example 2:

# Input: S1 = "ABC", S2 "ACB"
# Output: 1
# Explanation: The longest common substrings
# are "A", "B", "C" all having length 1.


def longestCommonSubstr(S1, S2, n, m):
  # code here
  _max = 0
  LCS = [[0 for _ in range(m+1)] for _ in range(n+1)]
  
  for i in range(n-1, -1, -1):
      for j in range(m-1, -1, -1):
          if S1[i] == S2[j]:
              LCS[i][j] = 1 + LCS[i+1][j+1]
              _max = max(_max,LCS[i][j] )
  print(LCS)
  return _max

S1 = "ABCDGH"
S2 = "ACDGHR"
n, m = 6, 6
print(longestCommonSubstr(S1, S2, n,m))
