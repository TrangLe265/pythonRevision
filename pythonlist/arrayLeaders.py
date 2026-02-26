"""
You are given an array arr of positive integers. Your task is to find all the leaders in the array. An element is considered a leader if it is greater than or equal to all elements to its right. The rightmost element is always a leader.
"""
def solution(arr):
    result =[arr[-1]] #last number of arr is always the leader

    for i in range(len(arr)-2,-1,-1):
        current_num = arr[i]
        is_leader= True
        for j in range(i+1,len(arr)):
            if current_num < arr[j]:
                is_leader = False
                break
        if is_leader:
            result.insert(0,current_num)
    
    return result

print(solution([10, 4, 2, 4, 1]))

def solution_2(arr):
    result =[arr[-1]] #last number of arr is always the leader
    current_max = arr[-1]

    for i in range(len(arr)-2, -1, -1):
        if arr[i] >= current_max:
            current_max = arr[i]
            result.insert(0,current_max)
    
    return result

print(solution_2([10, 4, 2, 4, 1]))


