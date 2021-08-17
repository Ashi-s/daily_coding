
def fib(n):
  if n <= 1:
    return n
  if F[n] != -1:
    return F[n]
  else:
    F[n] = fib(n-1) + fib(n-2)
  return F[n]

if __name__ == '__main__':
  n = 40
  F = [-1] * (n+1)
  print(fib(n))