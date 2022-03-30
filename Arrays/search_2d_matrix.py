# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
 

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
      row = len(matrix) + 1
      
      for i in range(len(matrix)):
        if matrix[i][0] == target or  matrix[i][-1] == target:
          return True
        elif matrix[i][0] < target < matrix[i][-1]:
          row = i
      
      if row == len(matrix) + 1: return False
      
      #binary search in row
      left = 0
      right = len(matrix[0]) - 1
      
      while left < right:
        mid = (left + right) // 2
        
        if matrix[row][mid] == target:
          return True
        
        if target > matrix[row][mid]:
          left = mid+1
        else:
          right = mid
      
      return False