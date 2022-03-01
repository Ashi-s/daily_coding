# Magical Candy Bags
# You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
# It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish,
#  the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
# You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

# Output
# A single integer, the maximum number of candies you can eat in k minutes.
# Example 1
# N = 5 
# k = 3
# arr = [2, 1, 7, 4, 2]

# output = 14
# In the first minute you can eat 7 pieces of candy. That bag will refill with floor(7/2) = 3 pieces.
# In the second minute you can eat 4 pieces of candy from another bag. That bag will refill with floor(4/2) = 2 pieces.
# In the third minute you can eat the 3 pieces of candy that have appeared in the first bag that you ate.
# In total you can eat 7 + 4 + 3 = 14 pieces of candy.

#M1
import math
def maxCandies(arr, k):
  # Write your code here
  arr.sort(reverse= True)
  count = 0
  while k > 0:
    count += arr[0]
    arr[0] = math.floor(arr[0] / 2)
    arr.sort(reverse= True)
    k -= 1
  
  return count
arr = [2, 1, 7, 4, 2]

#M2 - using heap
#heapq doesn't provide an option for max heap therefore convert it into max by multiplying each element by -1
import heapq
def maxCandies1(arr, k):
  # Write your code here
  arr = [-1*i for i in arr]
  count = 0
  heapq.heapify(arr)
  while k > 0:
    tmp = heapq.nsmallest(1, arr)[0]
    tmp *= -1
    heapq.heappop(arr)
    count += tmp
    heapq.heappush(arr, math.floor(tmp/2) * -1)
    k -= 1
  
  return count

print(maxCandies1(arr, 3))