# A complex number can be represented as a string on the form "real+imaginaryi" where:

# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100, 100].
# i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

# Example 1:

# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
# Example 2:

# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

# Constraints:

# num1 and num2 are valid complex numbers.

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
      r1, im1 = split_number(num1)
      r2, im2 = split_number(num2)
      
      real_sum = r1*r2 + (im1*im2)*-1
      im_sum = (r1*im2) + (im1*r2)
      
      return str(real_sum) + '+' + str(im_sum) + 'i'
      
      
      
      
      

def split_number(n):
  temp = n.split('+')
  real = temp[0]
  imaginary = temp[1].split('i')[0]
  
  return [int(real), int(imaginary)]