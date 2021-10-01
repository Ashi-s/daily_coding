# This question was asked by Google.

# Given an integer n and a list of integers l, 
# write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
from random import randint

def generate_random(l, n):
  if len(l) == 0:
    return randint(0, n)
  l.insert(0, 0)
  l.append(n)
  prev = -1
  res = []
  for i in range(len(l)):
    r = randint(prev+1, l[i])
    res.append(r)
    prev = l[i]
  print(res)
  return res[randint(0, len(res)-1)]

print(generate_random([1,5], 1000))