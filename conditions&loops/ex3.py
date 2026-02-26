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

"""
Given an integer n. Write a program to find the first prime number greater than n.
"""
import math
def nextPrime(n):
    current_num = n + 1

    while True:
        is_prime = True
        if current_num < 2:
            is_prime = False
        elif current_num == 2:
            return current_num
        elif current_num%2 == 0:
            is_prime = False
        else:
            # after checking 2, only odd number need to be checked
            for i in range(3,int(math.sqrt(current_num)) +1, 2):
                if current_num%i == 0:
                    is_prime = False
                    break
        if is_prime:
            return current_num    

        current_num += 1
           
print(nextPrime(31))
        