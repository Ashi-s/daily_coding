# find peak element in the array

def get_peak(input):
  start = 0
  end = len(input) - 1
  mid = (start + end) // 2

  while True:
    if start == mid and end == mid:
      return input[mid]
    #mid is the peak element
    elif input[mid] > input[mid - 1] and input[mid] > input[mid + 1]:
      return input[mid]
    elif input[mid - 1] > input[mid]:
      end = mid - 1
    elif input[mid + 1] > input[mid]:
      start = mid + 1
    mid = (start + end) // 2

if __name__ == '__main__':
  input = [5, 10, 15, 25, 30, 45, 65, 50, 35, 1]
  input2 = [9, 8, 7, 6, 5, 4, 3]
  input3 = [1, 2, 3, 4, 5, 6, 7, 8]
  input4 = [8, 9, 10, 2, 5, 6]
  print(get_peak(input))
  print(get_peak(input2))
  print(get_peak(input3))
  print(get_peak(input4))
  print(get_peak([1,2,1,3,5,6,4]))
  print(get_peak([1,2]))
