"""
Given an integer n,  write a program to print the square wall of size n using nested loops. Try not to use String multiplication.
"""

def print_square(n):
    for i in range(n+1):
        print("* "*n)

#print_square(5)

"""
Given an integer n. Write a program to print the Right angle triangle wall. The length of perpendicular and base is n.  Use single loop and string multiplication.
"""
def print_right_angle_triangle(n):
    for i in range(1,n+1):
        print("* " * i)

#print_right_angle_triangle(3)

"""
Given an integer n. Write a program to print the Right angle triangle. The length of the perpendicular and base is n.  
"""
def print_triangle(n):
    for i in range(1,n+1):
        if i <= 2: 
            print("*" * i)
        elif i>2 and i<n:
            print("*" + " " * (i-2) +"*")
        elif i == n:
            print("*" * n)


def print_inverted_triangle(n):
    for i in range(n,0):
        print("*" * n)

print_inverted_triangle(10)