# You are given an integer array of unique positive integers nums. Consider the following graph:

# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

# Example 1:


# Input: nums = [4,6,15,35]
# Output: 4
# Example 2:


# Input: nums = [20,50,9,63]
# Output: 2
# Example 3:


# Input: nums = [2,3,6,7,4,12,21,39]
# Output: 8

def largestComponentSize(nums):
    
    def dfs(v, node, max1):
      visited.add(v)
      for each in d[v]:
        if each not in visited:
          node += 1
          max1.add(node)
          dfs(each, node, max1)
    
    def factor(x, y):
      while y:
        x, y = y, x%y
      return x
      
    d = {}

    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if factor(nums[i], nums[j]) > 1:
          if nums[i] not in d:
            d[nums[i]] = [nums[j]]
          else:
            d[nums[i]].append(nums[j])
          
          if nums[j] not in d:
            d[nums[j]] = [nums[i]]
          else:
            d[nums[j]].append(nums[i])
    
    max1 = set()
    # print( d)
    for v in nums:
      node = 1
      visited = set()
      if v not in visited:
        dfs(v, node, max1)
    
    return max(max1)
print(largestComponentSize([4, 6, 15, 35]))
print(largestComponentSize([20,50,9,63]))
print(largestComponentSize([2,3,6,7,4,12,21,39]))

        