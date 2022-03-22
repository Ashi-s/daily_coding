# The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

# The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. 
# For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

# You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, 
# or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

# Example 1:

# Input: n = 3, k = 27
# Output: "aay"
# Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.
# Example 2:

# Input: n = 5, k = 73
# Output: "aaszz"

#M1 TLE
def getSmallestString(n, k):
  def helper(idx, summ, curr, res):
    if len(res) > 0:
      return

    if idx == n and summ == k:
      res.append(curr)
      return
    
    if idx >= n or summ >= k:
      return
    
    for i in 'abcdefghijklmnopqrstuvwxyz':
      tmp = ord(i)-ord('a')+1
      helper(idx+1, summ+tmp, curr+i, res)
      
  res = []
  helper(0, 0, '', res)
  return res[0]

n = 3
k = 27
print(getSmallestString(n, k))

n1 = 5
k1 = 73
print(getSmallestString(n1,k1))

def getSmallestString2(n, k):
  #assume every char is a at start
  res = ['a'] * n
  # k is reduced by n bcoz we assumed every char is a, so n times a
  k -= n

  for i in range(n-1, -1, -1):
    # since we have 'a' at all the n place, therefore we can add max 25 to make it 26
    val = min(k, 25)
    #97 bcoz we have 'a' present at that index
    res[i] = chr(97+val)
    k -= val

  return ''.join(res) 

n = 3
k = 27
print(getSmallestString2(n, k))

n1 = 5
k1 = 73
print(getSmallestString2(n1,k1))