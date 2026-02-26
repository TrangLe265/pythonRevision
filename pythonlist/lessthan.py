"""
You are given a number k and a list arr[] that contains integers. You need to return list of numbers that are less than k
"""
def less_than(k, arr):
    new = [x for x in arr if x < k]
    print(*new)

less_than(10, [1,124,4])

#Average: You are given a list arr that contains integers. You need to return average of the non negative integers.
def nonNegativeAverage(arr):
    non_neg=[x for x in arr if x >= 0]
    return (sum(non_neg)/len(non_neg))

print(nonNegativeAverage([1,2,3]))

#Given a list of positive integer, find second largest
def second_largest(arr):
    if (len(arr) < 2):
        return -1
    largest,second = -1,-1

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

second_largest([1,412,515,4])



