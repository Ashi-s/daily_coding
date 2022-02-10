# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, 
# and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
# https://leetcode.com/problems/redundant-connection/discuss/851877/Python-by-union-find-w-Visualization

##Union find

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
      
      parent = {v:-1 for v in range(1, len(edges) + 1)}
      
      def find(u):
        if parent[u] == -1:
          return u
        else:
          parent[u] = find(parent[u])
          return parent[u]
      
      for u, v in edges:
        parent_u = find(u)
        parent_v = find(v)
        
        if parent_u == parent_v:
          return [u, v]
        else:
          parent[parent_u] = parent_v
        