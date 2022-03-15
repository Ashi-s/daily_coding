def numberToWords(nums):
  single_map = {1: "One",2: "Two",3: "Three",4: "Four",5: "Five",6: "Six",7: "Seven",8: "Eight",9: "Nine",10: "Ten",11: "Eleven",12: "Twelve",13: "Thirteen",14: "Fourteen",15:
    "Fifteen",16: "Sixteen",17: "Seventeen",18: "Eighteen",19: "Nineteen"
  }

  double_map = {
      2: "Twenty",3: "Thirty",4: "Forty",5: "Fifty",6: "Sixty",7: "Seventy",8: "Eighty", 9: "Ninety" 
  }

        
        
  def helper(nums):
    tmp = ''
    val = 0
    if len(nums) == 3:
      val = int(nums[0]) 
      if val in single_map:
        tmp += single_map[val] + ' Hundred '
        nums = nums[1:]
    
    if len(nums) == 2:
      val = int(nums) 
      if val in single_map:
        tmp += single_map[val]
      tens, ones = int(nums[0]), int(nums[1])
      if tens in double_map and ones in single_map:
        tens, ones = int(nums[0]), int(nums[1])
        tmp += double_map[tens] + ' ' + single_map[ones]
        
    if len(nums) == 1:
      val = int(nums) 
      tmp += single_map[val]
    
    return tmp
        
        
  if nums == 0: return 'Zero'

  nums = str(nums)
  output = ''
  if 1 <=len(nums) <= 3:
    return helper(nums)
  elif 4 <= len(nums) <=6:
    print(nums[:-3], nums[-3:])
    val1, val2 = helper(nums[:-3]), helper(nums[-3:])
    if len(val1) > 0:
      output += val1 + ' Thousand'
    if len(val2) > 0:
      output += ' ' + val2
  
  elif 7 <= len(nums) <=9:
    val1, val2, val3 = helper(nums[:-6]) , helper(nums[-6:-3]), helper(nums[-3:])
    print(val1, val2, val3)
    if len(val1) > 0:
      output += val1  + ' Million'
    if len(val2) > 0:
      output += ' ' + val2 + ' Thousand'
    if len(val3) > 0:
      output +=  ' ' + val3
      
  elif 10 <= len(nums) <=12:
    val1, val2, val3, val4 = helper(nums[:-9]), helper(nums[-9:-6]) , helper(nums[-6:-3]), helper(nums[-3:])
    if len(val1) > 0:
      output += val1  + ' Billion'
    if len(val2) > 0:
      output += ' ' + val2  + ' Million'
    if len(val3) > 0:
      output += ' ' + val3 + ' Thousand'
    if len(val4) > 0:
      output +=  ' ' + val4
  return output


# doesn't work for single digit and double digit
print(numberToWords(123))
        
        
        
        
        
        
        