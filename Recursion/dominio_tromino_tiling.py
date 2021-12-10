# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.


# Example 1:

# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1

# https://www.youtube.com/watch?v=CecjOo4Zo-g
class Solution:
    def numTilings(self, n: int) -> int:
      MOD = 1000000007
      count = 0
      dp = [[None]*4] * (n+1)
      print(dp)
      def getState(t1, t2):
        if not t1 and  not t2: return 0
        elif t1 and not t2: return 1
        elif not t1 and t2: return 2
        else: return 3
      
      def helper(idx, t1, t2):
        nonlocal count
        if idx == n:
          return 1
        state = getState(t1, t2)
        
        if dp[idx][state] != None:
          return dp[idx][state]
        
        t3, t4 = idx+1<n, idx+1<n
        
        if t1 and t2 and t3:
          count += helper(idx+1, False, True)
        
        if t1 and not t2 and t3 and t4:
          count += helper(idx+1, False, False)
        
        if t1 and t2 and t3:
          count += helper(idx+1, True, False)
        
        if not t1 and t2 and t3 and t4:
          count += helper(idx+1, False, False)
        
        if t1 and t2:
          count += helper(idx+1, True, True)
        
        if t1 and not t2 and t3:
          count += helper(idx+1, False, True)
          
        if not t1 and not t2 and t4:
          count += helper(idx+1, True, False)
        
        if t1 and t2 and t3 and t4:
          count += helper(idx+1, False, False)
        
        if not t1 and not t2:
          count += helper(idx+1, True, True)
        
        dp[idx][state] = count % MOD
        return dp[idx][state]
      helper(0, True, True)
      return count
        