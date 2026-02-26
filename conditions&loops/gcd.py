"""
Given two numbers a and b. The task is to find the GCD of  a and b.
The GCD of two numbers is the largest number that can divide both a and b perfectly.
"""

def find_gcd(a,b):
    gcd = 1
    limit = min(a,b) +1 

    for i in range(1,limit):
        if (a%i == 0 and b%i == 0):
            gcd=i

    return gcd
        
print(find_gcd(4,4))