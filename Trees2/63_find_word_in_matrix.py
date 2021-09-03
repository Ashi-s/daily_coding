# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

def find_word(mat, target):

  for r in range(len(mat)):
    for c in range(len(mat[r])):
      left_to_right = helper(mat, r, c, [], left=True, up=False)
      up_to_down = helper(mat, r, c, [], left=False, up=True)

      if target in ''.join(left_to_right):
        return True
      
      if target in ''.join(up_to_down):
        return True
  
  return False


def helper(mat, row, col, current, left, up):
  if left:
    while col < len(mat[row]):
      current.append(mat[row][col])
      col += 1

    return current

  if up:
    while row < len(mat):
      current.append(mat[row][col])
      row += 1
    
    return current

mat = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

target = 'FOAM'

print(find_word(mat, target))