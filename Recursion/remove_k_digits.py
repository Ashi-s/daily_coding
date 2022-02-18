# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.


# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.

#M1 Recursion TLE
def removeKdigits(num, k):
      
  def helper(num, n, idx, curr, res):
    nonlocal _min
    if len(curr) == n:
      if int(''.join(curr)) < _min:
        _min = int(''.join(curr))
        return
    if idx > len(num)-1 or len(curr) > n:
      return

    curr.append(num[idx])
    helper(num, n, idx+1, curr, res)
    
    curr.pop()
    helper(num, n, idx+1, curr, res)
      
  n = len(num) - k
  _min = float('inf')
  num = list(num)
  res = []
  helper(num, n, 0, [], res)
  return _min

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
      n = len(num)
      count = k
      if n == k:
        return '0'
      i = 0
      st = []
      
      while count > 0 and i < len(num):
        if st and st[-1] > num[i]:
          st.pop()
          count -= 1
        else:
          st.append(num[i])
          i += 1
      
      if count == 0:
        #to remove leading zeros
        return str(int(''.join(st) + num[i:]))
      else:
        return str(int(''.join(st[:n-k])))
      

print(removeKdigits('1432219', 3))