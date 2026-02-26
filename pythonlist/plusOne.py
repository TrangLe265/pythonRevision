"""
Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number (increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array.
"""
def plus_one(arr):
    #assume that the carry is 1 since the beginning, because we anyway need to add 1 to the 'number'
    carry = 1

    for i in range(len(arr)-1,-1, -1):
        #perform the add on
        total = arr[i] + carry
        #assign the arr value with the remainder of total % 10 
        #so if the original val = 9 and become 10 after the add on
        #remainder of 10%10 is 0
        #if original val = 7 and become 8 -> remainder 8%10 is 8 and so on
        arr[i] = total % 10 
        # calculate again if there is any more add on for the next number
        carry = total // 10

    if carry: #incase [9,9,9,9]
        arr.insert(0,1)

    return arr

print(plus_one([1,2,3,9]))