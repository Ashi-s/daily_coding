# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
      res = []
      
#       #  M1 basic loop through all possibility
#       for i in range(low, high+1):
#         n = str(i)
#         is_sequential = True
#         for j in range(1, len(n)):
#           if int(n[j]) != int(n[j-1]) + 1:
#             is_sequential = False
        
#         if is_sequential:
#           res.append(i)
      
      #M2 optimized
      l, h = len(str(low)), len(str(high))
      for i in range(l, h+1):
        for j in range(1, 9-i+2):
          tmp = ''
          for k in range(i):
            tmp += str(j+k)
          if low <= int(tmp) <= high:
            res.append(int(tmp))
      return res