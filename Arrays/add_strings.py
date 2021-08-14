
# Input: num1 = "11", num2 = "123"
# Output: "134"
#this a wrong answer

def add_string(num1, num2):
  res  = []
  carry = 0
  for i, j in zip(num1[::-1], num2[::-1]):
    if carry:
      _sum = int(i)+int(j)+int(carry)
    else:
      _sum = int(i)+int(j)
    if _sum > 9:
      carry = str(_sum)[0]
      val = str(_sum)[1]
    else:
      val = str(_sum)
    res.append(val)
  
  if len(num1) > len(num2):
    for i in range(len(num1) - len(num2)):
      if carry:
        res.append(str(int(num1[i])+int(carry)))
        carry = 0
      else:
        res.append(num1[i])
  if len(num1) < len(num2):
      for i in range(len(num2) - len(num1)):
        if carry:
          res.append(str(int(num1[i])+int(carry)))
          carry = 0
      else:
        res.append(num2[i])
  
  return ''.join(res[::-1])

print(add_string(num1 = "11", num2 = "123"))
