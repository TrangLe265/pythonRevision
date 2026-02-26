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