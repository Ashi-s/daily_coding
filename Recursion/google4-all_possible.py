#[(2,4) (4,5) (4,5)]  [range given 2-4 mens 2, 3, 4]
# output: ['244', '245', '254', '255', '344', '345', '354', '355', '444', '445', '454', '455']

def all_possible(nums):
  res = []
  helper(res, nums, 0, [], len(nums))

  return res

def helper(res, nums, index, curr, maxSize):
 
  if len(curr) == maxSize:
    res.append(''.join(curr))
    return 
  # if index > len(nums):
  #   return
  
  for i in range(nums[index][0], nums[index][1]+1):
    curr.append(str(i))
    # print(i, curr)
    helper(res, nums, index+1, curr, maxSize)
    curr.pop()

print(all_possible([(2,4), (4,5), (4,5)]))