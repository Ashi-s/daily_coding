# This problem was asked by Snapchat.

# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

# The input list is not necessarily ordered in any way.

# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
    def merge(intervals):
      
      if len(intervals) == 0:
        return []
      res = []
      intervals.sort(key = lambda x:x[0])
      
      start = intervals[0][0]
      end = intervals[0][1]
      
      for i in range(1, len(intervals)):
        if intervals[i][0] > end:
          res.append((start, end))
          start = intervals[i][0]
          end = intervals[i][1]
        else:
          end = max(end, intervals[i][1])
          
      res.append((start, end))
      return res
