# Revenue Milestones
# We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. 
# Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.\

# Signature
# int[] getMilestoneDays(int[] revenues, int[] milestones)
# Input
# revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
# Output
# Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.

# Example
# revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# milestones = [100, 200, 500]
# output = [4, 6, 10]
# Explanation
# On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time that FB has >= $200 of total revenue.

# Wrong - if milestone is not sorted
# def getMilestoneDays(revenues, milestones):
#   # Write your code here
#   summ = 0
#   j = 0
#   res = []
#   for i in range(len(revenues)):
#     summ += revenues[i]
#     while summ >= milestones[j]:
#       res.append(i+1)
#       j += 1
#       if j == len(milestones):
#         break
#   return res

def getMilestoneDays(revenues, milestones):
  prefix_sum = []
  res = []
  summ = 0
  for i in revenues:
    summ += i
    prefix_sum.append(summ)
  
  def search(target):
    left = 0
    right = len(prefix_sum)

    while left < right:
      mid = (left + right) // 2

      if prefix_sum[mid] < target:
        left = mid + 1
      else:
        right = mid
    
    return left + 1

  for m in milestones:
    res.append(search(m))
  
  return res
revenues_1 = [100, 200, 300, 400, 500]
milestones_1 = [300, 800, 1000, 1400]

print(getMilestoneDays(revenues_1, milestones_1)) #[2, 4, 4, 5]


revenues_2 = [700, 800, 600, 400, 600, 700]
milestones_2 = [3100, 2200, 800, 2100, 1000] 

print(getMilestoneDays(revenues_2, milestones_2)) #[5, 4, 2, 3, 2]