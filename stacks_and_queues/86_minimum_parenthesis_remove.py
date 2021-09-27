# This problem was asked by Google.

# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.

def minimumparenthesisRemove(str):
  count = 0
  st = []

  for p in str:
    if p == '(':
      st.append(p)
    elif p == ')' and len(st) > 0:
      st.pop()
    elif p == ')':
      count += 1

  return count + len(st)

print(minimumparenthesisRemove('()())()'))
print(minimumparenthesisRemove(')()'))