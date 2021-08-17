#linear time & constant space
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

#M1 linear time & linear space
def minNumber(l):
    _set = set(l)
    for i in range(1, len(l)+1):
        if not i in _set:
            return i
    return len(l) + 1
    
# print(minNumber([3, 4, -1, 1]))
# print(minNumber([1, 2, 0]))


#M2
def min2(nums):
    print('inside min2')
    counter = 0
    for i in range(len(nums)):
        correctPos = nums[i]-1
        while 1 <= nums[i] <= len(nums) and nums[i] != nums[correctPos]:
            counter += 1
            print('inside while', nums)
            nums[i], nums[correctPos] = nums[correctPos], nums[i]
            correctPos = nums[i] - 1
            print(nums[i], nums[nums[i]-1] )
    print('final num: ', nums)
    print('counter: ', counter)
    for i in range(len(nums)):
        if nums[i] !=  i+1:
            return i+1
    return len(nums) +1

print(min2([3, 4, -1, 1]))
            
            