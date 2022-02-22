# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: columnTitle = "A"
# Output: 1
# Example 2:

# Input: columnTitle = "AB"
# Output: 28
# Example 3:

# Input: columnTitle = "ZY"
# Output: 701

def titleToNumber(columnTitle):
  # AA
  # 26^1 * 1 + 26^0 + 1
  res = 0
  n = len(columnTitle)-1
  for i in columnTitle:
    res += (26 ** n) * (ord(i) - ord('A')+ 1)
    n -= 1
  return res