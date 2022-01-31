# Design a data structure to find the frequency of a given value in a given subarray.

# The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

# Implement the RangeFreqQuery class:

# RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
# int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
# A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).


# Example 1:

# Input
# ["RangeFreqQuery", "query", "query"]
# [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
# Output
# [null, 1, 2]

# Explanation
# RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
# rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
# rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.

# M1 (TLE)
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
      d = {}
      for idx, val in enumerate(arr):
        if val in d:
          d[val].add(idx)
        else:
          d[val] = set()
          d[val].add(idx)
      self.d = d
      print(self.d)

    def query(self, left: int, right: int, value: int) -> int:
      if value not in self.d:
        return 0
      count = 0
      for idx in self.d[value]:
        if left <= idx <= right:
          count += 1
      return count

#M2
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
      d = {}
      for idx, val in enumerate(arr):
        if val in d:
          d[val].append(idx)
        else:
          d[val] = [idx]
      self.d = d
      
    def query(self, left: int, right: int, value: int) -> int:
      if value not in self.d:
        return 0
      count = 0
      arr = self.d[value]
      i, j = self.binarySearch(arr, left), self.binarySearch(arr, right)
      
      if j == len(arr): return j-i
      
      if arr[j] == right: j += 1
      
      return j-i
    
    def binarySearch(self, arr, target):
      left, right = 0, len(arr)
      
      while left < right:
        mid = (left + right) // 2
        
        if arr[mid] >= target:
          right = mid
        else:
          left = mid + 1
      return left