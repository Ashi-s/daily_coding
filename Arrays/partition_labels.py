# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]


#This problem can be convereted into Merge Intervals problem
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = collections.OrderedDict()
        
        for i,v in enumerate(s):
          if v not in d:
            d[v] = [i]
          else:
            if len(d[v]) == 1:
              d[v].append(i)
            else:
              d[v][1] = i
        
        intervals = list(d.values())
        
        low = intervals[0][0]
        high = intervals[0][0] if len(intervals[0]) == 1 else intervals[0][1]
        
        i = 1
        res = []
        while i < len(intervals):
          if intervals[i][0] < high:
            tmp = intervals[i][0] if len(intervals[i]) == 1 else intervals[i][1]
            high = max(high, tmp)
          else:
            res.append(high-low+1)
            low = intervals[i][0]
            high = intervals[i][0] if len(intervals[i]) == 1 else intervals[i][1]
          i+= 1
        res.append(high-low+1)
        return res