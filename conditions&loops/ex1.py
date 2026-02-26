"""
Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
Note: Don't add a new line in the end.
"""
def table_diff(n1,n2):
    for i in range(1,11):
        print(n1*i - n2*i, end = " ")

table_diff(6,4)