# Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. 
# Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
 

# Example 1:

# Input: 
# n = 4, arr1[] = [1 3 5 7] 
# m = 5, arr2[] = [0 2 6 8 9]
# Output: 
# arr1[] = [0 1 2 3]
# arr2[] = [5 6 7 8 9]
# Explanation:
# After merging the two 
# non-decreasing arrays, we get, 
# 0 1 2 3 5 6 7 8 9.

def merge(arr1,arr2,n,m):
    #code here
    s1, s2, e1, e2 = 0, 0, n-1, m-1
    
    while s1 <= n and s2 <= m and s1 <= e1 and s2 <= e2:
        if arr2[s2] <= arr1[s1]:
            arr2[s2], arr1[e1] = arr1[e1], arr2[s2]
            s2 += 1
            e1 -= 1
        else:
            s1 += 1
    
    arr1.sort()
    arr2.sort()

    return arr1, arr2

n = 4
arr1 = [1, 3, 5, 7] 
m = 5
arr2 = [0, 2, 6, 8, 9]
print(merge(arr1, arr2, n,m))


