# Reference
# https://www.youtube.com/watch?v=u0n-6zBnohY&ab_channel=AlgorithmsMadeEasy
# https://leetcode.com/problems/minimize-deviation-in-array/discuss/1042557/Python-Cleanest-Solution-or-Sorted-List-or

# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
# Example 2:

# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
# Example 3:

# Input: nums = [2,10,8]
# Output: 3

from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
      #if odd multiply by 2 and make it even
      sl = SortedList([ i*2 if i%2 == 1 else i for i in nums])
      
      diff = float('inf')
      
      while sl[-1] % 2 == 0:
        diff = min(diff, sl[-1] - sl[0])
        sl.add(sl.pop(-1) // 2)
      
      return min(diff, sl[-1]-sl[0])