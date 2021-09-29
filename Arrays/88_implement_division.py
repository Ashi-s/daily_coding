# This question was asked by ContextLogic.

# Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

def implement_division(n1, n2):
  quo = 0
  if n2 > n1:
    n1, n2 = n2, n1
  while n1 >= n2:
    quo += 1
    n1 -= n2
  
  return quo

print(implement_division(15, 5))
print(implement_division(13, 5))
print(implement_division(3, 22))