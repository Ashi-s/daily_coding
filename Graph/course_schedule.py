# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = {i:[] for i in range(numCourses)}
        
        for cor, preq in prerequisites:
          adjacency[cor].append(preq)
          
        def helper(node):
          nonlocal result
          if node in visited:
            result = False
            return
          visited.add(node)
          for n in adjacency[node]:
            helper(n)
          visited.remove(node)
          adjacency[node] = []
          
        visited = set()
        result = True
        for i in range(numCourses):
          helper(i)
        
        return result

#M2
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {c:[] for c in range(numCourses)}
        
        for i, j in prerequisites:
          d[i].append(j)
        
        cycle = set()
        visited = set()
        result = []
        isCycle = False
        def dfs(node):
          nonlocal result, isCycle
          if node in cycle:
            isCycle = True
            result = []
            return
          
          if node in visited:
            return
          
          cycle.add(node)
          for ch in d[node]:
            dfs(ch)
          
          cycle.remove(node)
          visited.add(node)
          if not isCycle: result.append(node)
        
        
        for i in range(numCourses):
          if i not in visited:
            dfs(i)
        
        return result