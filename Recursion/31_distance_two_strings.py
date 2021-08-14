# This problem was asked by Google.


# The edit distance between two strings refers to the minimum number of character insertions, deletions, 
# and substitutions required to change one string to the other. For example, 
# the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

# Given two strings, compute the edit distance between them.

## THIS SOLUTION IS WRONG BCOZ IT DOESN'T CONSIDER THE CASES LIKE "racecar" & "car" (or anyscenario where the match doesn't start from the first index)
def max_distance1(s1, s2):
  count = 0

  for i, j in zip(s1, s2):
    if i != j:
      count += 1
  
  dif = abs(len(s1) - len(s2))

  return count + dif

def max_distance2(s1, s2):
  res = helper(s1, s2, debt=0)
  return res

def helper(s1, s2, debt):
  if not s1 or not s2:
    return len(s1) + len(s2) + debt
  
  insertions = helper(s1, s2[1:], debt+1)
  deletion = helper(s1[1:], s2, debt+1)
  substitution = helper(s1[1:], s2[1:], debt + (s1[0] != s2[0]))

  return min(insertions, deletion, substitution)

print(max_distance2("a", "b"))
print(max_distance2("", ""))
print(max_distance2("abc", ""))
print(max_distance2("abc", "abc"))
print(max_distance2("kitten", "sitting"))
print(max_distance2("racecar", "car"))
