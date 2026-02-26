"""
Sum of the First n Positive Integers
Write a program that takes a positive integer, n, as input and then displays the sum of all of the integers from 1 to n. The sum of the first n positive integers can be computed using the formula:

𝑠𝑢𝑚=n*(n+1)/2

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column
For example:

Input	Result
10
The sum of the first 10 positive integers is 55
4
The sum of the first 4 positive integers is 10
"""

def sum(n):
    sum = n*(n+1)//2
    print(f"The sum of the first {n} positive integers is {sum} ")

sum(10)