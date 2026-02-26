"""
Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 

If you will win: print "You" (without quotes)
If your friend will win: print "Friend" (without quotes)
"""

def winner(n):
    if n%2 == 0:
        print("Friend")
    else:
        print("You")

winner(4)

"""
Given an integer year. Print "True" (without quotes) if it can represent a leap year, otherwise print "False" (without quotes).      
"""
def is_leap(year):
    if year%4 == 0 and year%100 != 0:
        print("True")
    else: 
        print("False")

is_leap(2001)