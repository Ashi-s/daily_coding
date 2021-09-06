# https://leetcode.com/problems/orderly-queue/discuss/1446596/Python-easy-n2-solution-with-video-explanation-easy-to-understand

# You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

 

# Example 1:

# Input: s = "cba", k = 1
# Output: "acb"
# Explanation: 
# In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
# In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
# Example 2:

# Input: s = "baaca", k = 3
# Output: "aaabc"
# Explanation: 
# In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
# In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
      output = s
      if k == 0:
        return s
      elif k == 1:
        for i in range(len(s)):
          temp = s[1:] + s[0]
          output = min(output, temp)
          s = temp
      else:
        return ''.join(sorted(s))
      
      return output
          