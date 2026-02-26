"""
You are given an array arr[] of non-negative integers. You have to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. The operation must be performed in place, meaning you should not use extra space for another array.
"""
def pushZerosToEnd(arr):
    pointer_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[pointer_index] = arr[pointer_index], arr[i]
            pointer_index += 1
            
    return arr

#print(pushZerosToEnd([1,0, 4, 3, 0, 5, 0]))

def push_even_number_to_end(arr):
    p_index = 0
    for i in range( len(arr)):
        if arr[i]%2 != 0:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1
    
    return arr

print(push_even_number_to_end([1,23,4,5,6,8]))