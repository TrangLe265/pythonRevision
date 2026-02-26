"""
Given a positive integer x, the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, ... (in increasing order).
"""
def printIncreasingPower(x):
    power= 0
    for i in range(1,x):
        power = i**2
        if (power > x):
            break
        else:
            print(power, end = " ")
            
            
printIncreasingPower(10)