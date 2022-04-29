# https://www.youtube.com/watch?v=CscLi1gVGUk&ab_channel=TimothyHChang
# https://www.youtube.com/watch?v=-SpTh4AEZrk&ab_channel=AlgorithmsMadeEasy

# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

 

# Example 1:


# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
# Example 2:


# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1] * n
        
        
        
        #0 is red and 1 is blue
        
        #there is a possibility that graph is not connected
        #therefore check for each node
        for i in range(n):
          if col[i] != -1:
            continue
          q = deque()
          q.append((i, 0))
          
          while q:
            node, color = q.popleft()

            #not touched yet
            if col[node] == -1:
              col[node] = color

              for nn in graph[node]:
                q.append((nn, not color)) #bfs take all node adjacent & reverse the color

            if col[node] != color: #someone else reverted the color, conflict 
              return False
        
        return True