# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# https://www.youtube.com/watch?v=cTBiBSnjO3c&ab_channel=NeetCode

def dailyTemperatures(temperatures):
  res = [0] * len(temperatures)
  st = []
  
  for i, val in enumerate(temperatures):
    if not st:
      st.append((i, val))
      continue
    else:
      print(st)
      while st and val > st[-1][1]:
        res[st[-1][0]] = i - st[-1][0]
        st.pop()

      st.append((i, val))
  
  return res

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))