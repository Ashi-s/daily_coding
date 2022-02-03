# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

# Example 1:

# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
# Example 2:

# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab = {}
        res = 0
        for a in A:
          for b in B:
            tmp = a+b
            if tmp in ab:
              ab[tmp] += 1
            else:
              ab[tmp] = 1
        
        for c in C:
          for d in D:
            tmp = -(c+d)
            if tmp in ab:
              res += ab[tmp]
        
        return res