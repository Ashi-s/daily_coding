# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# Method 1 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
      A, B = len(a), len(b)
      if A > B:
        b = '0' * (A-B) + b
      elif B > A:
        a = '0' * (B-A) + a
      
      carry = 0
      res = []
      for i in range(len(a)-1, -1, -1):
        tmp = int(a[i]) + int(b[i]) + carry
        if tmp == 2:
          res.append('0')
          carry = 1
        elif tmp == 3:
          res.append('1')
          carry = 1
        else:
          res.append(str(tmp))
          carry = 0
      if carry == 1:
        res.append(str(carry))
      return ''.join(res[::-1])

# Method 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary = bin(int(a,2) + int(b,2))
        return str(binary)[2:]