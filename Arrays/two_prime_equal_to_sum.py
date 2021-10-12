# This problem was asked by Alibaba.

# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

# A solution will always exist. See Goldbach’s conjecture.

# Example:

# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible, return the lexicographically smaller solution.

# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

# [a, b] < [c, d]
# If a < c OR a==c AND b < d.

# https://www.geeksforgeeks.org/find-two-prime-numbers-with-given-sum/
#Step1: First find all the prime numbers in range(N) using Sieve of Eratosthenes. 
#Step2: Then traverse through and find the pair

def getAllPrimes(N):
  primes = [1] * (N+1)
  primes[0] = primes[1] = 0

  for i in range(2, len(primes)):
    if primes[i] == 1:
      for j in range(i*i, len(primes), i):
        primes[j] = 0

  return primes

def getPairs(N):
  prime_arr = getAllPrimes(N)

  for i in range(len(prime_arr)):
    if prime_arr[i] and prime_arr[N-i]:
      return i, N-i


print(getPairs(10))
print(getPairs(74))
