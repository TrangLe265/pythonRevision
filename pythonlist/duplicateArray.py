"""
You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.
"""

# the arr is sorted, so basically u only need to check if the 2 values next to each other is the same
def solution(arr):
    result = [arr[0]]

    for i in range (1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    
    return result
