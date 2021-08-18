# https://www.youtube.com/watch?v=21OuwqIC56E&ab_channel=KevinNaughtonJr.
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letter_combinations(digits):
  if len(digits) == 0:
    return []

  result = []

  mapping = {
    2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'
  }

  helper(result, digits, '', 0, mapping)
  return result

def helper(result, digits, current_str, index, mapping):
  if index == len(digits):
    result.append(current_str)
    return

  for i in mapping[int(digits[index])]:
    helper(result, digits, current_str + i, index+1, mapping)

print(letter_combinations("23"))