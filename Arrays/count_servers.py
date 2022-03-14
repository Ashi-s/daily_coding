# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server.
#  Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

 

# Example 1:



# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# Example 2:



# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.
# Example 3:



# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other.
#  The server at right bottom corner can't communicate with any other server.
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
          return 0
        
        row_index = defaultdict(int)
        col_index = defaultdict(int)
        total = 0
        count = 0
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if grid[i][j] == 1:
              row_index[i] += 1
              col_index[j] += 1
              total += 1
        
        for i in range(len(grid)):
          for j in range(len(grid[0])):
            if grid[i][j] == 1:
              if max(row_index[i], col_index[j]) == 1:
                count += 1
        
        return total - count