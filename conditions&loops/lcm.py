"""
Given two numbers a and b. The task is to find out their Lowest Common Multiple.
"""

def find_lcm(a,b):
    i = min(a,b) + 1
    
    while i:
        if (i%a == 0 and i%b == 0):
            return i
        i +=1

print(find_lcm(14,8))