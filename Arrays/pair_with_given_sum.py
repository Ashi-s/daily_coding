# arr = [8, 7, 2, 5, 3, 1]
# sum = 10
# also called 2 sum problem

def pair_sum(input, s):
  d = {}
  for idx, value in enumerate(input):
    if s - value in d:
      return (value, input[d[s-value]])
    else:
      d[value] = idx
  return "not found"

if __name__ == '__main__':
  input = [8, 7, 2, 5, 3, 1]
  print(pair_sum(input, 10))
  print(pair_sum([3,3], 6))
  print(pair_sum([3,2,4], 6))