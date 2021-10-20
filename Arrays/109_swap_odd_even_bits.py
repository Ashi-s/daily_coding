def swap_odd_even_bits(s):
  s = [i for i in s]
  for i in range(0, len(s), 2):
    s[i], s[i+1] = s[i+1], s[i]
  return ''.join(s)

s = '10101010' # 01010101. 
s1 = '11100010' #11010001.
print(swap_odd_even_bits(s))
print(swap_odd_even_bits(s1))