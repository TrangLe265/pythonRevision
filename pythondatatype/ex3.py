"""
Squares
Write a program that prints a dictionary where the keys are numbers between 1 and N, and the values are square of keys.

Input Specification

The first line of input contains N
Output Specification

Print the dictionary

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:
For example:

Input	Result
10
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""

def squares(n):
    squares = {}
    for num in range(1,n+1):
        squares[num]=num*num
    return squares

print(squares(10))