# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

 

# Example 1:


# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count_tops = [0] * 7
        count_bottom = [0]*7
        common = [0] * 7
        
        n = len(tops)
        res = n
        
        for i in range(n):
          count_tops[tops[i]] += 1
          count_bottom[bottoms[i]] += 1
          
          if tops[i] == bottoms[i]:
            common[tops[i]] += 1
          
        
        for i in range(1, 7):
          if count_tops[i] + count_bottom[i] - common[i] == n:
            res = min(res, n - max(count_tops[i], count_bottom[i]))
        
        if res == n:
          return -1
        else:
          return res
        