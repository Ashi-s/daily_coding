# x^n

#m1
# recurrence relation
#x * x^(n-1) if n > 0
#1           if n = 0
def pow(x,n):
  if n == 0:
    return 1
  return x * pow(x, n-1)

#m2
#recurrence relation
#x^(n/2) * x^(n/2) if n%2 == 0(even)
#x * x^(n-1)       if n%2 != 0 (odd)
#1                 if n == 0
def pow2(x, n):
  if n == 0:
    return 1
  elif n%2 == 0:
    y = pow2(x, n//2)
    return y * y
  else:
    return x * pow2(x, n-1)

print(pow(40,40))
print(pow2(40, 40))