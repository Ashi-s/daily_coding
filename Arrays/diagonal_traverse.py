# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:


# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
# Example 2:

# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}
        
        for i in range(len(mat)):
          for j in range(len(mat[0])):
            if i+j in d:
              d[i+j].append(mat[i][j])
            else:
              d[i+j] = [mat[i][j]]
        
        isDown = False
        res = []
        res.extend(d[0])

        for val in list(d.values())[1:]:
          if isDown:
            res.extend(val[::-1])
          else:
            res.extend(val)
          isDown = not isDown
        
        return res