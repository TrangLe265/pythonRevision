"""
Given an integer n, write a program to return the factorial of n. The Factorial of a number is the product of all the numbers from 1 to n.
"""
def factorial(n):
    factorial=1
    for i in range(1,n+1,1):
        factorial *= i
    return factorial

#print(factorial(3))

"""
Given an integer n. Write a program to print all the divisors of n in a single line.
"""
def divisor(n):
    output = []
    for i in range(1,n+1):
        if n%i == 0:
            output.append(i)
    
    print(*output)

#divisor(10)


        