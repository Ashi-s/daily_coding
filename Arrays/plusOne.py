# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

def plusOne(digits):
  num = 0
  out = []
  for i in range(len(digits)):
    num *= 10
    num += digits[i]

  num += 1

  while num:
    temp = num % 10
    num //= 10
    out.append(temp)

  return out[::-1]

#Method 2

def plusOne2(digits):
  val = [str(i) for i in digits]
  val = int(''.join(val))
  val += 1

  out = [int(i) for i in str(val)]
  return out


if __name__ == '__main__':
  digits = [1,2,3]
  print(plusOne2(digits))

