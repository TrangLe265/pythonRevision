"""
Given an integer n. Write a program to find the nth Fibonacci number.

F(0)= 0, F(1)=1
The nth Fibonacci number is given by the forumla F(n) = F(n-1) + F(n-2). The first few fibonacci numbers are: 0 1 1 2 3 5. . . . 
"""
def fibonacyn(n):
    if n<=1:
        return n 
    
    a,b = 0,1
    #in Python, _ is used as var name if we dont care about that var and only need the iteration to happen
    for _ in range(2,n+1):
        a,b = b, a+b
        # Assign value of b to a (new a)
        # Assign value of (a+b) to b (new b)
        # we are doing this to reduce the number of values to keep track of
    return b
