# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

# Example 1:


# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Example 2:

# Input: n = 1
# Output: [[1]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[None for _ in range(n)] for _ in range(n)]
        
        left, right = 0, n
        top, bottom = 0, n
        value = 1
        
        while left < right and top < bottom:
          #top row
          for i in range(left, right):
            grid[top][i] = value
            value += 1
          top += 1
          
          #right column
          for i in range(top, bottom):
            grid[i][right-1] = value
            value += 1
          right -= 1
          
          if not (left < right and top < bottom):
            break
          
          #bottom row
          for i in range(right-1, left-1, -1):
            grid[bottom-1][i] = value
            value += 1
          bottom -= 1
          
          #left column
          for i in range(bottom-1, top-1, -1):
            grid[i][left] = value
            value += 1
          left += 1
        
        return grid