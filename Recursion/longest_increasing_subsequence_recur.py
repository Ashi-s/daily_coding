# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given an array of numbers, find the length of the longest increasing subsequence in the array. 
# The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
#  the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

def LIS(s):
  L = [1]*len(s)

  for i in range(len(s)-1, -1, -1):
    for j in range(i+1, len(s)):
      if s[j] > s[i]:
        L[i] = max(L[i], 1+L[j])
  
  return L[0]
print(LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))