# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      d1 = {}
      # create a hasmap of count
      for i in nums:
        if i in d1:
          d1[i] += 1
        else:
          d1[i] = 1
      
      d2 = {}
      max_freq = 0
      for key, val in d1.items():
        if val in d2:
          d2[val].append(key)
        else:
          d2[val] = [key]
        if val > max_freq:
          max_freq = val
      
      res = []
      for i in range(max_freq, -1, -1):
        if i in d2:
          res += d2[i]
        if len(res) >= k:
          return res