# https://leetcode.com/problems/generate-parentheses/
# https://www.youtube.com/watch?v=qBbZ3tS0McI&ab_channel=NickWhite

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

def generate_parenthesis(n):
  if n == 0:
    return []
  result = []

  helper(result, n, '', 0, 0, n*2)
  return result

def helper(result, n, current_str, open, close, max_size):
  if len(current_str) == max_size:
    result.append(current_str)
    return

  if open < n:
    helper(result, n, current_str + '(', open+1, close, max_size)

  if close < open:
    helper(result, n, current_str + ')', open, close +1, max_size)

print(generate_parenthesis(3))