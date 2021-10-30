# Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

# Example 1:

# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# Example 2:

# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
      if len(expression) == 0:
        return 0
      
      if expression.isdigit():
        return [int(expression)]
      
      res = []
      for i in range(len(expression)):
        if expression[i] in ['-', '+', '*']:
          op = expression[i]
          left = self.diffWaysToCompute(expression[:i])
          right = self.diffWaysToCompute(expression[i+1:])
          
          for l in left:
            for r in right:
              if op == '+':
                res.append(l+r)
              if op == '-':
                res.append(l-r)
              if op == '*':
                res.append(l*r)
      return res
    
print(diffWaysToCompute('2*3-4*5'))