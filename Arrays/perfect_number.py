# This problem was asked by Microsoft.

# A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.
def perfect_number(n):
  res = []
  num = 1
  while len(res) != n:
    tmp = str(num)
    val = 0
    for i in tmp:
      val += int(i)

    if val == 10:
      res.append(tmp)
    
    num += 1
  return res[-1]

print(perfect_number(1))
print(perfect_number(2))
print(perfect_number(3))
print(perfect_number(4))
print(perfect_number(5))
