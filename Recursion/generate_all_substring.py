
def all_substring(s):
  res = []
  max_len = 0
  helper(res, s, 0, [], max_len)
  return max_len

def helper(res, s, index, curr, max_len):
  if index >= len(s):
    # res.append(''.join(curr))
    return
  
  for i in range(index, len(s)):
    curr.append(s[i])
    print(i, curr)
    res.append(''.join(curr))
    if is_palindrome(''.join(curr)):
      print('inside is_palindrome')
      if max_len < len(curr):
        max_len = len(curr)
        print('inside max_len', max_len, len(curr))
    helper(res, s, i+1, curr, max_len)
    curr.pop()

def is_palindrome(s):
  left = 0
  right = len(s)-1
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True


print(all_substring('babad'))