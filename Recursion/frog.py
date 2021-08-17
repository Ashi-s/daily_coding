#problem link https://www.youtube.com/watch?v=5o-kdjv7FD0&ab_channel=CSDojo

def frog_jump_ways(n):
  #can either jump 1 step or 2 steps
  if n==1:
    return 1
  elif n ==2:
    return 2
  else:
    return frog_jump_ways(n-1) + frog_jump_ways(n-2)

#memoization
def frog_jump_ways2(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif N[n] != -1:
    return N[n]
  else:
    N[n] = frog_jump_ways2(n-1) + frog_jump_ways2(n-2)
    return N[n]

#instead of just 1 *=& 2 steps if an array of steps possible is given
# e.g you can take {1, 3, 5} steps
def frog_jump_with_steps_given(n, jump):
  if n == 0: return 1
  N[0] = 1
  for i in range(1, n+1):
    total = 0
    for j in jump:
      if i-j >= 0:
        total += N[i-j]
    N[i] = total
  print(N)
  return N[n]


if __name__ == '__main__':
  n = 5
  print(frog_jump_ways(n))

  N = [-1] * (n+1)
  print(frog_jump_ways2(n))

  jump = [1, 3, 5]
  print(frog_jump_with_steps_given(n, jump))
