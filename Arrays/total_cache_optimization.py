#output = max(i,j) * sum(i, j)
# e.g [2,3,1,2]
# max([2]) * sum([2])
# max([2,3]) * sum([2,3])
# max([2,3,1]) * sum([2,3,1])
# max([2,3,1,2]) * sum([2,3,1,2])

# max([3]) * sum([3])
# max([3,1]) * sum([3,1])
# max([3,1,2]) * sum([3,1.2])

# max([1]) * sum([1])
# max([1,2]) * sum([1,2])

# max([2]) * sum([2])


def findTotalPower(power):
    # Write your code here
    output = 0
    n = len(power)
    
    for i in range(n):
        min_value = power[i]
        summ = 0
        for j in range(i, n):
            if power[j] < min_value:
                min_value = power[j]
            summ += power[j]
            output += min_value * summ
    return output

print(findTotalPower([2,3,2,1]))