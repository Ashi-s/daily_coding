# This problem was asked by Yelp.

# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

def phoneNumberCombination(mapping, digits):
  res = []
  helper(mapping, digits, res, 0, [])
  return res

def helper(mapping, digits, res, idx, curr):
  if len(curr) == len(digits):
    res.append(''.join(curr))
    return

  for ele in mapping[digits[idx]]:
    curr.append(ele)
    helper(mapping, digits, res, idx+1, curr)
    curr.pop()

mapping = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}
digits = '23'

print(phoneNumberCombination(mapping, digits))