# Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

# https://leetcode.com/problems/expression-add-operators/discuss/230225/Python-solution

# Example 1:

# Input: num = "123", target = 6
# Output: ["1*2*3","1+2+3"]
# Example 2:

# Input: num = "232", target = 8
# Output: ["2*3+2","2+3*2"]
# Example 3:

# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
# Example 4:

# Input: num = "00", target = 0
# Output: ["0*0","0+0","0-0"]
# Example 5:

# Input: num = "3456237490", target = 9191
# Output: []

def addOperators( nums, target):
  def helper(idx, curr, prev, op):
    if idx == len(nums) and curr == target:
      res.append(op)
    else:
      curr_val = 0
      for i in range(idx, len(nums)):
        curr_val = 10*curr_val + int(nums[i])
        if idx == 0:
          helper(i+1, curr_val, curr_val, op + str(curr_val))
        else:
          #addition
          helper(i+1, curr + curr_val, curr_val, op + '+' + str(curr_val) )
          #substraction
          helper(i+1, curr - curr_val, -curr_val, op + '-' + str(curr_val) )
          #multiplication
          val = curr - prev 
          helper(i+1, val+ prev*curr_val, prev*curr_val, op + '*' + str(curr_val) )
          
        if nums[i] == '0':
          break
  
  res = []
  helper(0, 0, 0, '')
  return res

print(addOperators( nums = "123", target = 6))