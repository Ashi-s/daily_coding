# Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
# A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. 
# The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
# Note: This means you must swap two characters at different indices.

# Output
# Return an integer denoting the maximum number of matching pairs
# Example 1
# s = "abcd"
# t = "adcb"
# output = 4
# Explanation:
# Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
# Therefore, the number of matching pairs of s and t will be 4.

# Example 2
# s = "mno"
# t = "mno"
# output = 1
# Explanation:
# Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.

def matching_pairs(s, t):
  # Write your code here
  n = len(s)
  if s == t:
    return n-2
  
  unmatched_s = set()
  unmatched_t = set()
  unmatched = set()
  perfect_match = False
  partial_match = False
  count = 0
  
  for i, j in zip(s,t):
    if i == j:
      count += 1
    else:
      unmatched.add((i, j))
      unmatched_s.add(i)
      unmatched_t.add(j)
    
    if (j, i) in unmatched:
      perfect_match = True
    elif i in unmatched_t or j in unmatched_s:
      partial_match = True
  
  if perfect_match:
    return count + 2
  elif partial_match:
    return count + 1