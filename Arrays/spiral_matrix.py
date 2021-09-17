# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
      res = []
      res.extend(a[0])
      a.remove(a[0])

      while len(a) > 0:
          a = list(zip(*a))
          a.reverse()
          res.extend(a[0])
          a.remove(a[0])
          
      return res