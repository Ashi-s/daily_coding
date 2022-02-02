# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

#M1 TLE
def findAnagrams(s, p):
  p = list(p)
  p.sort()
  p = ''.join(p)
  S = len(s)
  P = len(p)
  res = []
  for i in range(S - P + 1):
    tmp = list(s[i:i+P])
    tmp.sort()
    if ''.join(tmp) == p:
      res.append(i)
  
  return res

#M2
import collections

def findAnagrams(s, p):
  c1 = collections.Counter(s[:len(p)])
  c2 = collections.Counter(p)
  
  i = 0
  res = []
  
  while i < (len(s) - len(p)):
    if c1 == c2:
      res.append(i)
    
    c = s[i + len(p)]
    
    if c in c1:
      c1[c] += 1
    else:
      c1[c] = 1
    
    c1[s[i]] -= 1
    
    if c1[s[i]] == 0:
      del c1[s[i]]
    
    i += 1
  
  if c1 == c2:
    res.append(i)
  return res

s = "cbaebabacd"
p = "abc"
s1 = "abab"
p1 = "ab"
s2 = "ababababab"
p2 = "aab"
print(findAnagrams(s,p))
print(findAnagrams(s1,p1))
print(findAnagrams(s2,p2))


