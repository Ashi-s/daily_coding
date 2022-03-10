# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height):
      maxLeft =[0]
      maxRight = [0]
      max_left = 0
      max_right = 0
      water = 0
      
      for i in range(1, len(height)):
        max_left = max(max_left, height[i-1])
        maxLeft.append(max_left)
        
      for i in range(len(height)-2, -1, -1):
        max_right = max(max_right, height[i+1])
        maxRight.append(max_right)
      
      maxRight = maxRight[::-1]
      
      for i in range(len(height)):
        val =  min(maxLeft[i], maxRight[i]) -height[i]
        
        if val > 0:
          water += val
      
      return water