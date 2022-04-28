# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

# Example 1:



# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:



# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:


# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

import heapq

#M1 Recursion TLE
def minimumEffortPath(heights):
  m, n = len(heights), len(heights[0])
  def helper(r, c, curr, res, visited):
    if r >= m or c >=n:
      return
    if r == m-1 and c == n-1:
      res.append(curr.copy())
      return

    lst = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

    for row, col in lst:
      if row >= 0 and row < m and col >= 0 and col < n and (row, col) not in visited:
        curr.append(abs(heights[r][c] - heights[row][col]))
        visited.add((row, col))
        helper(row, col, curr, res, visited)
        curr.pop()
        visited.remove((row, col))

  if m == 1 and n == 1:
    return 0
  res = []
  visited = set()
  visited.add((0,0))
  helper(0, 0, [], res, visited)

  _min = float('inf')

  for ele in res:
    _min = min(_min, max(ele))
  return _min
      
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffortPath(heights))

#M2 Min heap
def minimumEffortPath2(heights):
  heap = [(0, (0,0))]
  m, n = len(heights), len(heights[0])
  heapq.heapify(heap)
  
  visited = set()
  cost = [[float('inf')]*n for _ in range(m)]
  cost[0][0] = 0
  
  while heap:
    ele = heapq.heappop(heap)
    val = ele[0]
    r, c = ele[1]
    
    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
      if 0<=nr<m and 0<=nc<n and (nr, nc) not in visited:
        dist = abs(heights[nr][nc] - heights[r][c])
        dist = max(dist, val)
        
        if dist < cost[nr][nc]:
          cost[nr][nc] = dist
          heapq.heappush(heap, (dist, (nr,nc)))
  
  return cost[m-1][n-1]