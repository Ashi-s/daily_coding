# This problem was asked by Google.

# You are in an infinite 2D grid where you can move in any of the 8 directions:

#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
# You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

# Example:

# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).


# https://www.geeksforgeeks.org/minimum-steps-needed-to-cover-a-sequence-of-points-on-an-infinite-grid/

def min_step(arr):
  steps = 0

  for i in range(len(arr)-1):
    steps += helper(arr[i], arr[i+1])

  return steps

def helper(A, B):
  x = abs(A[0] - B[0])
  y = abs(A[1] - B[1])
  return max(x, y)

arr = [(0, 0), (1, 1), (1, 2)]
print(min_step(arr))
arr1 = [(4, 6), (1, 2), (4, 5), (10, 12)]
print(min_step(arr1))