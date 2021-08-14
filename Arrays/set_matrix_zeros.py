# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

# You must do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

def setZeroes(matrix):
  """
  Do not return anything, modify matrix in-place instead.
  """
  row_set = set()
  col_set = set()
  
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 0:
        row_set.add(i)
        col_set.add(j)
  
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if i in row_set or j in col_set:
        matrix[i][j] = 0
              
  return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
                
        