# Hey all, I recieved a question called "String to Int" in an interview, and 
# I was flabberghasted at how simple it sounded at first, but difficult it is in practice.

# Turn a string to a number

# Example 1:

# Input: "Three hundred million"
# Output: 300,000,000
# Example 2:

# Input: "Five Hundred Thousand"
# Output: 500,000

digits = {
  'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten': 10
}

teens = {
  'eleven': 11, 'tweleve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17, 'eighteen': 18, 'nineteen': 19
}

tys = {
  'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninty': 90
}

big = {
  'thousand': 1000, 'million': 1000000, 'billion': 1000000000
}
def english_word_to_integer(s):
  res = 0
  tmp =0

  for i in s.split(' '):
    if i in digits:
      tmp += digits[i]
    
    elif i in teens:
      tmp += teens[i]
    
    elif i in tys:
      tmp += tys[i]
    
    elif i == 'hundred':
      tmp *= 100
    
    elif i in big:
      res += tmp * big[i]
      tmp = 0
  
  res += tmp

  return res

print(english_word_to_integer("three hundred million"))
print(english_word_to_integer("five hundred thousand"))
print(english_word_to_integer("twenty one"))
print(english_word_to_integer("seven billion three hundred million nine hundred seventy thousand seven hundred nineteen"))
print(english_word_to_integer("fourteen thousand one hundred forty"))

