# This problem was asked by Microsoft.

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

def running_median(s):
  res = []

  for i in range(len(s)):
    #even
    if (i+1) % 2 == 0:
      temp = sorted(s[:i+1])
      middle = len(temp)//2
      res.append((temp[middle]+temp[middle-1])/2)
    #odd
    else:
      temp = sorted(s[:i+1])
      middle = len(temp)//2
      res.append(temp[middle])
  return res

print(running_median([2, 1, 5, 7, 2, 0, 5]))
