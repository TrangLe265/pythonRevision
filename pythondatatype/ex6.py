"""
Sum a Collection of Numbers
Write a program that sums all of the numbers taken as input, while ignoring any input that is not a valid number.
Your program should display the current sum after each number is entered. It should display an error message after each non-numeric input, and then continue to sum any additional numbers entered by the user.  The program exits when the user enters 0. 
Ensure that your program works correctly for both integers and floating-point numbers.
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column
For example:

Input	Result
200
hello
10
0
The total is now 200.0
That wasn’t a number.
The total is now 210.0
The grand total is 210.0

"""

def sum(Input):
    sum = 0
    for val in Input:
        if not isinstance(val,(int, float)) :
            print("That wasn’t a number.")
        else:
            if int(val) > 0:
                sum += val
                print(f"The total is now {sum:.1f}")
            elif int(val) == 0:
                print(f"The grand total is {sum:.1f}")
                break

sum([200, "hello", 10, 0])